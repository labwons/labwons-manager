from pylabwons_stub.env import PATH
from pylabwons_stub.core.build.baseline import Baseline
from pylabwons_stub.schema.const.baseline import BASELINE
from pylabwons_stub.schema.const.bubble import BUBBLE, COLORS
from pylabwons_stub.utils import tools
from datetime import datetime
from pandas import DataFrame
from jinja2 import Environment, FileSystemLoader
from json import dumps
from sklearn.preprocessing import RobustScaler
from typing import Callable, Dict, Hashable, List
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import pylabwons as lw


class MarketBubble(Baseline):

    def __init__(self, logger:Callable=print):
        super().__init__(logger)
        self.logger(f'| DEPLOY MARKET BUBBLE ON {self.log.baseline.date}')

        self._extract()
        self._scaling()
        return

    @classmethod
    def __norm(cls, data):
        return (data - data.min()) / (data.max() - data.min())

    def _extract(self):
        copy = self[self['marketCap'] >= self['marketCap'].median()].copy()

        # CALC AND PROCESS
        copy['name'] = copy[['name', 'market']].apply(lambda r: f'{r[0]}*' if r[1] == 'kosdaq' else r[0], axis=1, raw=True)
        copy['size'] = np.power(self.__norm(np.log10(copy['marketCap'])), 3) * 100
        copy['meta'] = copy['name'] + '(' + copy.index + ')<br>' \
                     + '시가총액: ' + copy['marketCap'].apply(tools.int2krw) + '원<br>' \
                     + '종가: ' + copy['close'].apply(lambda x: f'{x:,d}원')
        copy['color'] = copy['sectorCode'].apply(lambda x: COLORS[x].hex)
        keys = list(BUBBLE.keys()) + \
               ['name', 'size', 'meta', 'color',
                'industryName', 'industryCode', 'sectorName', 'sectorCode']
        copy.drop(
            inplace=True,
            columns=[c for c in copy.columns if not c in keys]
        )
        for c in copy.columns:
            if not c in BASELINE:
                continue
            meta = BASELINE[c]
            if c.lower().endswith('pe'):
                copy[c] = copy[c].apply(lambda x: np.nan if x < 0 else x)
            if meta.data_type in [int, float]:
                copy[c] = pd.to_numeric(copy[c], errors='coerce')
        super(Baseline, self).__init__(copy)
        return

    def _scaling(self):
        scaler = RobustScaler()
        for col in self.columns:
            if not col.startswith('yoy'):
                continue
            self[f'{col}_Scaled'] = scaler.fit_transform(self[[col]])
        return

    @property
    def metadata(self) -> Dict:
        meta = {}
        for key, _meta in BUBBLE.items():
            meta[key] = {
                'label': BASELINE[key].kor_name,
                'unit': BASELINE[key].unit,
                'mean': float(round(self[key].mean(), 4)),
                'digit': BASELINE[key].round,
                'text': f'{key}_Scaled' in self,
                'dtype': str(BASELINE[key].data_type) \
                         .replace("<class ", "") \
                         .replace(">", "") \
                         .replace("'", ""),
            }
        return meta

    @property
    def sectors(self) -> DataFrame:
        sectors = self[['sectorCode', 'sectorName', 'color']] \
                  .drop_duplicates().dropna() \
                  .set_index(keys='sectorCode')
        return pd.concat([
            DataFrame({'sectorName': '전체', 'color': '#4169E1'}, index=['ALL']),
            sectors
        ])

    def deploy(self):
        date = datetime.strptime(self.log.baseline.date, "%Y%m%d %H:%M")
        with open(file=PATH.HTML.BUBBLE, mode='w', encoding='utf-8') as file:
            file.write(
                Environment(loader=FileSystemLoader(PATH.HTML.TEMPLATE)) \
                .get_template('bubble-1.0.0.html') \
                .render({
                    "title": "LAB￦ONS: 종목분포",
                    "srcTradingDate": f'"{date.strftime("%Y/%m/%d %H:%M")}"',
                    "srcTickers": self.to_json(orient='index'),
                    "srcSectors": self.sectors.to_json(orient='index'),
                    "srcIndicatorOpt": dumps(self.metadata),
                })
            )
        return

    def test_plot(
        self,
        x:str = 'returnOn1Day',
        y:str = 'returnOn1Month',
    ):
        ind = self.metadata
        x_d, y_d = self[x], self[y]
        if f'{x}_Scaled' in self:
            x_d = self[f'{x}_Scaled']
        if f'{y}_Scaled' in self:
            y_d = self[f'{y}_Scaled']

        text = "x: " + self[x].astype(str) + f"{ind[x]['unit']}<br>"\
               "y: " + self[y].astype(str) + f"{ind[y]['unit']}"
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x_d,
            y=y_d,
            mode='markers',
            marker={
                'size': self['size'],
                'color': self['color'],
            },
            meta=self['meta'],
            text=text,
            opacity=0.9,
            hovertemplate=f'%{{meta}}<br>%{{text}}<extra></extra>',
        ))
        fig.update_layout(
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            xaxis=dict(
                autorange=False,
                range=[1.05 * x_d.min(), 1.05 * x_d.max()]
            ),
            yaxis=dict(
                autorange=False,
                range=[1.05 * y_d.min(), 1.05 * y_d.max()]
            )
        )
        fig.show('browser')
        return


if __name__ == "__main__":
    bub = MarketBubble()
    # print(bub)
    # print(bub.sectors)
    print(lw.DataDict(bub.metadata))
    bub.deploy()
    # bub.test_plot(
    #     x='yoyEps'
    # )


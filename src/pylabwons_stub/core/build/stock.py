from pylabwons_stub.env import PATH, HOST
from pylabwons import Ticker
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from json import dumps
from typing import Union
if HOST == 'hkefico':
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context


class Stock(Ticker):

    # def deploy(self):
    #     file = PATH.HTML.STOCK / f'{self.ticker}.html'
    #     file.parent.mkdir(parents=True, exist_ok=True)
    #     with open(file=file, mode='w', encoding='utf-8') as file:
    #         file.write(
    #             Environment(loader=FileSystemLoader(PATH.HTML.TEMPLATE)) \
    #                 .get_template('stock-1.0.0.html') \
    #                 .render({
    #                 # "title": f"LAB￦ONS: {self['name']}({self.ticker})",
    #                 "title": f"LAB￦ONS: {self.snapshot['name']}({self.ticker})",
    #             })
    #         )
    #     return

    def release(self, path:Union[str, Path]=None):
        tech = {"date": self.ohlcv.index.strftime("%Y-%m-%d").tolist()}
        for col in self.ohlcv:
            tech[col] = self.ohlcv[col].tolist()

        if path is None:
            path = PATH.DATA / f'release/stock'
        file = path / f'{self.ticker}.html'
        file.parent.mkdir(parents=True, exist_ok=True)
        with open(file=file, mode='w', encoding='utf-8') as file:
            file.write(
                Environment(loader=FileSystemLoader(PATH.HTML.TEMPLATE)) \
                    .get_template('stock-release-1.0.0.html') \
                    .render({
                    "title": f"LAB￦ONS: {self.snapshot['name']}({self.ticker})",
                    "ticker": self.ticker,
                    "tech": dumps(tech),
                })
            )
        return


if __name__ == "__main__":
    import pandas as pd

    stock = Stock('000660')
    stock.baseline = pd.read_parquet(PATH.PARQUET.BASELINE, engine='pyarrow')
    stock.ohlcv = pd.read_parquet(r'C:\Users\Administrator\Downloads\sample_ohlcv.parquet', engine='pyarrow')
    stock.release(PATH.DOWNLOADS)

    print(stock.ohlcv.columns)
    # print(stock.ohlcv)
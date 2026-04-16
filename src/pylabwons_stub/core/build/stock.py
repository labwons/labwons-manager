from pylabwons_stub.env import PATH, HOST
from pylabwons import Ticker
from jinja2 import Environment, FileSystemLoader
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

    def release(self):
        file = PATH.DATA / f'release/stock/{self.ticker}.html'
        file.parent.mkdir(parents=True, exist_ok=True)
        with open(file=file, mode='w', encoding='utf-8') as file:
            file.write(
                Environment(loader=FileSystemLoader(PATH.HTML.TEMPLATE)) \
                    .get_template('stock-release-1.0.0.html') \
                    .render({
                    # "title": f"LAB￦ONS: {self['name']}({self.ticker})",
                    "title": f"LAB￦ONS: {self.snapshot['name']}({self.ticker})",
                    "ticker": self.ticker,
                })
            )
        return


if __name__ == "__main__":

    stock = Stock('000660')
    stock.release()
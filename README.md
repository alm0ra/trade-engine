
![Alt text](logo.png)

![GitHub](https://img.shields.io/github/license/xibalbas/trade-engine)
![GitHub all releases](https://img.shields.io/github/downloads/xibalbas/trade-engine/total)
![GitHub contributors](https://img.shields.io/github/contributors/xibalbas/trade-engine)
![GitHub repo size](https://img.shields.io/github/repo-size/xibalbas/trade-engine)
![GitHub top language](https://img.shields.io/github/languages/top/xibalbas/trade-engine)
![PyPI](https://img.shields.io/pypi/v/trade-engine)
# Trade Engine

a library for demo trading | backtest and forward test simulation

## Features
- [x] **Limit/Market orders**: you can place a Limit or Market order in 2 side "long", "Short" .
- [x] **SL/TP set**: you can set stop loss and take profit for your market or limit order .

# Documentations
    soon...

# Getting start

### install package
install package using [PyPI](https://pypi.org/project/trade-engine/)
```bash
pip install trade-engine
```
### import package 
```python
from trade_engine import TradeEngine
engine = TradeEngine()

# set balance ==> 1000$
engine.set_initial_balance(1000)

# place market order
engine.place_market_order(symbol="BTC/USDT",
                        entry_price=57900,
                        sl=54000,
                        tp=66000,
                        volume=100,
                        commission=0,
                        side="long"
                    )

# place Limit order
engine.place_limit_order(symbol="BTC/USDT",
                        entry_price=30000,
                        sl=27000,
                        tp=45000,
                        volume=100,
                        commission=0,
                        side="long"
                    )

```

# Contributing
Contributions are very welcome. There are a number of requirements:
* See Issues tab, and feel free to submit your own issues
* Add PRs if you discover a solution to an existing issue
* The code should be Pep8 compliant.
* Comments are required for every class and function and they should be a clear description.
* At least one broad test case and a set of unit tests must be provided for every function.
* Avoid very pythonic construction

# License
`trade-engine` is freely available under the MIT [license](https://github.com/xibalbas/trade-engine/blob/master/LICENSE).
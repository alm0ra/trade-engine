# Trade Engine Quick Start
![GitHub](https://img.shields.io/github/license/xibalbas/trade-engine)
![GitHub all releases](https://img.shields.io/github/downloads/xibalbas/trade-engine/total)
![GitHub contributors](https://img.shields.io/github/contributors/xibalbas/trade-engine)
![GitHub repo size](https://img.shields.io/github/repo-size/xibalbas/trade-engine)
![GitHub top language](https://img.shields.io/github/languages/top/xibalbas/trade-engine)
![PyPI](https://img.shields.io/pypi/v/trade-engine)

![Alt text](./assets/images/logo.png)

Trade Engine is an open source project for simulating Trade it use for Backtesting your strategy

## installation

* `pip install trade-engine` - install with Pypi.


## Usage

``` py title="main.py" linenums="1" hl_lines="10 11 12 13 14 15 16 17"
from trade_engine import TradeEngine

# make an Engine for trade
engine = TradeEngine()

# set balance ==> 1000$
engine.set_initial_balance(1000)

# Submit an market order order
engine.place_market_order(symbol="BTC/USDT",
                        entry_price=57900,
                        sl=54000,
                        tp=66000,
                        volume=100,
                        commission=0,
                        side="long"
                    )

```

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

## Features
- [x] **Limit/Market orders**: you can place a Limit or Market order in 2 side "long", "Short" .
- [x] **SL/TP set**: you can set stop loss and take profit for your market or limit order .
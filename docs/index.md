# Welcome to Trade Engine

here is Trade Engine library Documents

## installation

* `pip install trade-engine` - install with Pypi.


## Qucik Start

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


## title 1
asdasd
## title 2
asdasd
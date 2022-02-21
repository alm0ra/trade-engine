from src.trade_engine.trade_engine import TradeEngine
from pydantic import ValidationError

import unittest


class TestTradeEngine(unittest.TestCase):
    """Unit Test for Trade Engine Moudle Library

    """
    def __init__(self, *args, **kwargs):
        super(TestTradeEngine, self).__init__(*args, **kwargs)

        self.engine = TradeEngine()

    def test_place_limit_order(self):
        # Test Limit Order
        
        with self.assertRaises(ValidationError):
            self.engine.place_limit_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=5300,
                tp=54514,
                volume=54515,
                side="long",
            )
        with self.assertRaises(ValidationError):
            self.engine.place_limit_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=0,
                tp=0,
                volume=54515,
                side="long",
            )
        with self.assertRaises(ValidationError):
            self.engine.place_limit_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=0,
                tp=0,
                volume=54515,
                side="loasdng",
            )
        
        # Submit a True order
        self.engine.place_limit_order(
            symbol="BTCUSDT",
            entry_price=54850,
            sl=5320,
            tp=65400,
            volume=300,
            side="long",
        )
        self.assertEqual(self.engine.position_count(), 0)
        self.assertEqual(self.engine.order_count(), 1)
        self.assertEqual(self.engine.trade_count(), 0)
            
            
    def test_place_market_order(self):
        # Test Market Order
        
        with self.assertRaises(ValidationError):
            self.engine.place_market_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=5300,
                tp=54514,
                volume=54515,
                side="long",
            )
        with self.assertRaises(ValidationError):
            self.engine.place_market_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=0,
                tp=0,
                volume=54515,
                side="long",
            )
        with self.assertRaises(ValidationError):
            self.engine.place_market_order(
                symbol="BTCUSDT",
                entry_price=1,
                sl=0,
                tp=0,
                volume=54515,
                side="loasdng",
            )
        # Submit a True order
        self.engine.place_market_order(
            symbol="BTCUSDT",
            entry_price=54850,
            sl=5320,
            tp=65400,
            volume=300,
            side="long",
        )
        self.assertEqual(self.engine.position_count(), 1)
        self.assertEqual(self.engine.order_count(), 0)
        self.assertEqual(self.engine.trade_count(), 0)

    def test_set_initial_balance(self):
        # check Value Errors
        with self.assertRaises(ValueError):
            self.engine.set_initial_balance("asdasd")
        with self.assertRaises(ValueError):
            self.engine.set_initial_balance(-1)
        with self.assertRaises(ValueError):
            self.engine.set_initial_balance(0)
        with self.assertRaises(ValueError):
            self.engine.set_initial_balance(0.01)
        # set a True value
        self.engine.set_initial_balance(50)

        # check if saved
        self.assertEqual(self.engine.initial_balance, 50)

    def test_set_commision(self):
        # check Value Errors
        with self.assertRaises(ValueError):
            self.engine.set_commision("asdasd")
        with self.assertRaises(ValueError):
            self.engine.set_commision("asdasd")
        with self.assertRaises(ValueError):
            self.engine.set_commision(1245)
        with self.assertRaises(ValueError):
            self.engine.set_commision(-5415)
        with self.assertRaises(ValueError):
            self.engine.set_commision("")
        # set a True value
        self.engine.set_commision(0)
        self.engine.set_commision(0.002)
        # check if saved
        self.assertEqual(self.engine.commision, 0.002)

import pandas as pd
from .operations import EngineOperation


class TradeEngine:
    
    """Trade Engine Library
    if you want develope a backtest or forward test simulator welcome to TradeEngine
    in this class we have 2 type of order
    
        Limit order:
            a Limit order will execeute when price arrive to enter price
            and will known  as a position.
        Market order:
            a Market order will execute immediatly turn to position
            Market orders will close when price arrive to stop loss
            or take profit price.
    """
    def __init__(self) -> None:
        self.operations = EngineOperation()
        
        self.open_orders = []
        self.open_positions = []
        self.trade_list = []
        
        self.open_price = None
        self.close_price = None
        self.high_price = None
        self.low_price = None
        self.csv_template = None
        
        self.initial_balance = 0
        self.final_balance = 0
        self.profit_loss = 0

    def position_count(self):
        """
        Returns:
            float: number of open positions
        """
        return len(self.open_positions)
    
    def order_count(self):
        """
        Returns:
            float: number of open orders
        """
        return len(self.open_orders)
    
    def trade_count(self):
        """
        Returns:
            float: number of trades in trade list
        """
        return len(self.trade_list)
    
    def set_initial_balance(self, balance: float):
        """set initial money for demo trade

        Args:
            balance (float): a positive number that show your initial money
        """
        self.initial_balance = float(balance)
        
    def clean_all(self):
        """
            clean all Open orders / open positions / trade history
        """
        self.open_orders = []
        self.open_positions = []
        self.trade_list = []

    def clean_all_orders(self):
        """
            clean all open orders
        """
        self.open_orders = []
        
    def candle_checker(self, open: float, high: float, low: float, close: float):
        """check open orders / open positions and wait for execute order
        or close a open position by each candle

        Args:
            open (float): open price
            high (float): high price
            low (float): low price
            close (float): close price
        """
        self.open_price = open
        self.high_price = high
        self.low_price = low
        self.close_price = close
        self.check_orders(high=high, low=low, close=close)
        self.check_positions(high=high, low=low, close=close)
        
    def check_orders(self, high, low, close):
        """
            Check all Limit orders with every candle and if executed it wil be known as a position
        """

        for order in self.open_orders:

            if order["order_status"] != "BadOrdering(10001)":

                enter_price = float(order["enter_price"])
                side = order["side"]

                if order["order_type"] == "limit":
                    if low <= enter_price <= high:
                        self.execute_limit_order(order)

                    if side == "long":
                        if low < enter_price:
                            order["order_status"] = "BadOrdering(10001)"
                    if side == "short":
                        if high > enter_price:
                            order["order_status"] = "BadOrdering(10001)"

    def check_positions(self, high, low, close):
        """
            Check all open positions with every candle and if closed it wil be known as a Trade in Trade History
        """
        for position in self.open_positions:
            sl = float(position["stop_loss"])
            tp = float(position["take_profit"])
            enter_price = float(position["enter_price"])
            side = position["side"]

            if side == "long":

                # check if Stop loss Take profit hit
                if low <= sl <= high or low < sl:
                    position["unrealized_profit_loss"] =0
                    self.close_position(position=position, closed_price=sl)
                elif low <= tp <= high or high > tp:
                    position["unrealized_profit_loss"] = 0
                    self.close_position(position=position, closed_price=tp)
                else:
                    # check unrealized profit status
                    position["unrealized_profit_loss"] = self.operations.realized_pnl_percent(side=side, entry_price=enter_price,
                                                                                              close_price=close)
            if side == "short":
                # check unrealized profit status

                # check if Stop loss Take profit hit
                if low <= sl <= high or high > sl:
                    position["unrealized_profit_loss"] = 0
                    self.close_position(position=position, closed_price=sl)
                elif low <= tp <= high or low < tp:
                    position["unrealized_profit_loss"] = 0
                    self.close_position(position=position, closed_price=tp)
                else:
                    # check unrealized profit status
                    position["unrealized_profit_loss"] = self.operations.realized_pnl_percent(side=side, entry_price=enter_price,
                                                                                              close_price=close)

    def place_market_order(self, symbol: str, entry_price: float, sl: float, tp: float, volume: float,
                           commission: float, side: str) -> None:
        """
        it uses for placing a market order (this order will be executed at entry price,
        entry price is close price of current candle)
        """
        position = {
            "symbol": f"{symbol}",
            "order_status": "executed",
            "position_status": "open",
            "order_type": "market",
            "side": f"{side}",
            "enter_price": f"{entry_price}",
            "stop_loss": f"{sl}",
            "take_profit": f"{tp}",
            "volume": f"{volume}",
            "commission": f"{commission}",
            "unrealized_profit_loss": "",
            "realized_profit_loss": "",
            "close_price": "",
            "trade_status": "",  # sl_hit, tp_hit, closed
            "realized_profit_loss_percent": "",
            "final_volume": "",
        }

        self.open_positions.append(position)

    def place_limit_order(self, symbol: str, entry_price: float, sl: float, tp: float, volume: float,
                          commission: float, side: str):
        """
            it uses for placing a Limit Order (this order will be executed when price arrived to entry price)
            Notice1 : BadOrdering(10001)
                    it's status of order that we can't execute them because they are not Limit order anymore
                    Limit Order side Long:
                        Bad Condition:
                            current price < Enter price
                        if price is under enter price we can't execute this order, and we know this as bad order

                    Limit Order side short:
                        Bad Condition:
                            current price > Enter price
                        if price is upper enter price we can't execute this order, and we know this as bad order

        """
        order = {
            "symbol": f"{symbol}",
            "order_status": "open",
            "position_status": "NotExecuted",
            "order_type": "limit",
            "side": f"{side}",
            "enter_price": f"{entry_price}",
            "stop_loss": f"{sl}",
            "take_profit": f"{tp}",
            "volume": f"{volume}",
            "commission": f"{commission}",
            "unrealized_profit_loss": "",
            "realized_profit_loss": "",
            "close_price": "",
            "trade_status": "",  # sl_hit, tp_hit, closed
            "realized_profit_loss_percent": "",
            "final_volume": "",
        }
        self.open_orders.append(order)

    def execute_limit_order(self, order):
        """
            it uses for executing limit orders (it changes an order to position)
        """
        # remove from open orders
        if order["order_status"] != "BadOrdering(10001)":
            self.open_orders.remove(order)

            order["order_status"] = "executed"
            order["position_status"] = "open"
            # add to open positions
            self.open_positions.append(order)

    def calculate_account_loss_profit(self):
        """
            Get all Trade and add profits or losses to account balance
        """
        self.final_balance = 0
        
        for trade in self.trade_list:
            self.final_balance = self.initial_balance + round(float(trade["realized_profit_loss"]), 2)
        self.profit_loss = round((self.final_balance - self.initial_balance) / self.initial_balance * 100, 2)

        return {
            "initial_balance": self.initial_balance, 
            "final_balance":self.final_balance, 
            "profit/loss": self.profit_loss
            }

    def close_all_positions(self, closed_price):
        """
            Get all open positions and close them
        """
        
        for position in self.open_positions:
            self.close_position(position=position, closed_price=closed_price)

    def close_position(self, position, closed_price):
        """
            closing open position and write into trade history .
        """
        self.open_positions.remove(position)
        position["position_status"] = "closed"
        position["close_price"] = closed_price
        position["unrealized_profit_loss"] = 0

        entry_price = float(position["enter_price"])
        sl = float(position["stop_loss"])
        tp = float(position["take_profit"])
        volume = float(position["volume"])
        side = str(position["side"])

        if side == "long":
            position["realized_profit_loss"] = self.operations.realized_pnl(side="long", volume=volume,
                                                                entry_price=entry_price, close_price=closed_price)
            position["realized_profit_loss_percent"] = self.operations.realized_pnl_percent(side="long",
                                                                entry_price=entry_price, close_price=closed_price)
            position["final_volume"] = self.operations.final_volume(side="long", volume=volume,
                                                                entry_price=entry_price, close_price=closed_price)

        if side == "short":
            position["realized_profit_loss"] = self.operations.realized_pnl(side="short", volume=volume,
                                                    entry_price=entry_price, close_price=closed_price)
            position["realized_profit_loss_percent"] = self.operations.realized_pnl_percent(side="short",
                                                                entry_price=entry_price, close_price=closed_price)
            position["final_volume"] = self.operations.final_volume(side="short", volume=volume,
                                                                entry_price=entry_price, close_price=closed_price)
            
        if closed_price == sl:
            position["trade_status"] = "sl_hit"
        elif closed_price == tp:
            position["trade_status"] = "tp_hit"
        else:
            position["trade_status"] = "closed"


        self.trade_list.append(position)

    def save_trade_report(self, report_path="./"):
        """
            Get all Trade and save them in a Csv file
        """
        self.csv_template = pd.DataFrame(
            columns=['symbol', 'order_status', 'position_status', 'side', 'enter_price',
                     'stop_loss', 'take_profit', 'volume', 'commission', 'unrealized_profit_loss',
                     'realized_profit_loss', 'close_price', 'trade_status',
                     'realized_profit_loss_percent', 'final_volume'])
        for trade in self.trade_list:
            self.csv_template = self.csv_template.append(trade, ignore_index=True)

        self.csv_template.to_csv(report_path)
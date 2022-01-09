class EngineOperation:
    
    """Engine Operations
    All operations realted to TradeEngine class wrote here
    """
    def __init__(self) -> None:
        pass
    
    def realized_pnl(self,side:str, volume: float, entry_price: float, close_price: float):
        """caculate realized pnl when position is closed by close price

        Args:
            side (str): side of position "long" or "short"
            volume (float): amount of position in $
            entry_price (float): price you open position
            close_price (float): price you close position

        Returns:
            (float): realized pnl amount
        """
        if side == "long":
            return round(volume * (close_price - entry_price) / entry_price, 2)
        
        elif side == "short":
            return round(- volume * (entry_price - close_price) / entry_price, 2)
    
    def realized_pnl_percent(self, side, entry_price, close_price):
        """caculate realized pnl %  when position is closed by close price

        Args:
            side (str): side of position "long" or "short"
            entry_price (float): price you open position
            close_price (float): price you close position

        Returns:
            (float): realized pnl percent %
        """
        if side == "long":
            return round((close_price - entry_price) / entry_price * 100, 2)
        
        elif side == "short":
            return round((entry_price - close_price) / entry_price * 100, 2)
    
    def final_volume(self, side, volume, entry_price, close_price):
        """caculate final volume  when position is closed by close price

        Args:
            side (str): side of position "long" or "short"
            volume (float): amount of position in $
            entry_price (float): price you open position
            close_price (float): price you close position

        Returns:
            (float): final volume
        """
        if side == "long":
            return round(volume + volume * (close_price - entry_price) / entry_price, 2)
        
        elif side == "short":
            return round(volume + volume * (entry_price - close_price) / entry_price, 2)
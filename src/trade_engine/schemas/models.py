from pydantic import BaseModel, validator, Extra, Field,root_validator
from typing_extensions import Literal
from typing import Union

class Order(BaseModel):
    """Validation for Order Inputs
    """
    symbol: str
    entry_price: float = Field(gt=0)
    sl: float = Field(gt=0)
    tp: float = Field(gt=0)
    volume: float = Field(gt=0)
    side: Union[
        Literal["long"],
        Literal["short"],
    ]
    
    @root_validator(pre=True)
    def do_validation(cls, values):
        # check short long
        if values['side'] == "long":
            if not values['sl'] < values['entry_price'] < values['tp']:
                raise ValueError('Bad Possition . In Long position sl < entry_price <tp')
        
        # check short short
        else:
            if not values['sl'] > values['entry_price'] > values['tp']:
                raise ValueError('Bad Possition . In short position sl > entry_price >tp')
        return values
    
class Commision(BaseModel, extra=Extra.forbid):
    """Validation for Commision
    """
    commision: float = Field(ge=0, lt=0.1)
    

class Balance(BaseModel, extra=Extra.forbid):
    """Validation for Balance
    """
    balance: float = Field(gt=10)
    
    
from pydantic import BaseModel,Field
from typing import Optional


class Supplies(BaseModel):
    id: Optional[int]=None
    supplier_id: int= Field(ge=1)
    product_id: int= Field (ge=1)
    purchase_price: float= Field(len=5)


    class Config:
        schema_extra= {
            "example":{
                'id':1,
                'supplier_id': 4,
                'product_id': 5,
                'purchase_price': 6
            }
        }
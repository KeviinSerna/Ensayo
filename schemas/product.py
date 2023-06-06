from pydantic import BaseModel,Field
from typing import Optional


class product(BaseModel):
    id: Optional[int]= None
    name: str= Field(max_length= 30, min_length= 3)
    brand: str= Field(max_length= 30, min_length= 3)
    description: str= Field(max_length= 300, min_length= 3)
    price: float= Field(len=300)
    entry_date: str= Field(max_length= 10, min_length= 10)
    availability: bool= Field(description= "Yes or No")
    available_quantity: int= Field(len=10)


    class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'gaseosa',
                    'brand': "postobon",
                    'description':"bebida saborizada, azucarada y con gas",
                    'price': 3.0,
                    'entry_date':'06/06/2023',
                    'availability': True,
                    'available_quantity': 8
                }
            }
from pydantic import BaseModel,Field
from typing import Optional


class Supplier(BaseModel):
    id: Optional[int]= None
    name: str= Field(max_length= 30, min_length= 3)
    address: str= Field(max_length= 30, min_length= 3)
    phone: int= Field(len= 10)
    email: str= Field(max_length= 30)


    class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'postobon',
                    'address': "carmen de viboral",
                    'phone': 3133333333,
                    'email': "postobon@gmail.com"
                }
            }
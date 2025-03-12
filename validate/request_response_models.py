from pydantic import BaseModel, Field, AfterValidator, IPvAnyAddress, condecimal
from typing import Annotated
from uuid import UUID
from validate.functions import check_passport

Money = condecimal(max_digits=10, decimal_places=2)

class CreateLoanBid(BaseModel):
    user_id: Annotated[UUID, 
                       Field(title="Unique identifier of user creating loan", 
                             description="Enter UUID of user")]
    loan_amount: Annotated[Money,  # type: ignore
                           Field(title="Amount of money for loan", 
                                 description="Specify amount of money for loan")]
    term_amount: Annotated[int, 
                           Field(title="A period for loan", 
                                 description="Specify a period for loan to be repaid")]
    passport: Annotated[str, 
                        Field(title="Passport number and series",
                              description="Enter series and then number of passport as a single line without spaces",
                              max_length=10, 
                              min_length=10, 
                              examples=["5741002204", "3068479533"]), 
                        AfterValidator(check_passport)]
    income: int
    ip_address: Annotated[IPvAnyAddress | None,
                          Field(default=None, 
                                title="IP address, optional parameter", 
                                description="Enter IPv4 or IPv6 address or just don't add this parameter",
                                examples=["210.67.44.36", "424e:37ae:2c3b:7d60:6d25:8861:dec0:0c40"])]

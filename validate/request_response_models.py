from pydantic import BaseModel, Field, AfterValidator, IPvAnyAddress, condecimal
from typing import Annotated
from uuid import UUID
from validate.functions import check_passport
from datetime import datetime
from enum import Enum


class LoanStatus(str, Enum):
    pending = "pending"
    in_review = "in_review"
    ready_for_decision = "ready_for_decision"
    approved = "approved"
    rejected = "rejected"


class FraudStatus(str, Enum):
    pending = "pending"
    in_review = "in_review"
    safe = "safe"
    high_risk = "high_risk"
    manual = "manual_review"


class Progress(LoanStatus, FraudStatus):
    scoring_status = LoanStatus
    document_status = LoanStatus
    fraud_status = FraudStatus


AmountMoney = condecimal(max_digits=10, decimal_places=2)


class CreateLoanBid(BaseModel):
    user_id: Annotated[UUID, 
                       Field(title="Unique identifier of user creating loan", 
                             description="Enter UUID of user")]
    loan_amount: Annotated[AmountMoney,  # type: ignore
                           Field(title="Amount of money for loan", 
                                 description="Specify amount of money for loan")]
    term_amount: Annotated[int, 
                           Field(title="Quantity of days for period of loan", 
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


class CreateLoanResponse(BaseModel):
    loan_id: Annotated[UUID, 
                        Field(description="Unique identifier of loan bid")]
    amount: Annotated[AmountMoney, # type: ignore
                      Field(description="amount of money for loan")]
    term_months: Annotated[int, 
                           Field(description="quantity of months of period")]
    loan_status: Annotated[LoanStatus, 
                           Field(description="status of loan bid")]
    progress: Annotated[Progress,
                        Field(description="")]
    created_at: Annotated[datetime,
                          Field(description="")]
    updated_at: Annotated[datetime,
                          Field(description="")]

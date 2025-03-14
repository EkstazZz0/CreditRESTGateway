from pydantic import BaseModel
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


class Progress(BaseModel):
    scoring_status: LoanStatus
    document_status: LoanStatus
    fraud_status: FraudStatus
from fastapi import APIRouter

from uuid import UUID, uuid4
from ..models.loans.progress import Progress

router = APIRouter(
    prefix="/api/v1",
    tags="API v1"
)


# @router.post("/loan/apply")
# async def create_loan(create_loan_bid: CreateLoanBid) -> Progress:
#     loan_id = uuid4()

#     return Progress(scoring_status=LoanStatus.ready_for_decision, 
#                     document_status=LoanStatus.in_review, 
#                     fraud_status=FraudStatus.pending)


@router.get("/loan/status/{loan_id}")
async def get_loan_status(
    loan_id: UUID
) -> Progress:
    progress = None
    #getting progress from database by loan_id

    return progress
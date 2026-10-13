from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.proposal import ProposalRequest, ProposalResponse
from ..services.proposal_generator import ProposalGenerator
from ..models.models import Proposal, User
from ..auth import get_current_user
from datetime import datetime

router = APIRouter()
proposal_generator = ProposalGenerator()

@router.post("/generate", response_model=ProposalResponse)
async def generate_proposal(
    request: ProposalRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        # Generate proposal
        response = proposal_generator.generate_proposal(request)
        
        # Save to database
        proposal = Proposal(
            user_id=current_user.id,
            tender_title=request.tender_requirements.title,
            proposal_text=response.proposal_text,
            tone=request.tone,
            generated_at=datetime.fromisoformat(response.generated_at)
        )
        db.add(proposal)
        db.commit()
        db.refresh(proposal)
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def get_proposal_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    proposals = db.query(Proposal).filter(Proposal.user_id == current_user.id).all()
    return proposals 
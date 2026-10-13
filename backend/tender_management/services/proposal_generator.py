from datetime import datetime
from typing import List
from ..schemas.proposal import ProposalRequest, ProposalResponse, ProposalTone

class ProposalGenerator:
    def __init__(self):
        self.templates = {
            ProposalTone.FORMAL: self._generate_formal_proposal,
            ProposalTone.CONCISE: self._generate_concise_proposal,
            ProposalTone.TECHNICAL: self._generate_technical_proposal,
            ProposalTone.MARKETING: self._generate_marketing_proposal
        }

    def generate_proposal(self, request: ProposalRequest) -> ProposalResponse:
        generator = self.templates.get(request.tone, self._generate_formal_proposal)
        proposal_text, sections = generator(request)
        
        return ProposalResponse(
            proposal_text=proposal_text,
            sections=sections,
            generated_at=datetime.now().isoformat(),
            tone=request.tone
        )

    def _generate_formal_proposal(self, request: ProposalRequest) -> tuple[str, List[str]]:
        sections = [
            "Executive Summary",
            "Company Overview",
            "Project Understanding",
            "Proposed Solution",
            "Implementation Plan",
            "Budget and Timeline",
            "Conclusion"
        ]
        
        proposal = f"""
# {request.tender_requirements.title} - Proposal

## Executive Summary
{request.company_profile.name} is pleased to submit this proposal for {request.tender_requirements.title}. 
With {request.company_profile.years_of_experience} years of experience in {request.company_profile.industry}, 
we are well-positioned to deliver exceptional results.

## Company Overview
{request.company_profile.name} brings extensive expertise in:
{self._format_list(request.company_profile.expertise)}

Notable achievements include:
{self._format_list(request.company_profile.achievements)}

## Project Understanding
We have carefully reviewed the tender requirements and understand that the project scope includes:
{request.tender_requirements.scope}

Key requirements:
{self._format_list(request.tender_requirements.requirements)}

## Proposed Solution
Our approach leverages our experience in similar projects:
{self._format_list(request.company_profile.past_projects)}

## Implementation Plan
[Implementation details will be customized based on specific requirements]

## Budget and Timeline
[Budget and timeline details will be provided based on project scope]

## Conclusion
We look forward to the opportunity to work on this project and are confident in our ability to deliver 
exceptional results that meet all requirements.
"""
        return proposal, sections

    def _generate_concise_proposal(self, request: ProposalRequest) -> tuple[str, List[str]]:
        sections = ["Overview", "Solution", "Benefits", "Next Steps"]
        proposal = f"""
# {request.tender_requirements.title} - Proposal

## Overview
{request.company_profile.name} proposes to deliver {request.tender_requirements.title} leveraging our 
{request.company_profile.years_of_experience} years of experience in {request.company_profile.industry}.

## Solution
Our solution addresses all key requirements:
{self._format_list(request.tender_requirements.requirements)}

## Benefits
- Proven track record in similar projects
- Strong expertise in {', '.join(request.company_profile.expertise[:3])}
- Focused on delivering measurable results

## Next Steps
We are ready to begin work immediately upon approval.
"""
        return proposal, sections

    def _generate_technical_proposal(self, request: ProposalRequest) -> tuple[str, List[str]]:
        sections = [
            "Technical Overview",
            "Methodology",
            "Technical Specifications",
            "Implementation Details",
            "Quality Assurance"
        ]
        proposal = f"""
# Technical Proposal: {request.tender_requirements.title}

## Technical Overview
{request.company_profile.name} brings deep technical expertise in:
{self._format_list(request.company_profile.expertise)}

## Methodology
Our approach is based on industry best practices and proven methodologies.

## Technical Specifications
Detailed technical specifications will address:
{self._format_list(request.tender_requirements.requirements)}

## Implementation Details
Implementation will follow a structured approach with clear milestones and deliverables.

## Quality Assurance
Our QA process ensures all deliverables meet the highest technical standards.
"""
        return proposal, sections

    def _generate_marketing_proposal(self, request: ProposalRequest) -> tuple[str, List[str]]:
        sections = [
            "Value Proposition",
            "Market Position",
            "Success Stories",
            "Partnership Benefits",
            "Call to Action"
        ]
        proposal = f"""
# {request.tender_requirements.title} - Partnership Proposal

## Value Proposition
{request.company_profile.name} offers a unique combination of expertise and experience that will 
deliver exceptional value for {request.tender_requirements.title}.

## Market Position
As a leader in {request.company_profile.industry}, we bring:
{self._format_list(request.company_profile.achievements)}

## Success Stories
Our track record includes:
{self._format_list(request.company_profile.past_projects)}

## Partnership Benefits
- Proven expertise in {', '.join(request.company_profile.expertise)}
- {request.company_profile.years_of_experience} years of industry experience
- Strong focus on client success

## Call to Action
Let's discuss how we can work together to achieve outstanding results.
"""
        return proposal, sections

    def _format_list(self, items: List[str]) -> str:
        return "\n".join(f"- {item}" for item in items) 
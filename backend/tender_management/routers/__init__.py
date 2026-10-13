# Import all routers
from .auth import router as auth_router
from .tenders import router as tenders_router
from .companies import router as companies_router
from .bids import router as bids_router
from .notifications import router as notifications_router
from .analytics import router as analytics_router

__all__ = [
    'auth_router',
    'tenders_router',
    'companies_router',
    'bids_router',
    'notifications_router',
    'analytics_router'
]

# This file makes the routers directory a Python package 
import os
import sys
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))

# Now use relative imports
from app.database import Base, engine
from app.models.models import User, Company, Tender, Bid, Notification, Proposal

def init_db():
    """Initializes database by creating all defined tables."""
    print("Current working directory:", os.getcwd())
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()

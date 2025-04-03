# Tender Management System

A comprehensive platform for managing tenders, matching companies with relevant opportunities, and streamlining the bidding process.

## Features

- Data Collection & Processing
- AI Model Development
- User Interface & Experience
- Notification System
- Bid Evaluation System
- API Integration
- Reporting & Analytics
- Feedback & Improvement Loop

## Project Structure

```
tendor-management/
├── backend/                 # FastAPI backend
│   ├── app/                # Application code
│   ├── models/             # Database models
│   ├── services/           # Business logic
│   └── tests/              # Backend tests
├── frontend/               # React frontend
│   ├── src/                # Source code
│   ├── components/         # React components
│   └── public/             # Static files
└── docs/                   # Documentation
```

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run the backend server:
```bash
uvicorn app.main:app --reload
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm start
```

## Environment Variables

Create a `.env` file in the backend directory with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/tendor_db
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_secret_key
```

## License

MIT 
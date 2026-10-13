import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// Layout
import Layout from './components/Layout';

// Auth Pages
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";

// Dashboard
import Dashboard from "./pages/Dashboard";

// Tender Pages
import Tenders from "./pages/tenders/Tenders";
import TenderDetail from "./pages/tenders/TenderDetail";

// Bid Pages
import Bids from "./pages/bids/Bids";
import BidDetail from "./pages/bids/BidDetail";
import EditBid from "./pages/bids/EditBid";
import NewBid from "./pages/bids/NewBid";

// Company Pages
import CompanyProfile from "./pages/company/CompanyProfile";

// Proposal Generator
import ProposalGenerator from "./pages/ProposalGenerator";

const theme = createTheme({
  palette: {
    primary: { main: "#1976d2" },
    secondary: { main: "#dc004e" },
    background: { default: "#f5f5f5" },
  },
  typography: { fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif' },
});

const PrivateRoute = ({ children }) => {
  const { isAuthenticated } = useSelector((state) => state.auth);
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          {/* Public Routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* Protected Routes */}
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Layout />
              </PrivateRoute>
            }
          >
            <Route index element={<Dashboard />} />
            <Route path="tenders" element={<Tenders />} />
            <Route path="tenders/:id" element={<TenderDetail />} />
            <Route path="bids" element={<Bids />} />
            <Route path="bids/new" element={<NewBid />} />
            <Route path="bids/:id" element={<BidDetail />} />
            <Route path="bids/:id/edit" element={<EditBid />} />
            <Route path="company" element={<CompanyProfile />} />
            <Route path="proposal-generator" element={<ProposalGenerator />} />
          </Route>

          {/* Catch all route */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;

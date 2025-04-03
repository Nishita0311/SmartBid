import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { Provider } from 'react-redux';
import { store } from './store';

// Layout Components
import Layout from './components/layout/Layout';
import PrivateRoute from './components/auth/PrivateRoute';

// Auth Pages
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';

// Main Pages
import Dashboard from './pages/Dashboard';
import Tenders from './pages/tenders/Tenders';
import TenderDetail from './pages/tenders/TenderDetail';
import CompanyProfile from './pages/company/CompanyProfile';
import Bids from './pages/bids/Bids';
import BidDetail from './pages/bids/BidDetail';
import Analytics from './pages/analytics/Analytics';
import Notifications from './pages/notifications/Notifications';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
    background: {
      default: '#f5f5f5',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  },
});

function App() {
  return (
    <Provider store={store}>
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
              <Route path="tenders">
                <Route index element={<Tenders />} />
                <Route path=":id" element={<TenderDetail />} />
              </Route>
              <Route path="company" element={<CompanyProfile />} />
              <Route path="bids">
                <Route index element={<Bids />} />
                <Route path=":id" element={<BidDetail />} />
              </Route>
              <Route path="analytics" element={<Analytics />} />
              <Route path="notifications" element={<Notifications />} />
            </Route>

            {/* Catch all route */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Router>
      </ThemeProvider>
    </Provider>
  );
}

export default App; 
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  Button,
  Box,
  Chip
} from '@mui/material';

const Bids = () => {
  const navigate = useNavigate();
  const [bids, setBids] = useState([]);

  useEffect(() => {
    // TODO: Fetch bids from API
    setBids([
      {
        id: 1,
        tenderTitle: 'Road Construction Project',
        amount: '$950,000',
        status: 'Submitted',
        submissionDate: '2024-03-15',
        lastModified: '2024-03-15'
      },
      {
        id: 2,
        tenderTitle: 'School Building Project',
        amount: '$450,000',
        status: 'Under Review',
        submissionDate: '2024-03-10',
        lastModified: '2024-03-12'
      }
    ]);
  }, []);

  const getStatusColor = (status) => {
    switch (status) {
      case 'Submitted':
        return 'info';
      case 'Under Review':
        return 'warning';
      case 'Accepted':
        return 'success';
      case 'Rejected':
        return 'error';
      default:
        return 'default';
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
        <Typography variant="h4" component="h1">
          My Bids
        </Typography>
        <Button variant="contained" color="primary">
          New Bid
        </Button>
      </Box>
      
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Tender Title</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Submission Date</TableCell>
              <TableCell>Last Modified</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {bids.length === 0 ? (
              <TableRow>
                <TableCell colSpan={6} align="center">
                  No bids available
                </TableCell>
              </TableRow>
            ) : (
              bids.map((bid) => (
                <TableRow key={bid.id}>
                  <TableCell>{bid.tenderTitle}</TableCell>
                  <TableCell>{bid.amount}</TableCell>
                  <TableCell>
                    <Chip 
                      label={bid.status} 
                      color={getStatusColor(bid.status)}
                      size="small"
                    />
                  </TableCell>
                  <TableCell>{bid.submissionDate}</TableCell>
                  <TableCell>{bid.lastModified}</TableCell>
                  <TableCell>
                    <Button 
                      variant="outlined" 
                      size="small"
                      onClick={() => navigate(`/bids/${bid.id}`)}
                    >
                      View Details
                    </Button>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default Bids;

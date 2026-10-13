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
  Box
} from '@mui/material';

const Tenders = () => {
  const navigate = useNavigate();
  const [tenders, setTenders] = useState([]);

  useEffect(() => {
    // TODO: Fetch tenders from API
    setTenders([
      {
        id: 1,
        title: 'Road Construction Project',
        description: 'Construction of 10km highway',
        deadline: '2024-12-31',
        budget: '$1,000,000',
        status: 'Open'
      },
      {
        id: 2,
        title: 'School Building Project',
        description: 'Construction of new school building',
        deadline: '2024-11-30',
        budget: '$500,000',
        status: 'Open'
      }
    ]);
  }, []);

  const handleTenderClick = (tenderId) => {
    navigate(`/tenders/${tenderId}`);
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
        <Typography variant="h4" component="h1">
          Active Tenders
        </Typography>
        <Button variant="contained" color="primary">
          Create New Tender
        </Button>
      </Box>
      
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Title</TableCell>
              <TableCell>Description</TableCell>
              <TableCell>Deadline</TableCell>
              <TableCell>Budget</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {tenders.length === 0 ? (
              <TableRow>
                <TableCell colSpan={6} align="center">
                  No tenders available
                </TableCell>
              </TableRow>
            ) : (
              tenders.map((tender) => (
                <TableRow 
                  key={tender.id}
                  hover
                  onClick={() => handleTenderClick(tender.id)}
                  sx={{ cursor: 'pointer' }}
                >
                  <TableCell>{tender.title}</TableCell>
                  <TableCell>{tender.description}</TableCell>
                  <TableCell>{tender.deadline}</TableCell>
                  <TableCell>{tender.budget}</TableCell>
                  <TableCell>{tender.status}</TableCell>
                  <TableCell>
                    <Button 
                      variant="outlined" 
                      size="small"
                      onClick={(e) => {
                        e.stopPropagation();
                        navigate(`/tenders/${tender.id}/edit`);
                      }}
                    >
                      Edit
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

export default Tenders;

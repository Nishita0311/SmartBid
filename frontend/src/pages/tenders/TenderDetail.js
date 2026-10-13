import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Typography,
  Grid,
  Box,
  Button,
  Divider,
  Chip,
  List,
  ListItem,
  ListItemText
} from '@mui/material';

const TenderDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [tender, setTender] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // TODO: Fetch tender details from API
    setLoading(false);
    setTender({
      id,
      title: 'Road Construction Project',
      description: 'Construction of 10km highway with modern infrastructure and safety features.',
      deadline: '2024-12-31',
      budget: '$1,000,000',
      status: 'Open',
      requirements: [
        'Minimum 5 years of experience in road construction',
        'Valid construction license',
        'Previous government contracts',
        'Safety certification',
        'Environmental compliance certificate'
      ],
      documents: [
        { name: 'Technical Specifications', url: '#' },
        { name: 'Terms and Conditions', url: '#' },
        { name: 'Bid Form', url: '#' }
      ]
    });
  }, [id]);

  if (loading) {
    return (
      <Container>
        <Typography>Loading...</Typography>
      </Container>
    );
  }

  if (!tender) {
    return (
      <Container>
        <Typography>Tender not found</Typography>
      </Container>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
          <Typography variant="h4" component="h1">
            {tender.title}
          </Typography>
          <Chip label={tender.status} color={tender.status === 'Open' ? 'success' : 'default'} />
        </Box>

        <Grid container spacing={3}>
          <Grid item xs={12} md={8}>
            <Typography variant="h6" gutterBottom>
              Description
            </Typography>
            <Typography paragraph>
              {tender.description}
            </Typography>

            <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
              Requirements
            </Typography>
            <List>
              {tender.requirements.map((req, index) => (
                <ListItem key={index}>
                  <ListItemText primary={req} />
                </ListItem>
              ))}
            </List>
          </Grid>

          <Grid item xs={12} md={4}>
            <Paper variant="outlined" sx={{ p: 2 }}>
              <Typography variant="h6" gutterBottom>
                Tender Details
              </Typography>
              <Divider sx={{ my: 2 }} />
              
              <Box sx={{ mb: 2 }}>
                <Typography color="textSecondary">Budget</Typography>
                <Typography variant="h6">{tender.budget}</Typography>
              </Box>

              <Box sx={{ mb: 2 }}>
                <Typography color="textSecondary">Deadline</Typography>
                <Typography variant="h6">{tender.deadline}</Typography>
              </Box>

              <Button 
                variant="contained" 
                color="primary" 
                fullWidth 
                sx={{ mt: 2 }}
                onClick={() => navigate('/proposal-generator')}
              >
                Submit Proposal
              </Button>
            </Paper>

            <Paper variant="outlined" sx={{ p: 2, mt: 2 }}>
              <Typography variant="h6" gutterBottom>
                Documents
              </Typography>
              <List>
                {tender.documents.map((doc, index) => (
                  <ListItem key={index} sx={{ px: 0 }}>
                    <Button 
                      href={doc.url}
                      color="primary"
                      sx={{ textAlign: 'left' }}
                    >
                      {doc.name}
                    </Button>
                  </ListItem>
                ))}
              </List>
            </Paper>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
};

export default TenderDetail;

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Typography,
  Box,
  Grid,
  Button,
  Chip,
  Divider,
  List,
  ListItem,
  ListItemText,
  Alert
} from '@mui/material';

const BidDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [bid, setBid] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // TODO: Fetch bid details from API
    setBid({
      id: 1,
      tenderTitle: 'Road Construction Project',
      amount: '$950,000',
      status: 'Submitted',
      submissionDate: '2024-03-15',
      lastModified: '2024-03-15',
      description: 'Detailed proposal for the road construction project including timeline, materials, and methodology.',
      documents: [
        { name: 'Technical Proposal.pdf', type: 'PDF' },
        { name: 'Financial Proposal.pdf', type: 'PDF' },
        { name: 'Company Profile.pdf', type: 'PDF' }
      ],
      notes: 'Additional notes about the bid submission and any special considerations.'
    });
    setLoading(false);
  }, [id]);

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
        <Typography>Loading...</Typography>
      </Container>
    );
  }

  if (!bid) {
    return (
      <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
        <Alert severity="error">Bid not found</Alert>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
          <Typography variant="h4" component="h1">
            Bid Details
          </Typography>
          <Chip 
            label={bid.status} 
            color={
              bid.status === 'Submitted' ? 'info' :
              bid.status === 'Under Review' ? 'warning' :
              bid.status === 'Accepted' ? 'success' :
              bid.status === 'Rejected' ? 'error' : 'default'
            }
          />
        </Box>

        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Typography variant="h6" gutterBottom>
              {bid.tenderTitle}
            </Typography>
          </Grid>

          <Grid item xs={12} sm={6}>
            <Typography variant="subtitle1" color="textSecondary">
              Amount
            </Typography>
            <Typography variant="body1">
              {bid.amount}
            </Typography>
          </Grid>

          <Grid item xs={12} sm={6}>
            <Typography variant="subtitle1" color="textSecondary">
              Submission Date
            </Typography>
            <Typography variant="body1">
              {bid.submissionDate}
            </Typography>
          </Grid>

          <Grid item xs={12}>
            <Typography variant="subtitle1" color="textSecondary">
              Description
            </Typography>
            <Typography variant="body1" paragraph>
              {bid.description}
            </Typography>
          </Grid>

          <Grid item xs={12}>
            <Divider sx={{ my: 2 }} />
            <Typography variant="h6" gutterBottom>
              Documents
            </Typography>
            <List>
              {bid.documents.map((doc, index) => (
                <ListItem key={index}>
                  <ListItemText
                    primary={doc.name}
                    secondary={doc.type}
                  />
                </ListItem>
              ))}
            </List>
          </Grid>

          {bid.notes && (
            <Grid item xs={12}>
              <Divider sx={{ my: 2 }} />
              <Typography variant="h6" gutterBottom>
                Notes
              </Typography>
              <Typography variant="body1">
                {bid.notes}
              </Typography>
            </Grid>
          )}

          <Grid item xs={12}>
            <Box display="flex" justifyContent="flex-end" gap={2}>
              <Button
                variant="outlined"
                onClick={() => navigate('/bids')}
              >
                Back to Bids
              </Button>
              <Button
                variant="contained"
                color="primary"
                onClick={() => navigate(`/bids/${id}/edit`)}
              >
                Edit Bid
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
};

export default BidDetail;

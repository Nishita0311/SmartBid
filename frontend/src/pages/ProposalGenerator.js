import React, { useState } from 'react';
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  Box
} from '@mui/material';

const ProposalGenerator = () => {
  const [formData, setFormData] = useState({
    tenderDetails: '',
    companyStrengths: '',
    previousExperience: '',
    proposedSolution: '',
    budget: '',
    timeline: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission
    console.log('Form submitted:', formData);
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Proposal Generator
        </Typography>
        <Paper sx={{ p: 3 }}>
          <form onSubmit={handleSubmit}>
            <TextField
              fullWidth
              label="Tender Details"
              name="tenderDetails"
              multiline
              rows={4}
              value={formData.tenderDetails}
              onChange={handleChange}
              margin="normal"
            />
            <TextField
              fullWidth
              label="Company Strengths"
              name="companyStrengths"
              multiline
              rows={4}
              value={formData.companyStrengths}
              onChange={handleChange}
              margin="normal"
            />
            <TextField
              fullWidth
              label="Previous Experience"
              name="previousExperience"
              multiline
              rows={4}
              value={formData.previousExperience}
              onChange={handleChange}
              margin="normal"
            />
            <TextField
              fullWidth
              label="Proposed Solution"
              name="proposedSolution"
              multiline
              rows={4}
              value={formData.proposedSolution}
              onChange={handleChange}
              margin="normal"
            />
            <TextField
              fullWidth
              label="Budget"
              name="budget"
              value={formData.budget}
              onChange={handleChange}
              margin="normal"
            />
            <TextField
              fullWidth
              label="Timeline"
              name="timeline"
              value={formData.timeline}
              onChange={handleChange}
              margin="normal"
            />
            <Button
              type="submit"
              variant="contained"
              color="primary"
              sx={{ mt: 2 }}
            >
              Generate Proposal
            </Button>
          </form>
        </Paper>
      </Box>
    </Container>
  );
};

export default ProposalGenerator; 
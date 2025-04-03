import React, { useEffect } from 'react';
import { useNavigate, Link as RouterLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Link,
  Alert,
  Paper,
  FormControlLabel,
  Checkbox,
  Grid,
} from '@mui/material';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { register, clearError } from '../../store/slices/authSlice';

const validationSchema = yup.object({
  email: yup.string().email('Invalid email').required('Email is required'),
  password: yup
    .string()
    .min(8, 'Password must be at least 8 characters')
    .required('Password is required'),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref('password'), null], 'Passwords must match')
    .required('Confirm password is required'),
  full_name: yup.string().required('Full name is required'),
  is_company: yup.boolean(),
  company_name: yup.string().when('is_company', {
    is: true,
    then: yup.string().required('Company name is required'),
  }),
  company_description: yup.string().when('is_company', {
    is: true,
    then: yup.string().required('Company description is required'),
  }),
  industry: yup.string().when('is_company', {
    is: true,
    then: yup.string().required('Industry is required'),
  }),
});

const Register = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { isAuthenticated, loading, error } = useSelector((state) => state.auth);

  useEffect(() => {
    if (isAuthenticated) {
      navigate('/');
    }
    return () => {
      dispatch(clearError());
    };
  }, [isAuthenticated, navigate, dispatch]);

  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
      confirmPassword: '',
      full_name: '',
      is_company: false,
      company_name: '',
      company_description: '',
      industry: '',
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      const { confirmPassword, ...submitValues } = values;
      dispatch(register(submitValues));
    },
  });

  return (
    <Container component="main" maxWidth="sm">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper
          elevation={3}
          sx={{
            padding: 4,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            width: '100%',
          }}
        >
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          {error && (
            <Alert severity="error" sx={{ mt: 2, width: '100%' }}>
              {error.detail || 'Registration failed'}
            </Alert>
          )}
          <Box
            component="form"
            onSubmit={formik.handleSubmit}
            sx={{ mt: 3, width: '100%' }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                  value={formik.values.email}
                  onChange={formik.handleChange}
                  error={formik.touched.email && Boolean(formik.errors.email)}
                  helperText={formik.touched.email && formik.errors.email}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="full_name"
                  label="Full Name"
                  id="full_name"
                  value={formik.values.full_name}
                  onChange={formik.handleChange}
                  error={formik.touched.full_name && Boolean(formik.errors.full_name)}
                  helperText={formik.touched.full_name && formik.errors.full_name}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  value={formik.values.password}
                  onChange={formik.handleChange}
                  error={formik.touched.password && Boolean(formik.errors.password)}
                  helperText={formik.touched.password && formik.errors.password}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="confirmPassword"
                  label="Confirm Password"
                  type="password"
                  id="confirmPassword"
                  value={formik.values.confirmPassword}
                  onChange={formik.handleChange}
                  error={formik.touched.confirmPassword && Boolean(formik.errors.confirmPassword)}
                  helperText={formik.touched.confirmPassword && formik.errors.confirmPassword}
                />
              </Grid>
              <Grid item xs={12}>
                <FormControlLabel
                  control={
                    <Checkbox
                      name="is_company"
                      checked={formik.values.is_company}
                      onChange={formik.handleChange}
                      color="primary"
                    />
                  }
                  label="Register as a company"
                />
              </Grid>
              {formik.values.is_company && (
                <>
                  <Grid item xs={12}>
                    <TextField
                      required
                      fullWidth
                      name="company_name"
                      label="Company Name"
                      id="company_name"
                      value={formik.values.company_name}
                      onChange={formik.handleChange}
                      error={formik.touched.company_name && Boolean(formik.errors.company_name)}
                      helperText={formik.touched.company_name && formik.errors.company_name}
                    />
                  </Grid>
                  <Grid item xs={12}>
                    <TextField
                      required
                      fullWidth
                      name="company_description"
                      label="Company Description"
                      id="company_description"
                      multiline
                      rows={4}
                      value={formik.values.company_description}
                      onChange={formik.handleChange}
                      error={formik.touched.company_description && Boolean(formik.errors.company_description)}
                      helperText={formik.touched.company_description && formik.errors.company_description}
                    />
                  </Grid>
                  <Grid item xs={12}>
                    <TextField
                      required
                      fullWidth
                      name="industry"
                      label="Industry"
                      id="industry"
                      value={formik.values.industry}
                      onChange={formik.handleChange}
                      error={formik.touched.industry && Boolean(formik.errors.industry)}
                      helperText={formik.touched.industry && formik.errors.industry}
                    />
                  </Grid>
                </>
              )}
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              disabled={loading}
            >
              {loading ? 'Signing up...' : 'Sign Up'}
            </Button>
            <Box sx={{ textAlign: 'center' }}>
              <Link component={RouterLink} to="/login" variant="body2">
                Already have an account? Sign in
              </Link>
            </Box>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Register; 
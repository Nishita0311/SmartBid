import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  bids: [],
  loading: false,
  error: null,
};

const bidSlice = createSlice({
  name: 'bids',
  initialState,
  reducers: {
    setBids: (state, action) => {
      state.bids = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
  },
});

export const { setBids, setLoading, setError } = bidSlice.actions;
export default bidSlice.reducer; 
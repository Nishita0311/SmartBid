import { createSlice } from '@reduxjs/toolkit';
import { 
  auth, 
  createUserWithEmailAndPassword, 
  signInWithEmailAndPassword, 
  signOut, 
  onAuthStateChanged 
} from '../../config/firebase';

const initialState = {
  user: null,
  isAuthenticated: false,
  loading: false,
  error: null
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload;
      state.isAuthenticated = !!action.payload;
      state.loading = false;
      state.error = null;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
      state.loading = false;
    },
    logout: (state) => {
      state.user = null;
      state.isAuthenticated = false;
      state.loading = false;
      state.error = null;
    }
  }
});

export const { setUser, setLoading, setError, logout } = authSlice.actions;

// Thunks
export const login = (email, password) => async (dispatch) => {
  try {
    dispatch(setLoading(true));
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    dispatch(setUser(userCredential.user));
  } catch (error) {
    dispatch(setError(error.message));
  }
};

export const register = (email, password, fullName) => async (dispatch) => {
  try {
    dispatch(setLoading(true));
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    await userCredential.user.updateProfile({
      displayName: fullName
    });
    dispatch(setUser(userCredential.user));
  } catch (error) {
    dispatch(setError(error.message));
  }
};

export const checkAuthState = () => (dispatch) => {
  onAuthStateChanged(auth, (user) => {
    if (user) {
      dispatch(setUser(user));
    } else {
      dispatch(logout());
    }
  });
};

export default authSlice.reducer; 
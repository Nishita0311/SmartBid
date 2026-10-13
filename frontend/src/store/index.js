import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import bidReducer from './slices/bidSlice';
import notificationReducer from './slices/notificationSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    bids: bidReducer,
    notifications: notificationReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
}); 
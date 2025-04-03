import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import tenderReducer from './slices/tenderSlice';
import companyReducer from './slices/companySlice';
import bidReducer from './slices/bidSlice';
import notificationReducer from './slices/notificationSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    tender: tenderReducer,
    company: companyReducer,
    bid: bidReducer,
    notification: notificationReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
}); 
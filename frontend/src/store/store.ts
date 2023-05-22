import { configureStore } from '@reduxjs/toolkit';
import { createWrapper } from 'next-redux-wrapper';
import { authSlice } from './slices/authSlice';
import { errorsSlice } from './slices/errorSlice';
import { successMessageSlice } from './slices/successMessage';
import { createTopicSlice } from './slices/createTopicSlice';
import { eventSlice } from './slices/eventSlice';

const makeStore = () =>
    configureStore({
        reducer: {
            [authSlice.name]: authSlice.reducer,
            [errorsSlice.name]: errorsSlice.reducer,
            [successMessageSlice.name]: successMessageSlice.reducer,
            [createTopicSlice.name]: createTopicSlice.reducer,
            [eventSlice.name]: eventSlice.reducer,
        },
        devTools: true,
    });

export const wrapper = createWrapper(makeStore);

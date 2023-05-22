import { createSlice } from '@reduxjs/toolkit';
import { HYDRATE } from 'next-redux-wrapper';

const initialState = {
    errors: null,
};

export const errorsSlice = createSlice({
    name: 'errors',
    initialState,
    reducers: {
        setErrors: (state, action) => {
            state.errors = action.payload;
        },

        clearErrors: (state, action) => {
            state.errors = action.payload;
        },

        // Special reducer for hydrating the state
        // extraReducers: {
        //     [HYDRATE]: (state, action) => {
        //         return {
        //             ...state,
        //             ...action.payload.errors,
        //         };
        //     },
        // },
    },
});

export const { setErrors, clearErrors } = errorsSlice.actions;
export const selectError = state => state.errors.errors;
export default errorsSlice.reducer;

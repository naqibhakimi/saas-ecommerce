import { createSlice } from '@reduxjs/toolkit';
import { HYDRATE } from 'next-redux-wrapper';

const initialState = {
    message: '',
};

export const successMessageSlice = createSlice({
    name: 'successMessage',
    initialState,
    reducers: {
        setSuccessMessage: (state, action) => {
            state.message = action.payload;
        },

        clearSuccessMessage: (state, action) => {
            state.message = action.payload;
        },

        // Special reducer for hydrating the state
        // extraReducers: {
        //     [HYDRATE]: (state, action) => {
        //         return {
        //             ...state,
        //             ...action.payload.message,
        //         };
        //     },
        // },
    },
});

export const { setSuccessMessage, clearSuccessMessage } =
    successMessageSlice.actions;
export const selectSuccessMessage = state => state.successMessage.message;
export default successMessageSlice.reducer;

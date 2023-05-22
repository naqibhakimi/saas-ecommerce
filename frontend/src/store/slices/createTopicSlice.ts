import { createSlice } from '@reduxjs/toolkit';
import { HYDRATE } from 'next-redux-wrapper';

const initialState = {
    open: false,
};

export const createTopicSlice = createSlice({
    name: 'createTopicModal',
    initialState,
    reducers: {
        // Action to open the modal
        openModal: (state, action) => {
            state.open = action.payload;
        },

        closeModal: (state, action) => {
            state.open = action.payload;
        },

        // Special reducer for hydrating the state
        // extraReducers: {
        //     [HYDRATE]: (state, action) => {
        //         return {
        //             ...state,
        //             ...action.payload.createTopicModal,
        //         };
        //     },
        // },
    },
});

export const { openModal, closeModal } = createTopicSlice.actions;
export const selectModalState = state => state.createTopicModal.open;
export default createTopicSlice.reducer;

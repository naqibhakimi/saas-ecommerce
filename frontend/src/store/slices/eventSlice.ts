import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    event_id: null,
    event_type: null,
    data: undefined,
};

export const eventSlice = createSlice({
    name: 'event',
    initialState,
    reducers: {
        setEvent: (state, action) => {
            state.event_id = action.payload.event_id;
            state.event_type = action.payload.event_type;
            state.data = action.payload.data;
        },

        clearEvent: (state, action) => {
            state = action.payload;
        },
    },
});

export const { setEvent, clearEvent } = eventSlice.actions;
export const selectEvent = state => state.event;
export default eventSlice.reducer;

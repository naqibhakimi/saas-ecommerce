import { createSlice } from '@reduxjs/toolkit';
import { HYDRATE } from 'next-redux-wrapper';

const initialState = {
    authState: false,
    authUser: null,
};

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setAuthState(state, action) {
            state.authState = action.payload;
        },
        setAuthUser(state, action) {
            state.authUser = action.payload;
        },

        // extraReducers: {
        //   [HYDRATE]: (st: anyate, act: { payload: { auth: any; }; }ion) => {
        //     return {
        //       ...state,
        //       ...action.payload.auth,
        //     };
        //   },
        // },
    },
});

export const { setAuthState, setAuthUser } = authSlice.actions;
export const selectAuthState = (state: { auth: { authState: any } }) =>
    state.auth.authState;
export const selectAuthUser = (state: { auth: { authUser: any } }) =>
    state.auth.authUser;
export default authSlice.reducer;

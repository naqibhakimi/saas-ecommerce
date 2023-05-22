import { VERIFY_ACCOUNT } from '@/services/auth';
import { useMutation } from '@apollo/client';
import React, { useCallback, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { useRouter } from 'next/router';
import { setErrors } from '@/store/slices/errorSlice';
import {
    clearSuccessMessage,
    setSuccessMessage,
} from '@/store/slices/successMessage';
import { useDispatch } from 'react-redux';

import Link from 'next/link';
import Image from 'next/image';

import { ACTIVATION_WELLCOME_MESSAGE } from '@/constents';

const Activate = () => {
    const dispatch = useDispatch();
    const router = useRouter();
    const { secret } = router.query;

    const [ActivateAccount, { data, loading, error }] = useMutation(
        VERIFY_ACCOUNT,
        {
            onError(error) {
                dispatch(setErrors([{ message: error.message }]));
                dispatch(clearSuccessMessage(null));
            },
        },
    );

    if (loading) {
        dispatch(setSuccessMessage('Loading...'));
    }

    if (data?.verifyAccount?.errors) {
        dispatch(setErrors(data.verifyAccount.errors.nonFieldErrors));
    }

    if (data?.verifyAccount?.success) {
        dispatch(setSuccessMessage(ACTIVATION_WELLCOME_MESSAGE));
        localStorage.setItem('auth', JSON.stringify(data.verifyAccount));
        router.push('/');
    }

    useEffect(() => {
        ActivateAccount({ variables: { input: { token: secret } } });
        localStorage.removeItem('auth');
        router.prefetch('/');
    }, [secret]);

    return <></>;
};

export default Activate;

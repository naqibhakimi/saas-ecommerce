import { RESEND_ACTIVATION_EMIAL } from '@/services/auth';
import { useMutation } from '@apollo/client';
import React, { useCallback, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { NextRouter, useRouter } from 'next/router';
import { setErrors } from '@/store/slices/errorSlice';
import {
    clearSuccessMessage,
    setSuccessMessage,
} from '@/store/slices/successMessage';
import { useDispatch } from 'react-redux';

import Link from 'next/link';
import Image from 'next/image';

import { LOGIN_WELLCOME_MESSAGE } from '@/constents';

const VerifyEmail = () => {
    const dispatch = useDispatch();
    const router: NextRouter = useRouter();

    const [resentActivationEmail, { data, loading, error }] = useMutation(
        RESEND_ACTIVATION_EMIAL,
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

    if (data?.resendActivationEmail?.errors) {
        dispatch(setErrors(data.resendActivationEmail.errors.nonFieldErrors));
    }

    if (data?.resendActivationEmail.success) {
        dispatch(setSuccessMessage('Resent the activate email!'));
    }

    const onSubmit = useCallback(() => {
        resentActivationEmail({
            variables: { input: { email: localStorage.getItem('email') } },
        });
    }, []);

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-lg w-full space-y-8">
                <div className="py-24 sm:py-32 lg:py-40">
                    <div className="mx-auto max-w-10xl px-6 lg:px-8">
                        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                        <Link href="/">
                        <Image
                            alt="Your Company"
                            className="mx-auto h-10 w-auto"
                            src="/Skryb-Light.svg"
                            width={120}
                            height={50}
                        />
                    </Link>
                            <h2 className="mt-5 mb-4 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                                Please verify your email
                            </h2>
                        </div>
                        <button
                            className=" mx-auto w-full py-2 flex justify-center px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
                            onClick={onSubmit}
                        >
                            Resend Email
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default VerifyEmail;

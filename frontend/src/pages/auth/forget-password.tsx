import { SENT_PASSWORD_RESET_EMAIL } from '@/services/auth';
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

import { RESET_PASSWORD_EMAIL_SENT } from '@/constents';

const ForgetPassword = () => {
    const dispatch = useDispatch();
    const {
        register,
        handleSubmit,
        formState: { errors, isValid },
    } = useForm({ mode: 'onBlur' });
    const router: NextRouter = useRouter();

    useEffect(() => {
        localStorage.removeItem('auth');
        router.prefetch('/');
    }, [router]);

    const [sentPasswordResetEmail, { data, loading, error }] = useMutation(
        SENT_PASSWORD_RESET_EMAIL,
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

    if (data?.sendPasswordResetEmail?.errors) {
        dispatch(setErrors(data.sendPasswordResetEmail.errors.nonFieldErrors));
    }

    if (data?.sendPasswordResetEmail.success) {
        dispatch(setSuccessMessage(RESET_PASSWORD_EMAIL_SENT));
        localStorage.removeItem('auth');
    }

    const onSubmit = useCallback(data => {
        sentPasswordResetEmail({ variables: { input: data } });
    }, []);

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-md w-full space-y-8">
                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <Link href="/">
                        <Image
                            alt="Your Company"
                            className="mx-auto h-10 w-auto"
                            src="/SassEcommerce-Light.svg"
                            width={120}
                            height={50}
                        />
                    </Link>
                    <h2 className="mt-3 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                        Reset password
                    </h2>
                    <p className="text-center text-sm  tracking-tight text-gray-600">
                        Please enter your email address to reset your password
                    </p>
                </div>
                <form
                    className="mt-8 space-y-6"
                    noValidate
                    onSubmit={handleSubmit(onSubmit)}
                >
                    <input name="remember" type="hidden" value="true" />
                    <div className="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label className="sr-only" htmlFor="email-address">
                                Email address
                            </label>
                            <input
                                {...register('email', {
                                    required: true,
                                    maxLength: 20,
                                    pattern:
                                        /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/,
                                })}
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900  focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                                id="email-address"
                                name="email"
                                placeholder="Email address"
                                type="email"
                            />

                            {errors.email?.type === 'required' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    Email address required!
                                </p>
                            )}
                            {errors.email?.type === 'pattern' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    Email is not valid!
                                </p>
                            )}
                        </div>
                    </div>
                    <div>
                        <button
                            className="disabled:bg-gray-500 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:text-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:bg-gray-500"
                            disabled={!isValid}
                            type="submit"
                        >
                            <span className="absolute left-0 inset-y-0 flex items-center pl-3"></span>
                            Reset
                        </button>
                    </div>
                </form>
                <div className="flex items-center justify-center">
                    <div className="text-sm pr-2">Already have a account?</div>
                    <div className="text-sm">
                        <Link
                            className="font-medium text-blue-600 hover:text-blue-500"
                            href={'/auth/login'}
                        >
                            Login
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ForgetPassword;

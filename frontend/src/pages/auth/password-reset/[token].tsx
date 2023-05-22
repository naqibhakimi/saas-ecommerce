import { PASSWORD_RESET } from '@/services/auth';
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


const SetPassword = () => {
    const dispatch = useDispatch();
    const router = useRouter();
    const { token } = router.query;

    const {
        register,
        handleSubmit,
        watch,
        formState: { errors, isValid },
    } = useForm({ mode: 'onBlur' });

    useEffect(() => {
        localStorage.removeItem('auth');
        router.prefetch('/');
    }, [router]);

    const [passwordReset, { data, loading, error }] = useMutation(
        PASSWORD_RESET,
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

    if (data?.passwordReset?.errors) {
        dispatch(clearSuccessMessage(null));
        dispatch(setErrors(data.passwordReset.errors.nonFieldErrors));
    }

    if (data?.passwordReset?.errors?.newPassword2) {
        dispatch(clearSuccessMessage(null));
        dispatch(
            setErrors([
                {
                    code: '',
                    message: data.passwordReset.errors.newPassword2[0],
                },
            ]),
        );
    }

    if (data?.passwordReset.success) {
        router.push('/auth/login');
    }

    const onSubmit = useCallback(data => {
        passwordReset({ variables: { input: { ...data, token } } });
    }, []);

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
            <div className="max-w-md w-full space-y-8">
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
                    <h2 className="mt-3 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                        New Password!
                    </h2>
                    <p className="text-center text-sm  tracking-tight text-gray-600">
                        Please enter your new password
                    </p>
                </div>
                <form
                    className="mt-8 space-y-6"
                    noValidate
                    onSubmit={handleSubmit(onSubmit)}
                >
                    <div className="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label className="sr-only" htmlFor="newPassword1">
                                Password
                            </label>
                            <input
                                {...register('newPassword1', {
                                    required: true,
                                    minLength: 8,
                                })}
                                autoComplete="false"
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                                id="newPassword1"
                                name="newPassword1"
                                placeholder="Password"
                                required
                                type="password"
                            />
                        </div>
                        <div>
                            <label className="sr-only" htmlFor="newPassword2">
                                Password
                            </label>
                            <input
                                {...register('newPassword2', {
                                    required: true,
                                    minLength: 8,
                                    validate: (val: string) => {
                                        if (watch('newPassword1') != val) {
                                            return 'Your passwords do no match';
                                        }
                                    },
                                })}
                                autoComplete="false"
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                                id="newPassword2"
                                name="newPassword2"
                                placeholder="Confirm password"
                                required
                                type="password"
                            />
                            {errors.newPassword1?.type === 'required' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    Password required !
                                </p>
                            )}
                            {errors.newPassword1?.type === 'minLength' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    The password should not be less then 8
                                    charecters
                                </p>
                            )}

                            {errors.newPassword2?.type === 'required' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    Confirm password required !
                                </p>
                            )}

                            <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                {errors.newPassword2?.message}
                            </p>
                        </div>
                    </div>

                    <div>
                        <button
                            className="disabled:bg-gray-500 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:text-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:bg-gray-500"
                            disabled={!isValid}
                            type="submit"
                        >
                            <span className="absolute left-0 inset-y-0 flex items-center pl-3"></span>
                            Reset Password
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default SetPassword;

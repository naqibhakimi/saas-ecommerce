import { SIGNIN } from '@/services/auth';
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

const Login = () => {
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

    const [signIn, { data, loading, error }] = useMutation(SIGNIN, {
        onError(error) {
            dispatch(setErrors([{ message: error.message }]));
            dispatch(clearSuccessMessage(null));
        },
    });

    if (loading) {
        dispatch(setSuccessMessage('Loading...'));
    }

    if (data?.signin?.errors) {
        dispatch(setErrors(data.signin.errors.nonFieldErrors));
    }

    if (data?.signin.success) {
        dispatch(setSuccessMessage(LOGIN_WELLCOME_MESSAGE));
        localStorage.setItem('auth', JSON.stringify(data.signin));
        router.push('/');
    }

    const onSubmit = useCallback(data => {
        signIn({ variables: { input: data } });
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
                    <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                        Sign in to your account
                    </h2>
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
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                                id="email-address"
                                name="email"
                                placeholder="Email address"
                                type="email"
                            />
                        </div>
                        <div>
                            <label className="sr-only" htmlFor="password">
                                Password
                            </label>
                            <input
                                {...register('password', {
                                    required: true,
                                    minLength: 8,
                                })}
                                autoComplete="false"
                                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
                                id="password"
                                name="password"
                                placeholder="Password"
                                required
                                type="password"
                            />
                            {errors.password?.type === 'required' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    Password required !
                                </p>
                            )}
                            {errors.password?.type === 'minLength' && (
                                <p className="mt-1 mb-2 text-sm text-red-600 dark:text-red-500">
                                    {' '}
                                    The password should not be less then 8
                                    charecters
                                </p>
                            )}

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

                    <div className="flex items-center justify-between">
                        <div className="flex items-center">
                            <input
                                className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                                id="remember_me"
                                name="remember_me"
                                type="checkbox"
                            />
                            <label
                                className="ml-2 block text-sm text-gray-900"
                                htmlFor="remember_me"
                            >
                                Remember me
                            </label>
                        </div>

                        <div className="text-sm">
                            <Link
                                className="font-medium text-blue-600 hover:text-blue-500"
                                href={'/auth/forget-password'}
                            >
                                Forgot your password?
                            </Link>
                        </div>
                    </div>

                    <div>
                        <button
                            className="disabled:bg-gray-500 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-900 hover:text-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:bg-gray-500"
                            disabled={!isValid}
                            type="submit"
                        >
                            <span className="absolute left-0 inset-y-0 flex items-center pl-3"></span>
                            Sign in
                        </button>
                    </div>
                </form>
                <div className="flex items-center justify-center">
                    <div className="text-sm pr-2">Dont have a account?</div>
                    <div className="text-sm">
                        <Link
                            className="font-medium text-blue-600 hover:text-blue-500"
                            href={'/auth/signup'}
                        >
                            Sign Up
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;

import { useForm, Controller } from 'react-hook-form';
import {
    _Update_PRODUCT,
    _GET_PRODUCTS,
    _GET_PRODUCT_ID,
} from '@/services/products';
import { _GET_COUNTRIES } from '@/services/customers';
import { useLazyQuery, useMutation, useQuery } from '@apollo/client';
import { useRouter } from 'next/router';
import Layout from '@/components/layout/Layout';
import { convertEdgeToList } from '@/utils/helpers';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

import * as React from 'react';
import Autocomplete from '@mui/joy/Autocomplete';
import AutocompleteOption from '@mui/joy/AutocompleteOption';
import ListItemDecorator from '@mui/joy/ListItemDecorator';
import ListItemContent from '@mui/joy/ListItemContent';
import Typography from '@mui/joy/Typography';
import Select from '@mui/joy/Select';
import Option from '@mui/joy/Option';

import { TextareaAutosize } from '@mui/base/TextareaAutosize';
import { useDispatch } from 'react-redux';
import { setErrors } from '@/store/slices/errorSlice';
import {
    clearSuccessMessage,
    setSuccessMessage,
} from '@/store/slices/successMessage';

export default function Variant() {
    const {
        handleSubmit,
        control,
        formState: { errors },
    } = useForm();

    const router = useRouter();
    const { productId } = router.query;

    const { loading, error, data } = useQuery(_GET_PRODUCT_ID, {
        variables: { id: productId },
    });

    const countriesQuery = useQuery(_GET_COUNTRIES);

    return (
        <>
            <form>
                <div>
                    <div className="mt-10 space-y-8 border-b border-gray-900/10 pb-12 sm:space-y-0 sm:divide-y sm:divide-gray-900/10 sm:pb-0">
                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="country"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Variation theme
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <select
                                    id="country"
                                    name="country"
                                    autoComplete="country-name"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>Color Name</option>
                                    <option>Size Name</option>
                                    <option>Size Name Color Name</option>
                                </select>
                                {/* <Controller
                                    name="country"
                                    control={control}
                                    defaultValue={data.product.isExpirable}
                                    render={({ field }) => (
                                        <Select
                                            defaultValue={
                                                data.product.isExpirable
                                            }
                                        >
                                            <Option value={true}>False</Option>
                                            <Option value={false}>True</Option>
                                        </Select>
                                    )}
                                />
                                {errors.isExpirable && (
                                    <p className="text-red-500 text-sm mt-1">
                                        isExpirable is required
                                    </p>
                                )} */}
                            </div>
                        </div>
                    </div>
                </div>
                <div className="mt-6 flex items-center justify-end gap-x-6">
                    <button
                        type="button"
                        className="text-sm font-semibold leading-6 text-gray-900"
                    >
                        Cancel
                    </button>
                    <button
                        type="submit"
                        className="inline-flex justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                    >
                        Save
                    </button>
                </div>
            </form>
        </>
    );
}

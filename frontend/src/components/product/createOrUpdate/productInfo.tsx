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

export default function ProductInfo() {
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

    const dispatch = useDispatch();
    const [
        updateProduct,
        { data: productData, loading: productLoading, error: productError },
    ] = useMutation(_Update_PRODUCT, {
        onError(error) {
            dispatch(setErrors([{ message: error.message }]));
            dispatch(clearSuccessMessage(null));
        },
    });

    if (productLoading) {
        dispatch(setSuccessMessage('Loading...'));
    }

    if (productData?.updateProduct?.errors) {
        dispatch(setErrors(data.updateProduct.errors.nonFieldErrors));
    }

    if (productData?.updateProduct.success) {
        // dispatch(setSuccessMessage(LOGIN_WELLCOME_MESSAGE));
        // localStorage.setItem('auth', JSON.stringify(productData.updateProduct));
        // router.push('/');
    }

    const onSubmit = React.useCallback(
        data => {
            console.log(data);
            updateProduct({
                variables: { input: { Product: { id: productId, ...data } } },
            });
        },
        [productId],
    );

    if (loading || error) {
        return (
            <></>

            // <Layout>
            //     <></>
            // </Layout>
        );
    }

    return (
        <>
            <form onSubmit={handleSubmit(onSubmit)}>
                <div>
                    <div className="mt-10 space-y-8 border-b border-gray-900/10 pb-12 sm:space-y-0 sm:divide-y sm:divide-gray-900/10 sm:pb-0">
                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="title"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Title
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="title"
                                    control={control}
                                    defaultValue={data.product.title}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="title-basic"
                                            label="Title"
                                            variant="standard"
                                            {...field}
                                        />
                                    )}
                                />
                                {errors.title && (
                                    <p className="text-red-500 text-sm mt-1">
                                        Title is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="subtitle"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Subtitle
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="subtitle"
                                    control={control}
                                    defaultValue={data.product.subtitle}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="subtitle-basic"
                                            label="Subtitle"
                                            variant="standard"
                                            {...field}
                                        />
                                    )}
                                />
                                {errors.subtitle && (
                                    <p className="text-red-500 text-sm mt-1">
                                        Sub Title is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="about"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Description
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="description"
                                    control={control}
                                    defaultValue={data.product.description}
                                    render={({ field }) => (
                                        <TextareaAutosize
                                            className="w-full"
                                            {...field}
                                            minRows={2}
                                        />
                                    )}
                                />
                                {errors.description && (
                                    <p className="text-red-500 text-sm mt-1">
                                        description is required
                                    </p>
                                )}
                            </div>
                        </div>
                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="each-unit-count"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Each unit count
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="eachUnitCount"
                                    control={control}
                                    // defaultValue={data.product.eachUnitCount}
                                    defaultValue={parseInt(
                                        data.product.eachUnitCount,
                                        10,
                                    )}
                                    render={({ field }) => (
                                        <TextField
                                            {...field}
                                            className="w-full"
                                            id="each-unit-count"
                                            label="Each unit count"
                                            type="number"
                                            variant="standard"
                                            onChange={event => {
                                                const value = parseInt(
                                                    event.target.value,
                                                    10,
                                                );
                                                field.onChange(value);
                                            }}
                                        />
                                    )}
                                />
                                {errors.eachUnitCount && (
                                    <p className="text-red-500 text-sm mt-1">
                                        eachUnitCount is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="unit-count"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Unit count
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="unitCount"
                                    control={control}
                                    defaultValue={data.product.unitCount}
                                    render={({ field }) => (
                                        <TextField
                                            {...field}
                                            className="w-full"
                                            id="unitCount"
                                            label="Unit count"
                                            type="number"
                                            variant="standard"
                                            onChange={event => {
                                                const value = parseInt(
                                                    event.target.value,
                                                    10,
                                                );
                                                field.onChange(value);
                                            }}
                                        />
                                    )}
                                />
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="unit-count-type"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Unit count type
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="unitCountType"
                                    control={control}
                                    defaultValue={data.product.unitCountType}
                                    render={({ field }) => (
                                        <TextField
                                            {...field}
                                            className="w-full"
                                            id="unit-count-type"
                                            label="Unit count type"
                                            // type="number"
                                            variant="standard"
                                        />
                                    )}
                                />
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="material"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Material
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="material"
                                    control={control}
                                    defaultValue={data.product.material}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="material-basic"
                                            label="material"
                                            variant="standard"
                                            {...field}
                                        />
                                    )}
                                />
                                {errors.material && (
                                    <p className="text-red-500 text-sm mt-1">
                                        material is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="country"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Country/Region of Origin
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="originCountry"
                                    control={control}
                                    // defaultValue={data.product.originCountry.id}
                                    render={({ field }) => (
                                        <Autocomplete
                                            id="country-select-demo"
                                            value={data.product.originCountry}
                                            placeholder="Choose a country"
                                            slotProps={{
                                                input: {
                                                    autoComplete:
                                                        'new-password', // disable autocomplete and autofill
                                                },
                                            }}
                                            sx={{ width: 300 }}
                                            options={convertEdgeToList(
                                                countriesQuery?.data?.countries
                                                    .edges || [],
                                            )}
                                            autoHighlight
                                            getOptionLabel={option =>
                                                option.displayName
                                            }
                                            renderOption={(props, option) => (
                                                <AutocompleteOption {...props}>
                                                    {/* <ListItemDecorator>
                                                        <img
                                                            loading="lazy"
                                                            width="20"
                                                            src={`https://flagcdn.com/w20/${option.code.toLowerCase()}.png`}
                                                            srcSet={`https://flagcdn.com/w40/${option.code.toLowerCase()}.png 2x`}
                                                            alt=""
                                                        />
                                                    </ListItemDecorator> */}
                                                    <ListItemContent
                                                        className="w-full"
                                                        sx={{ fontSize: 'sm' }}
                                                    >
                                                        {option.displayName}
                                                        {/* <Typography level="body-xs">
                                                            ({option.iso3}) +
                                                            {option.numCode}
                                                            {option.displayName}
                                                        </Typography> */}
                                                    </ListItemContent>
                                                </AutocompleteOption>
                                            )}
                                        />
                                    )}
                                />
                                {errors.title && (
                                    <p className="text-red-500 text-sm mt-1">
                                        Country is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="isExpirable"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Is product Expirable?
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="isExpirable"
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
                                )}
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

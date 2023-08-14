import { useForm, Controller } from 'react-hook-form';
import { _GET_PRODUCTS, _GET_PRODUCT_ID } from '@/services/products';
import { _GET_COUNTRIES } from '@/services/customers';
import { useLazyQuery, useQuery } from '@apollo/client';
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

    const onSubmit = data => {
        console.log(data);
    };

    // const countryQuery = useQuery(_GET_COUNTRY);

    if (loading || error) {
        return (
            <Layout>
                <></>
            </Layout>
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
                                        <input
                                            type="text"
                                            {...field}
                                            autoComplete="subtitle"
                                            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xl sm:text-sm sm:leading-6"
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
                                <p className="mt-3 text-sm leading-6 text-gray-600">
                                    Write a few sentences about the product.
                                </p>
                            </div>
                        </div>
                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="street-address"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Each unit count
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="eachUnitCount"
                                    control={control}
                                    defaultValue={data.product.eachUnitCount}
                                    render={({ field }) => (
                                        <input
                                            type="text"
                                            // name="each-unit-count"
                                            {...field}
                                            id="each-unit-count"
                                            autoComplete="each-unit-count"
                                            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xl sm:text-sm sm:leading-6"
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
                                        <input
                                            type="text"
                                            name="unit-count"
                                            {...field}
                                            id="unit-count"
                                            autoComplete="unit-count"
                                            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xl sm:text-sm sm:leading-6"
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
                                        <input
                                            type="text"
                                            name="unit-count-type"
                                            {...field}
                                            id="unit-count-type"
                                            autoComplete="unit-count-type"
                                            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xl sm:text-sm sm:leading-6"
                                        />
                                    )}
                                />
                                {errors.unitCountType && (
                                    <p className="text-red-500 text-sm mt-1">
                                        unitCountType is required
                                    </p>
                                )}
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
                                        <input
                                            type="text"
                                            name="material"
                                            {...field}
                                            id="material"
                                            autoComplete="material"
                                            className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xl sm:text-sm sm:leading-6"
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
                                        Sub Title is required
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

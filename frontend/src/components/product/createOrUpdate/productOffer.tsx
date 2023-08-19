import TextField from '@mui/material/TextField';
import { useForm, Controller } from 'react-hook-form';
import { _GET_PRODUCTS, _GET_PRODUCT_ID } from '@/services/products';
// import { _GET_COUNTRIES } from '@/services/customers';
import { useQuery } from '@apollo/client';
import { useRouter } from 'next/router';
import Layout from '@/components/layout/Layout';
import { convertEdgeToList } from '@/utils/helpers';
import Button from '@mui/material/Button';
import Input from '@mui/material/Input';
import InputAdornment from '@mui/material/InputAdornment';

import * as React from 'react';
import Autocomplete from '@mui/joy/Autocomplete';
import AutocompleteOption from '@mui/joy/AutocompleteOption';
import ListItemDecorator from '@mui/joy/ListItemDecorator';
import ListItemContent from '@mui/joy/ListItemContent';
import Typography from '@mui/joy/Typography';
import Select from '@mui/joy/Select';
import Option from '@mui/joy/Option';

import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Chip from '@mui/material/Chip';
import MaterialSelect from '@mui/material/Select';

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
    PaperProps: {
        style: {
            maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
            width: 250,
        },
    },
};

const names = [
    'Oliver Hansen',
    'Van Henry',
    'April Tucker',
    'Ralph Hubbard',
    'Omar Alexander',
    'Carlos Abbott',
    'Miriam Wagner',
    'Bradley Wilkerson',
    'Virginia Andrews',
    'Kelly Snyder',
];

function getStyles(name, personName, theme) {
    return {
        fontWeight:
            personName.indexOf(name) === -1
                ? theme.typography.fontWeightRegular
                : theme.typography.fontWeightMedium,
    };
}
export default function productOffer() {
    const theme = useTheme();
    const [personName, setPersonName] = React.useState([]);

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

    const onSubmit = data => {
        console.log(data.product.price.amount);
    };

    console.log(data?.product?.price?.amount);
    if (loading || error) {
        return <></>;
    }

    const handleChange = event => {
        const {
            target: { value },
        } = event;
        setPersonName(
            // On autofill we get a stringified value.
            typeof value === 'string' ? value.split(',') : value,
        );
    };

    return (
        <>
            <form>
                <div>
                    <div className="mt-10 space-y-8 border-b border-gray-900/10 pb-12 sm:space-y-0 sm:divide-y sm:divide-gray-900/10 sm:pb-0">
                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="hs-code"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                HS code
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="HS-code"
                                    control={control}
                                    defaultValue={data.product.hsCode}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="hs-code"
                                            label="HS code"
                                            variant="standard"
                                            {...field}
                                        />
                                    )}
                                />
                                {errors.hsCode && (
                                    <p className="text-red-500 text-sm mt-1">
                                        HS code is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="mid-code"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Manufacturer code
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="mid-code"
                                    control={control}
                                    defaultValue={data.product.midCode}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="md-code"
                                            label="MD code"
                                            variant="standard"
                                            {...field}
                                        />
                                    )}
                                />
                                {errors.midCode && (
                                    <p className="text-red-500 text-sm mt-1">
                                        HS code is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="price"
                                className="block text-sm font-medium leading-6 text-gray-900"
                            >
                                Price
                            </label>
                            <div className="relative mt-2 rounded-md shadow-sm">
                                <Controller
                                    name="mid-code"
                                    control={control}
                                    defaultValue={data?.product?.price?.amount}
                                    render={({ field }) => (
                                        <Input
                                            {...field}
                                            id="product-price"
                                            className="w-full"
                                            startAdornment={
                                                <InputAdornment position="start">
                                                    $
                                                </InputAdornment>
                                            }
                                        />
                                    )}
                                />
                                {errors.midCode && (
                                    <p className="text-red-500 text-sm mt-1">
                                        HS code is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="condition"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Condition
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                {/* <select
                                    id="condition"
                                    name="condition"
                                    autoComplete="condition"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>New</option>
                                    <option>Used - Adaptable</option>
                                    <option>Used - Good </option>
                                    <option>Used - Like New </option>
                                    <option>Used - very Good </option>
                                </select> */}
                                <Controller
                                    name="isExpirable"
                                    control={control}
                                    defaultValue={data.product.isExpirable}
                                    render={({ field }) => (
                                        <Select
                                            {...field}
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

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="product-type"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Product Type
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                {/* <select
                                    id="product-type"
                                    name="product-type"
                                    autoComplete="product-type"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>Food and Beverages:</option>
                                    <option>Electronics</option>
                                    <option>Beauty and Personal Care </option>
                                    <option>Books and Media </option>
                                    <option>Toys and Games</option>
                                </select> */}
                                <Controller
                                    name="isExpirable"
                                    control={control}
                                    defaultValue={data.product.isExpirable}
                                    render={({ field }) => (
                                        // <Select
                                        //     defaultValue={
                                        //         data.product.isExpirable
                                        //     }
                                        // >
                                        //     <Option value={true}>False</Option>
                                        //     <Option value={false}>True</Option>
                                        //     <option>Select</option>
                                        //     <option>Food and Beverages:</option>
                                        //     <option>Electronics</option>
                                        //     <option>
                                        //         Beauty and Personal Care{' '}
                                        //     </option>
                                        //     <option>Books and Media </option>
                                        //     <option>Toys and Games</option>
                                        // </Select>
                                        <FormControl sx={{ m: 1, width: 300 }}>
                                            <InputLabel id="demo-multiple-chip-label">
                                                Chip
                                            </InputLabel>
                                            <MaterialSelect
                                                labelId="demo-multiple-chip-label"
                                                id="demo-multiple-chip"
                                                multiple
                                                value={personName}
                                                onChange={handleChange}
                                                input={
                                                    <OutlinedInput
                                                        id="select-multiple-chip"
                                                        label="Chip"
                                                    />
                                                }
                                                renderValue={selected => (
                                                    <Box
                                                        sx={{
                                                            display: 'flex',
                                                            flexWrap: 'wrap',
                                                            gap: 0.5,
                                                        }}
                                                    >
                                                        {selected.map(value => (
                                                            <Chip
                                                                key={value}
                                                                label={value}
                                                            />
                                                        ))}
                                                    </Box>
                                                )}
                                                MenuProps={MenuProps}
                                            >
                                                {names.map(name => (
                                                    <MenuItem
                                                        key={name}
                                                        value={name}
                                                        style={getStyles(
                                                            name,
                                                            personName,
                                                            theme,
                                                        )}
                                                    >
                                                        {name}
                                                    </MenuItem>
                                                ))}
                                            </MaterialSelect>
                                        </FormControl>
                                    )}
                                />
                                {errors.isExpirable && (
                                    <p className="text-red-500 text-sm mt-1">
                                        isExpirable is required
                                    </p>
                                )}
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="product-tag"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Product Tag
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <select
                                    id="product-tag"
                                    name="product-tag"
                                    autoComplete="product-tag"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>On Sale</option>
                                    <option>New Arrival</option>
                                    <option>Bestseller </option>
                                    <option>Limited Edition </option>
                                    <option>Seasonal</option>
                                    <option>Organic</option>
                                    <option>Handmade</option>
                                </select>
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="product-collections"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Product Collections
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <select
                                    id="product-collections"
                                    name="product-collections"
                                    autoComplete="product-collections"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>Summer Essentials</option>
                                    <option>Back-to-School Supplies</option>
                                    <option>Best-Selling Products </option>
                                    <option>New Arrivals </option>
                                    <option>Eco-Friendly Products</option>
                                    <option>Travel Accessories</option>
                                    <option>
                                        Tech Gadgets and Accessories
                                    </option>
                                </select>
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="is-gift-card"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Is Gift Card
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <select
                                    id="is-gift-card"
                                    name="is-gift-card"
                                    autoComplete="is-gift-card"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
                            </div>
                        </div>

                        <div className="sm:grid sm:grid-cols-3 sm:items-start sm:gap-4 sm:py-6">
                            <label
                                htmlFor="discountable"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                Discountable
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <select
                                    id="discountable"
                                    name="discountable"
                                    autoComplete="discountable"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                >
                                    <option>Select</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
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

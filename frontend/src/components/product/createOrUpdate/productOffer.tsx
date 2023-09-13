import TextField from '@mui/material/TextField';
import { useForm, Controller } from 'react-hook-form';
import {
    _GET_PRODUCTS,
    _GET_PRODUCT_ID,
    _Update_PRODUCT,
    _GET_PRODUCT_TYPES,
} from '@/services/products';
// import { _GET_COUNTRIES } from '@/services/customers';
import { useMutation, useQuery } from '@apollo/client';
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

import Grid from '@mui/material/Grid';
import { setErrors } from '@/store/slices/errorSlice';
import {
    clearSuccessMessage,
    setSuccessMessage,
} from '@/store/slices/successMessage';
import { useDispatch } from 'react-redux';

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
    const [productType, setProductType] = React.useState([]);
    const [productTag, setProductTag] = React.useState([]);
    const [productCollection, setProductCollection] = React.useState([]);

    const [currency, setCurrency] = React.useState('$'); // Default currency symbol
    const [amount, setAmount] = React.useState('');

    const handleCurrencyChange = event => {
        setCurrency(event.target.value);
    };
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

    const [condition, setCondition] = React.useState(
        data?.product?.condition || '',
    );

    const handleConditionChange = event => {
        setCondition(event.target.value);
    };

    const categories = useQuery(_GET_PRODUCT_TYPES);

    const handleTypeChange = event => {
        const {
            target: { value },
        } = event;
        setProductType(
            // On autofill we get a stringified value.
            typeof value === 'string' ? value.split(',') : value,
        );
    };

    const handleTagChange = event => {
        const {
            target: { value },
        } = event;
        setProductTag(typeof value === 'string' ? value.split(',') : value);
    };

    const handleCollectionChange = event => {
        const {
            target: { value },
        } = event;
        setProductCollection(
            typeof value === 'string' ? value.split(',') : value,
        );
    };

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
            // console.log(data);
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
                                htmlFor="hsCode"
                                className="block text-sm font-medium leading-6 text-gray-900 sm:pt-1.5"
                            >
                                HS code
                            </label>
                            <div className="mt-2 sm:col-span-2 sm:mt-0">
                                <Controller
                                    name="hsCode"
                                    control={control}
                                    defaultValue={data.product.hsCode}
                                    render={({ field }) => (
                                        <TextField
                                            className="w-full"
                                            id="hsCode"
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
                                    name="midCode"
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
                                    name="product-price"
                                    control={control}
                                    defaultValue={data?.product?.price?.amount}
                                    render={({ field }) => (
                                        <div>
                                            <Grid
                                                container
                                                spacing={2}
                                                alignItems="flex-end"
                                            >
                                                <Grid item xs={9}>
                                                    <FormControl
                                                        fullWidth
                                                        sx={{ m: 1 }}
                                                        variant="standard"
                                                    >
                                                        <InputLabel htmlFor="standard-adornment-amount">
                                                            Amount
                                                        </InputLabel>
                                                        <Input
                                                            id="standard-adornment-amount"
                                                            value={amount}
                                                            {...field}
                                                            onChange={e =>
                                                                setAmount(
                                                                    e.target
                                                                        .value,
                                                                )
                                                            }
                                                            startAdornment={
                                                                <InputAdornment position="start">
                                                                    {currency}
                                                                </InputAdornment>
                                                            }
                                                        />
                                                    </FormControl>
                                                </Grid>
                                                <Grid item xs={3}>
                                                    <FormControl sx={{ m: 1 }}>
                                                        <Select
                                                            value={currency}
                                                            onChange={
                                                                handleCurrencyChange
                                                            }
                                                            label="Currency"
                                                        >
                                                            <MenuItem value="$">
                                                                $ (USD)
                                                            </MenuItem>
                                                            <MenuItem value="€">
                                                                € (EUR)
                                                            </MenuItem>
                                                            <MenuItem value="£">
                                                                £ (GBP)
                                                            </MenuItem>
                                                        </Select>
                                                    </FormControl>
                                                </Grid>
                                            </Grid>
                                        </div>
                                    )}
                                />
                                {errors.amount && (
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
                                <Controller
                                    name="condition"
                                    control={control}
                                    defaultValue={data.product.condition}
                                    render={({ field }) => (
                                        <FormControl fullWidth>
                                            <InputLabel id="product-condition-label">
                                                Product Condition
                                            </InputLabel>
                                            <Select
                                                {...field}
                                                labelId="product-condition-label"
                                                id="product-condition"
                                                value={condition}
                                                label="Product Condition"
                                                onChange={handleConditionChange}
                                            >
                                                {data.product
                                                    .PRODUCT_CONDITION_CHOICES &&
                                                    data.product.PRODUCT_CONDITION_CHOICES.map(
                                                        choice => (
                                                            <MenuItem
                                                                key={choice[0]}
                                                                value={
                                                                    choice[0]
                                                                }
                                                            >
                                                                {choice[1]}
                                                            </MenuItem>
                                                        ),
                                                    )}
                                            </Select>
                                        </FormControl>

                                        // <Autocomplete
                                        //     id="product-condition-select-demo"
                                        //     value={data.product.condition} // Make sure to adjust this according to your data structure
                                        //     placeholder="Choose a product condition"
                                        //     slotProps={{
                                        //         input: {
                                        //             autoComplete:
                                        //                 'new-password', // disable autocomplete and autofill
                                        //         },
                                        //     }}
                                        //     sx={{ width: 300 }}
                                        //     options={
                                        //         data.product.condition
                                        //             .PRODUCT_CONDITION_CHOICES &&
                                        //         data.product.condition
                                        //             .PRODUCT_CONDITION_CHOICES
                                        //     }
                                        //     autoHighlight
                                        //     getOptionLabel={option => option}
                                        //     renderOption={(props, option) => (
                                        //         <AutocompleteOption {...props}>
                                        //             <ListItemContent
                                        //                 className="w-full"
                                        //                 sx={{ fontSize: 'sm' }}
                                        //             >
                                        //                 {option}
                                        //                 {/* <Typography level="body-xs">
                                        //                     ({option.iso3}) + {option.numCode}
                                        //                     {option.displayName}
                                        //                 </Typography> */}
                                        //             </ListItemContent>
                                        //         </AutocompleteOption>
                                        //     )}
                                        // />
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
                                <Controller
                                    name="productType"
                                    control={control}
                                    defaultValue={data.product.productType.id}
                                    render={({ field }) => (
                                        <Autocomplete
                                            id="product-type-select-demo"
                                            value={
                                                data.product.productType.value
                                            }
                                            placeholder="Choose a product type"
                                            slotProps={{
                                                input: {
                                                    autoComplete:
                                                        'new-password',
                                                },
                                            }}
                                            sx={{ width: 300 }}
                                            options={convertEdgeToList(
                                                categories?.data?.productTypes
                                                    .edges || [],
                                            )}
                                            autoHighlight
                                            getOptionLabel={option =>
                                                option.value
                                            }
                                            renderOption={(props, option) => (
                                                <AutocompleteOption {...props}>
                                                    <ListItemContent
                                                        className="w-full"
                                                        sx={{ fontSize: 'sm' }}
                                                    >
                                                        {option.value}
                                                    </ListItemContent>
                                                </AutocompleteOption>
                                            )}
                                        />
                                    )}
                                />

                                {errors.productType && (
                                    <p className="text-red-500 text-sm mt-1">
                                        productType is required
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
                                {/* <select
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
                                </select> */}
                                <Controller
                                    name="tags"
                                    control={control}
                                    defaultValue={data.product.tags}
                                    render={({ field }) => (
                                        <FormControl sx={{ m: 1, width: 300 }}>
                                            <InputLabel id="product-tag">
                                                Product Tag
                                            </InputLabel>{' '}
                                            <MaterialSelect
                                                labelId="product-tag"
                                                id="product-tag-id"
                                                multiple
                                                value={productTag}
                                                onChange={handleTagChange}
                                                input={
                                                    <OutlinedInput
                                                        id="select-multiple-chip"
                                                        label="Product Tag"
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
                                                            productTag,
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
                                {errors.tags && (
                                    <p className="text-red-500 text-sm mt-1">
                                        tags is required
                                    </p>
                                )}
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
                                {/* <select
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
                                </select> */}
                                <Controller
                                    name="collection"
                                    control={control}
                                    defaultValue={data.product.collection}
                                    render={({ field }) => (
                                        <FormControl sx={{ m: 1, width: 300 }}>
                                            <InputLabel id="product-collection">
                                                Product Collection
                                            </InputLabel>{' '}
                                            <MaterialSelect
                                                labelId="product-collection"
                                                id="product-collection-id"
                                                multiple
                                                value={productCollection}
                                                onChange={
                                                    handleCollectionChange
                                                }
                                                input={
                                                    <OutlinedInput
                                                        id="select-multiple-chip"
                                                        label="Product Collection"
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
                                                            productCollection,
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
                                {errors.collection && (
                                    <p className="text-red-500 text-sm mt-1">
                                        collection is required
                                    </p>
                                )}
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
                                <Controller
                                    name="isGiftCard"
                                    control={control}
                                    defaultValue={data.product.isGiftCard}
                                    render={({ field }) => (
                                        <Select
                                            defaultValue={
                                                data.product.isGiftCard
                                            }
                                        >
                                            <Option value={true}>False</Option>{' '}
                                            <Option value={false}>True</Option>{' '}
                                        </Select>
                                    )}
                                />
                                {errors.isGiftCard && (
                                    <p className="text-red-500 text-sm mt-1">
                                        isGiftCard is required{' '}
                                        {/* Changed the error message */}
                                    </p>
                                )}
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
                                <Controller
                                    name="discountable"
                                    control={control}
                                    defaultValue={data.product.discountable}
                                    render={({ field }) => (
                                        <Select
                                            defaultValue={
                                                data.product.discountable
                                            }
                                        >
                                            <Option value={true}>False</Option>{' '}
                                            <Option value={false}>True</Option>{' '}
                                        </Select>
                                    )}
                                />
                                {errors.discountable && (
                                    <p className="text-red-500 text-sm mt-1">
                                        discountable is required{' '}
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

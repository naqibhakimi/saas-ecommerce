import Layout from '@/components/layout/Layout';
import Breadcrumbs from '@/components/Breadcrumbs';
import { useQuery } from '@apollo/client';
import { convertEdgeToList } from '@/utils/helpers';
import { _GET_PRODUCTS } from '@/services/products';
import ProductListTable from '@/components/product/productListTable';
import ProductListCard from '@/components/product/productListCard';
import {
    ListBulletIcon,
    ChevronLeftIcon,
    ChevronRightIcon,
    Square2StackIcon,
} from '@heroicons/react/20/solid';

import { useState } from 'react';

enum View {
    ListView,
    TableView,
}

export default function Product() {
    const [tab, setTab] = useState(View.TableView);
    const getProductsQuery = useQuery(_GET_PRODUCTS);

    if (getProductsQuery.error || getProductsQuery.loading) {
        return (
            <Layout>
                <></>
            </Layout>
        );
    }

    return (
        <Layout>
            <Breadcrumbs title="products" />
            <div className="flex justify-between items-center justify-center">
                <div className="w-full mr-4">
                    <div className="relative mt-2 flex items-center">
                        <input
                            type="text"
                            name="search"
                            id="search"
                            className="block w-full rounded-md border-0 py-1.5 pr-14 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                        />
                        <div className="absolute inset-y-0 right-0 flex py-1.5 pr-1.5">
                            <kbd className="inline-flex items-center rounded border border-gray-200 px-1 font-sans text-xs text-gray-400">
                                ⌘K
                            </kbd>
                        </div>
                    </div>
                </div>
                <span className="isolate inline-flex rounded-md shadow-sm">
                    <button
                        type="button"
                        className="relative inline-flex items-center rounded-l-md bg-white px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-100 focus:z-10"
                        onClick={() => setTab(View.ListView)}
                    >
                        <span className="sr-only">Previous</span>
                        <ListBulletIcon
                            className="h-5 w-5"
                            aria-hidden="true"
                        />
                    </button>
                    <button
                        type="button"
                        className="relative -ml-px inline-flex items-center rounded-r-md bg-white px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-100 focus:z-10"
                        onClick={() => setTab(View.TableView)}
                    >
                        <span className="sr-only">Next</span>
                        <Square2StackIcon
                            className="h-5 w-5"
                            aria-hidden="true"
                        />
                    </button>
                    <div className="sm:ml-2 sm:mt-0 sm:flex-none">
                        <button
                            type="button"
                            className="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                        >
                            Add Product
                        </button>
                    </div>
                </span>
            </div>

            {tab === View.TableView ? (
                <ProductListTable
                    products={convertEdgeToList(
                        getProductsQuery.data.products.edges,
                    )}
                ></ProductListTable>
            ) : (
                <ProductListCard
                    products={convertEdgeToList(
                        getProductsQuery.data.products.edges,
                    )}
                ></ProductListCard>
            )}
        </Layout>
    );
}

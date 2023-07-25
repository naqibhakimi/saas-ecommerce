import Layout from '@/components/layout/Layout';
import Breadcrumbs from '@/components/Breadcrumbs';
import ProductDetailComponent from '@/components/product/ProductDetail';
import { useQuery } from '@apollo/client';
import { _GET_PRODUCT_ID } from '@/services/products';
import { useRouter } from 'next/router';
import { useState } from 'react';

export default function CreateProduct() {
    return (
        <Layout>
            <Breadcrumbs title="Create product"></Breadcrumbs>
            <div>
                <h1>This is crate alsdjfalsdjfasd</h1>
            </div>
        </Layout>
    );
}

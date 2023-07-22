import Layout from '@/components/layout/Layout';
import Breadcrumbs from '@/components/Breadcrumbs';
import ProductDetailComponent from '@/components/product/ProductDetail';
import { useQuery } from '@apollo/client';
import { _GET_PRODUCT_ID } from '@/services/products';
import { useRouter } from 'next/router';
import { useState } from 'react';

export default function ProductDetails() {
    return (
        <Layout>
            <Breadcrumbs title="product detail"></Breadcrumbs>
            <div>
                <ProductDetailComponent></ProductDetailComponent>
            </div>
        </Layout>
    );
}

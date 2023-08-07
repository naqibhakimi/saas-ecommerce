import ProductInfo from '@/components/product/createOrUpdate/productInfo';
import ProductVariant from '@/components/product/createOrUpdate/productVariant';
import ProductOffer from '@/components/product/createOrUpdate/productOffer';
import ProductImage from '@/components/product/createOrUpdate/productImage';
import { useState } from 'react';

const tabs = [
    { name: 'Vital info', id: 1, href: '#', current: true },
    { name: 'Variation', id: 2, href: '#', current: false },
    { name: 'Offer', id: 3, href: '#', current: false },
    { name: 'Images', id: 4, href: '#', current: false },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(' ');
}

export default function Example() {
    const [tab, setTab] = useState(1);

    return (
        <>
            <div>
                <div className="sm:hidden">
                    <label htmlFor="tabs" className="sr-only">
                        Select a tab
                    </label>
                    {/* Use an "onChange" listener to redirect the user to the selected tab URL. */}
                    <select
                        id="tabs"
                        name="tabs"
                        className="block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500"
                        defaultValue={tabs.find(tab => tab.current).name}
                    >
                        {tabs.map(tab => (
                            <option key={tab.name}>{tab.name}</option>
                        ))}
                    </select>
                </div>
                <div className="hidden sm:block">
                    <div className="border-b border-gray-200">
                        <nav className="-mb-px flex" aria-label="Tabs">
                            {tabs.map(t => (
                                <a
                                    key={t.id}
                                    onClick={() => setTab(t.id)}
                                    className={classNames(
                                        tab === t.id
                                            ? 'border-indigo-500 text-indigo-600'
                                            : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
                                        'w-1/4 border-b-2 py-4 px-1 text-center text-sm font-medium cursor-pointer',
                                    )}
                                    aria-current={
                                        t.current ? 'page' : undefined
                                    }
                                >
                                    {t.name}
                                </a>
                            ))}
                        </nav>
                    </div>
                </div>
            </div>
            <div>
                {tab === 1 ? <ProductInfo /> : <></>}
                {tab === 2 ? <ProductVariant /> : <></>}
                {tab === 3 ? <ProductOffer /> : <></>}
                {tab === 4 ? <ProductImage /> : <></>}
            </div>
        </>
    );
}

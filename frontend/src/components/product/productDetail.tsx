import ProductSideOver from '@/components/product/ProductSideOver';
import { useState } from 'react';

export default function Example() {
    const [open, setOpen] = useState(false);

    return (
        <>
            <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
                <button
                    onClick={() => (open ? setOpen(false) : setOpen(true))}
                    className="just"
                >
                    123
                </button>
                <h1> something</h1>
            </div>
            <ProductSideOver open={open} setOpen={setOpen} />
        </>
    );
}

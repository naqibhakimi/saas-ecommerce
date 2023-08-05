export default function productOffer() {
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
                                <input
                                    type="text"
                                    name="hs-code"
                                    id="hs-code"
                                    autoComplete="hs-code"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                />
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
                                <input
                                    type="text"
                                    name="mid-code"
                                    id="mid-code"
                                    autoComplete="mid-code"
                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                />
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
                                <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                                    <span className="text-gray-500 sm:text-sm">
                                        $
                                    </span>
                                </div>
                                <input
                                    type="text"
                                    name="price"
                                    id="price"
                                    className="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                                    placeholder="0.00"
                                />
                                <div className="absolute inset-y-0 right-0 flex items-center">
                                    <label
                                        htmlFor="currency"
                                        className="sr-only"
                                    >
                                        Currency
                                    </label>
                                    <select
                                        id="currency"
                                        name="currency"
                                        className="h-full rounded-md border-0 bg-transparent py-0 pl-2 pr-7 text-gray-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
                                    >
                                        <option>USD</option>
                                        <option>CAD</option>
                                        <option>EUR</option>
                                    </select>
                                </div>
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
                                <select
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
                                </select>
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
                                <select
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
                                </select>
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

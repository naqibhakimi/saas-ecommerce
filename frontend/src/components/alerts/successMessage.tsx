import { CheckCircleIcon, XMarkIcon } from '@heroicons/react/20/solid';
import { selectError } from '@/store/slices/errorSlice';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import {
    setSuccessMessage,
    clearSuccessMessage,
    selectSuccessMessage,
} from '@/store/slices/successMessage';

export default function Example() {
    const message = useSelector(selectSuccessMessage);
    const dispatch = useDispatch();

    if (message) setTimeout(() => dispatch(clearSuccessMessage(null)), 5000);

    const close = () => dispatch(clearSuccessMessage(null));

    return message ? (
        <div className="fixed mx-auto max-w-7xl py-12 px-4 sm:px-6 lg:px-8 top-0 z-50 w-2/4 left-1/4">
            <div className="rounded-md bg-green-50 p-4">
                <div className="flex">
                    <div className="flex-shrink-0">
                        <CheckCircleIcon
                            className="h-5 w-5 text-green-400"
                            aria-hidden="true"
                        />
                    </div>
                    <div className="ml-3">
                        <p className="text-sm font-medium text-green-800">
                            {message}
                        </p>
                    </div>
                    <div className="ml-auto pl-3">
                        <div className="-mx-1.5 -my-1.5">
                            <button
                                type="button"
                                className="inline-flex rounded-md bg-green-50 p-1.5 text-green-500 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-green-600 focus:ring-offset-2 focus:ring-offset-green-50"
                            >
                                <span className="sr-only">Dismiss</span>
                                <XMarkIcon
                                    className="h-5 w-5 cursor-pointer"
                                    onClick={close}
                                    aria-hidden="true"
                                />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ) : (
        <></>
    );
}

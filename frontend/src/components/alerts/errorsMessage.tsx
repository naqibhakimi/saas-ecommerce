import { XCircleIcon } from '@heroicons/react/20/solid';
import { selectError } from '@/store/slices/errorSlice';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { clearErrors } from '@/store/slices/errorSlice';

export default function ErrorsMessage() {
    const errors = useSelector(selectError);
    const dispatch = useDispatch();

    if (errors) setTimeout(() => dispatch(clearErrors(null)), 5000);

    const close = () => dispatch(clearErrors(null));

    return errors ? (
        <div className="fixed mx-auto max-w-7xl py-12 px-4 sm:px-6 lg:px-8 top-0 z-50 w-2/4 left-1/4">
            <div className="rounded-md bg-red-50 p-4">
                <div className="flex">
                    <div
                        className="flex-shrink-0 cursor-pointer"
                        onClick={close}
                    >
                        <XCircleIcon
                            className="h-5 w-5 text-red-400"
                            aria-hidden="true"
                        />
                    </div>
                    <div className="ml-3">
                        <h3 className="text-sm font-medium text-red-800">
                            There were {errors.length} errors.
                        </h3>
                        <div className="mt-2 text-sm text-red-700">
                            <ul
                                role="list"
                                className="list-disc space-y-1 pl-5"
                            >
                                {errors &&
                                    errors.map(error => (
                                        <li key={error.code}>
                                            {error.message}
                                        </li>
                                    ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    ) : (
        <></>
    );
}

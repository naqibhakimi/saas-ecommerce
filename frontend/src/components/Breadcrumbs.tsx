import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/react/20/solid';
import Link from 'next/link';
import { useRouter } from 'next/router';

export default function Breadcrumbs({ title }) {
    const router = useRouter();
    const { meetingId } = router.query;

    if (title === 'Home') {
        return <> </>;
    }
    return (
        <div className="px-8 w-full pb-5">
            <div>
                <nav aria-label="Back" className="sm:hidden">
                    <a
                        className="flex items-center text-sm font-medium text-gray-500 hover:text-gray-700 cursor-pointer"
                        onClick={() => router.push('/')}
                    >
                        <ChevronLeftIcon
                            aria-hidden="true"
                            className="-ml-1 mr-1 h-5 w-5 flex-shrink-0 text-gray-400"
                        />
                        Back
                    </a>
                </nav>
                <nav aria-label="Breadcrumb" className="hidden sm:flex">
                    <ol className="flex items-center space-x-4" role="list">
                        <li>
                            <div className="flex">
                                <a
                                    className="text-sm font-medium text-gray-500 hover:text-gray-700 cursor-pointer"
                                    onClick={() => router.push('/')}
                                >
                                    Home
                                </a>
                            </div>
                        </li>

                        {title === 'Meeting Notes' ? (
                            <li>
                                <div className="flex items-center">
                                    <ChevronRightIcon
                                        aria-hidden="true"
                                        className="h-5 w-5 flex-shrink-0 text-gray-400"
                                    />
                                    <a
                                        aria-current="page"
                                        className="ml-4 text-sm font-medium text-gray-500 hover:text-gray-700 cursor-pointer"
                                        onClick={() => router.push('/notes')}
                                    >
                                        Notes
                                    </a>
                                </div>
                            </li>
                        ) : (
                            <></>
                        )}

                        <li>
                            <div className="flex items-center">
                                <ChevronRightIcon
                                    aria-hidden="true"
                                    className="h-5 w-5 flex-shrink-0 text-gray-400"
                                />
                                <a
                                    aria-current="page"
                                    className="ml-4 text-sm font-medium text-gray-500 hover:text-gray-700"
                                    href="#"
                                >
                                    {title}
                                </a>
                            </div>
                        </li>
                    </ol>
                </nav>
            </div>
            <div className="mt-2 md:flex md:items-center md:justify-between">
                <div className="min-w-0 flex-1">
                    <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">
                        {title}
                    </h2>
                </div>
                <div className="mt-4 flex flex-shrink-0 md:ml-4 md:mt-0">
                    {title === 'Meeting Notes' ? (
                        <Link href={'/edit-meeting/' + meetingId}>
                            <button
                                className="inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                                type="button"
                            >
                                Edit
                            </button>
                        </Link>
                    ) : (
                        <></>
                    )}
                </div>
            </div>
        </div>
    );
}

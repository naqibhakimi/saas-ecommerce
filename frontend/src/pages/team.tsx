import Layout from '@/components/layout/Layout';
import Breadcrumbs from '@/components/Breadcrumbs';
import { useQuery } from '@apollo/client';
import { GET_USERS_BY_ORGANIZATION } from '@/services/user';
import { classNames, convertEdgeToList } from '@/utils/helpers';
import {
    CheckCircleIcon,
    EnvelopeIcon,
    EyeIcon,
    PhoneIcon,
    XMarkIcon,
} from '@heroicons/react/20/solid';

export default function Example() {
    const { data, error, loading } = useQuery(GET_USERS_BY_ORGANIZATION, {
        variables: { organizationId: 'T3JnYW5pemF0aW9uTm9kZTox' },
    });

    if (loading) {
        return <></>;
    }

    if (error) {
        return <></>;
    }

    return (
        <Layout>
            <Breadcrumbs title="Team" />
            <div className="px-4 sm:px-6 lg:px-8 mt-6">
                <ul
                    className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3"
                    role="list"
                >
                    {convertEdgeToList(data?.users?.edges).map(person => (
                        <li
                            className="col-span-1 divide-y divide-gray-200 rounded-lg bg-white shadow"
                            key={person.email}
                        >
                            <div className="flex w-full items-center justify-between space-x-6 p-6">
                                <div className="flex-1 truncate">
                                    <div className="flex items-center space-x-3">
                                        <h3 className="truncate text-sm font-medium text-gray-900">
                                            {person?.firstName}{' '}
                                            {person?.lastName}
                                        </h3>
                                        <span className="inline-flex flex-shrink-0 items-center rounded-full bg-green-50 px-1.5 py-0.5 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">
                                            role
                                        </span>
                                    </div>
                                    <p className="mt-1 truncate text-sm text-gray-500">
                                        {person?.email}
                                    </p>
                                </div>
                                <img
                                    alt=""
                                    className="h-10 w-10 flex-shrink-0 rounded-full bg-gray-300"
                                    src="https://api.dicebear.com/6.x/fun-emoji/svg?randomizeIds=falses"
                                />
                            </div>
                            <div>
                                <div className="-mt-px flex divide-x divide-gray-200">
                                    <div className="flex w-0 flex-1">
                                        <a
                                            className="relative -mr-px inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-bl-lg border border-transparent py-4 text-sm font-semibold text-gray-900"
                                            href={`mailto:${person?.email}`}
                                        >
                                            <CheckCircleIcon
                                                aria-hidden="true"
                                                className={classNames(
                                                    person?.isActive
                                                        ? 'text-green-400'
                                                        : 'text-gray-400',
                                                    'h-5 w-5',
                                                )}
                                            />
                                            Active
                                        </a>
                                    </div>
                                    <div className="-ml-px flex w-0 flex-1">
                                        <a
                                            className="relative inline-flex w-0 flex-1 items-center justify-center gap-x-3 rounded-br-lg border border-transparent py-4 text-sm font-semibold text-gray-900"
                                            href={`tel:${person.telephone}`}
                                        >
                                            <CheckCircleIcon
                                                aria-hidden="true"
                                                className={classNames(
                                                    person?.status?.verified
                                                        ? 'text-green-400'
                                                        : 'text-gray-400',
                                                    'h-5 w-5',
                                                )}
                                            />
                                            Verified
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
        </Layout>
    );
}

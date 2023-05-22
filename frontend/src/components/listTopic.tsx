import { _TOPICS } from '@/services/topic';
import { convertEdgeToList } from '@/utils/helpers';
import { useQuery } from '@apollo/client';
import { StarIcon } from '@heroicons/react/24/outline';
import Link from 'next/link';

export default function ListTopics() {
    const { data, error, loading } = useQuery(_TOPICS);

    if (loading) {
        return <></>;
    }

    if (error) {
        return <></>;
    }

    return (
        <ul
            className="mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-6 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-4 lg:gap-8 px-4 sm:px-6 lg:px-8"
            role="list"
        >
            {convertEdgeToList(data?.topics?.edges).map(topic => (
                <Link href={'/topic/' + topic?.id} key={topic?.id}>
                    <li
                        className="rounded-2xl bg-white border border-gray-200 h-full hover:bg-gray-50 hover:shadow-md flex flex-col justify-between"
                        key={topic?.name}
                    >
                        <div className="py-10 px-8 mb-outo h-full">
                            <h3 className=" capitalize text-base font-semibold leading-7 tracking-tight">
                                {topic?.name}
                            </h3>

                            {/* <div className="whitespace-nowrap py-4 text-sm text-gray-500 flex flex-wrap align-top">
                                {topic?.subTopics.edges.map(topic => (
                                    <span
                                        className="truncate capitalize whitespace-nowrap mr-3 mt-3 rounded bg-gray-400 px-2 py-1 text-xs font-medium text-gray-50"
                                        key={topic.node.name}
                                    >
                                        {topic.node.name}
                                    </span>
                                ))}
                            </div> */}
                            <div className="whitespace-nowrap py-4 text-sm  flex flex-wrap align-top">
                                {topic?.jsonTags?.slice(0, 4).map(topic => (
                                    <span
                                        className="truncate capitalize whitespace-nowrap mr-3 mt-3 rounded bg-gray-400 px-2 py-1 text-xs font-medium text-gray-50"
                                        key={topic}
                                    >
                                        {topic}
                                    </span>
                                ))}
                            </div>
                        </div>
                        <div className="border-t border-gray-200">
                            <h4 className="px-8 py-2 text-sm font-normal leading-7 tracking-tight">
                                {topic?.totalFiles} files
                            </h4>
                        </div>
                        <div className="border-t border-gray-200">
                            <h4 className="px-8 py-2 text-sm font-normal leading-7 tracking-tight">
                            <StarIcon
                                aria-hidden="true"
                                className="h-6 w-6 flex-none text-gray-600"
                            />
                            </h4>
                        </div>
                    </li>
                </Link>
            ))}
        </ul>
    );
}

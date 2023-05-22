import { format } from 'date-fns';
import { useEffect, useRef } from 'react';
import { truncate, useWindowSize } from '@/utils/helpers';
import Link from 'next/link';
export default function ListMeetings({ meetings }) {
    const cardRef = useRef(null);
    const size = useWindowSize(cardRef);

    if (!meetings) {
        return <> </>;
    }
    return (
        <>
            <div className="px-4 sm:px-6 lg:px-8 mt-6">
                <ul
                    className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mt-4"
                    role="list"
                >
                    {meetings
                        .filter(meeting => meeting.node.aiSummary !== null)
                        .map(meeting => (
                            <Link
                                href={'/meeting/' + meeting.node.id}
                                key={meeting.node.name}
                            >
                                <li
                                    className="col-span-1 flex flex-col divide-y divide-gray-200 rounded-lg bg-white text-left shadow hover:bg-gray-50 hover:shadow-md h-full"
                                    key={meeting.node.id}
                                    ref={cardRef}
                                >
                                    <div className="flex flex-1 flex-col p-8">
                                        <h3 className="text-sm capitalize font-medium text-gray-900">
                                            {meeting.node.title}
                                        </h3>
                                        <dl className="mt-1 flex flex-grow flex-col justify-between">
                                            <dt className="sr-only">Date</dt>
                                            <dd className="text-sm text-gray-500">
                                                {format(
                                                    new Date(
                                                        meeting.node.createdAt,
                                                    ),
                                                    'LLL d, yyyy',
                                                )}
                                            </dd>
                                            <dd className=" truncate text-sm text-gray-500 mt-4 block whitespace-normal">
                                                {truncate(
                                                    meeting.node.aiSummary ||
                                                        '',
                                                    size?.width / 2,
                                                    true,
                                                )}
                                            </dd>
                                            <dt className="sr-only">Topic</dt>
                                            <dd className="whitespace-nowrap py-4 text-sm text-gray-500 flex flex-wrap align-top">
                                                {meeting.node.topicSet.edges.map(
                                                    topic => (
                                                        <span
                                                            className="truncate capitalize whitespace-nowrap mr-3 mt-3 rounded bg-gray-400 px-2 py-1 text-xs font-medium text-gray-50"
                                                            key={
                                                                topic.node.name
                                                            }
                                                        >
                                                            {topic.node.name}
                                                        </span>
                                                    ),
                                                )}
                                            </dd>
                                        </dl>
                                    </div>
                                </li>
                            </Link>
                        ))}
                </ul>
            </div>
        </>
    );
}

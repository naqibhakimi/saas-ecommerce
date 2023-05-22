import { classNames } from '@/utils/helpers';
import { format } from 'date-fns';
import Link from 'next/link';

export default function ListMeetingsHarzintal({ meetings }) {
    if (!meetings) {
        return <> </>;
    }

    return (
        <div className="px-4 sm:px-6 lg:px-8">
            <div className="mt-8 flow-root">
                <div className="-mx-4 -my-2 sm:-mx-6 lg:-mx-8">
                    <div className="inline-block min-w-full py-2 align-middle">
                        <table className="min-w-full border-separate border-spacing-0">
                            <thead>
                                <tr>
                                    <th
                                        className="sticky top-0 z-10 border-b border-gray-300 bg-white bg-opacity-75 py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 backdrop-blur backdrop-filter sm:pl-6 lg:pl-8"
                                        scope="col"
                                    >
                                        Date
                                    </th>
                                    <th
                                        className="sticky top-0 z-10 hidden border-b border-gray-300 bg-white bg-opacity-75 px-3 py-3.5 text-left text-sm font-semibold text-gray-900 backdrop-blur backdrop-filter sm:table-cell"
                                        scope="col"
                                    >
                                        Summary
                                    </th>
                                    <th
                                        className="sticky top-0 z-10 hidden border-b border-gray-300 bg-white bg-opacity-75 px-3 py-3.5 text-left text-sm font-semibold text-gray-900 backdrop-blur backdrop-filter lg:table-cell"
                                        scope="col"
                                    >
                                        Topics
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {meetings.map((meeting, meetingIdx) => (
                                    <tr key={meeting.node.date}>
                                        <td
                                            className={classNames(
                                                meetingIdx !==
                                                    meetings.length - 1
                                                    ? 'border-b border-gray-200'
                                                    : '',
                                                'whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6 lg:pl-8 align-top',
                                            )}
                                        >
                                            {format(
                                                new Date(
                                                    meeting.node.createdAt,
                                                ),
                                                'LLL d, yyyy',
                                            )}
                                        </td>
                                        <td
                                            className={classNames(
                                                meetingIdx !==
                                                    meetings.length - 1
                                                    ? 'border-b border-gray-200'
                                                    : '',
                                                'whitespace-wrap hidden px-3 py-4 text-sm text-gray-500 sm:table-cell align-top',
                                            )}
                                        >
                                            <Link
                                                href={
                                                    '/meeting/' +
                                                    meeting.node.id
                                                }
                                                key={meeting.node.name}
                                            >
                                                <p>{meeting.node.aiSummary}</p>
                                            </Link>
                                        </td>
                                        <td
                                            className={classNames(
                                                meetingIdx !==
                                                    meetings.length - 1
                                                    ? 'border-b border-gray-200'
                                                    : '',
                                                'whitespace-nowrap px-3 py-4 text-sm text-gray-500 flex flex-wrap align-top',
                                            )}
                                        >
                                            {meeting.node.topicSet.edges.map(
                                                topic => (
                                                    <dd className="mt-3 mr-3 capitalize ">
                                                        <span className="rounded bg-gray-400 px-2 py-1 text-xs font-medium text-gray-50">
                                                            {topic.node.name}
                                                        </span>
                                                    </dd>
                                                ),
                                            )}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
}

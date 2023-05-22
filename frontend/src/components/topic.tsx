import { StarIcon } from '@heroicons/react/20/solid';
import { Fragment, useCallback, useState } from 'react';
import { Listbox, Transition } from '@headlessui/react';
import { CheckIcon, ChevronDownIcon } from '@heroicons/react/20/solid';

import VisNetwork from '@/components/network';

import ListMeetings from '@/components/listMeetings';
import ListMeetingsHarzintal from '@/components/listMeetingsHarzintal';
import { _TOPIC } from '@/services/topic';
import { useQuery } from '@apollo/client';
import { useRouter } from 'next/router';

const actions = [
    {
        name: 'Action 1',
        description: 'The action to be performed',
        current: true,
    },
    {
        name: 'Action 2',
        description: 'The action to be performed',
        current: false,
    },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(' ');
}

export default function Example() {
    const [selected, setSelected] = useState(actions[0]);
    const [tab, setTab] = useState(1);
    const switchTab = newTab => {
        setTab(newTab);
    };

    const router = useRouter();
    const { topicId } = router.query;

    const { data } = useQuery(_TOPIC, {
        variables: { id: topicId },
    });

    return (
        <>
            <div className="min-h-full">
                <header className="">
                    <div className="px-4 sm:px-6 lg:px-8 flex items-center justify-between">
                        <div className="min-w-0 flex-1">
                            <div className="flex justify-start">
                                <div
                                    className="inline-flex items-center justify-center overflow-hidden rounded-full bottom-5 left-5"
                                    x-data="scrollProgress"
                                >
                                    <svg className="w-10 h-12">
                                        <circle
                                            className="text-gray-300"
                                            cx="20"
                                            cy="27"
                                            fill="transparent"
                                            r="12"
                                            stroke="currentColor"
                                            stroke-width="10"
                                        ></circle>
                                        <circle
                                            className="text-blue-600"
                                            cx="20"
                                            cy="27"
                                            fill="transparent"
                                            r="12"
                                            stroke="currentColor"
                                            stroke-dasharray="120"
                                            stroke-dashoffset="100"
                                            stroke-linecap="cube"
                                            stroke-width="10"
                                        ></circle>
                                    </svg>
                                </div>
                                <h1 className="capitalize ml-2 mt-2 md:mt-3 sm:mt-3 text-xl font-normal leading-9 text-gray-900 md:truncate md:text-2xl md:tracking-tight lg:truncate lg:text-2xl lg:tracking-tight sm:truncate sm:text-2xl sm:tracking-tight">
                                    {data?.topic?.name}
                                </h1>
                            </div>
                        </div>
                        <div className="flex mt-0">
                            <StarIcon
                                aria-hidden="true"
                                className="mt-1 h-7 w-7 flex-none text-orange-400"
                            />
                            <Listbox
                                as="div"
                                className="sm:ml-3"
                                onChange={setSelected}
                                value={selected}
                            >
                                {({ open }) => (
                                    <>
                                        <Listbox.Label className="sr-only">
                                            Change published status
                                        </Listbox.Label>
                                        <div className="relative">
                                            <div className="inline-flex divide-x divide-gray-200 rounded-md shadow-sm">
                                                <div className="inline-flex divide-x divide-gray-200 rounded-md shadow-sm">
                                                    <div className="inline-flex items-center gap-x-1.5 rounded-l-md bg-gray-200 px-3 py-2 text-gray-700 shadow-sm">
                                                        <p className="text-sm font-semibold">
                                                            Actions
                                                        </p>
                                                    </div>
                                                    <Listbox.Button className="inline-flex items-center rounded-l-none rounded-r-md text-gray-700 bg-gray-200 p-2 hover:bg-gray-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-gray-200 focus-visible:ring-offset-2 focus-visible:ring-offset-gray-50">
                                                        <span className="sr-only">
                                                            Change published
                                                            status
                                                        </span>
                                                        <ChevronDownIcon
                                                            aria-hidden="true"
                                                            className="h-5 w-5 text-gray-700"
                                                        />
                                                    </Listbox.Button>
                                                </div>
                                            </div>

                                            <Transition
                                                as={Fragment}
                                                leave="transition ease-in duration-100"
                                                leaveFrom="opacity-100"
                                                leaveTo="opacity-0"
                                                show={open}
                                            >
                                                <Listbox.Options className="absolute left-0 z-10 -mr-1 mt-2 w-72 origin-top-right divide-y divide-gray-200 overflow-hidden rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:left-auto sm:right-0">
                                                    {actions.map(option => (
                                                        <Listbox.Option
                                                            className={({
                                                                active,
                                                            }) =>
                                                                classNames(
                                                                    active
                                                                        ? 'bg-gray-50 text-gray-700 '
                                                                        : 'text-gray-500',
                                                                    'cursor-default select-none p-4 text-sm',
                                                                )
                                                            }
                                                            key={option.name}
                                                            value={option}
                                                        >
                                                            {({
                                                                selected,
                                                                active,
                                                            }) => (
                                                                <div className="flex flex-col">
                                                                    <div className="flex justify-between">
                                                                        <p
                                                                            className={
                                                                                selected
                                                                                    ? 'font-semibold'
                                                                                    : 'font-normal'
                                                                            }
                                                                        >
                                                                            {
                                                                                option.name
                                                                            }
                                                                        </p>
                                                                        {selected ? (
                                                                            <span
                                                                                className={
                                                                                    active
                                                                                        ? 'text-white'
                                                                                        : 'text-gray-500'
                                                                                }
                                                                            >
                                                                                <CheckIcon
                                                                                    aria-hidden="true"
                                                                                    className="h-5 w-5"
                                                                                />
                                                                            </span>
                                                                        ) : null}
                                                                    </div>
                                                                    <p
                                                                        className={classNames(
                                                                            active
                                                                                ? 'text-gray-200'
                                                                                : 'text-gray-500',
                                                                            'mt-2',
                                                                        )}
                                                                    >
                                                                        {
                                                                            option.description
                                                                        }
                                                                    </p>
                                                                </div>
                                                            )}
                                                        </Listbox.Option>
                                                    ))}
                                                </Listbox.Options>
                                            </Transition>
                                        </div>
                                    </>
                                )}
                            </Listbox>
                        </div>
                    </div>
                </header>

                <main className="pb-16 pt-8">
                    <div className="mx-auto sm:px-6 lg:px-8">
                        <div className="mt-0">
                            <h2 className="text-2xl font-normal tracking-tight text-gray-900">
                                Summary
                            </h2>
                            <p className="mt-6">{data?.topic?.about}</p>
                        </div>
                        <div className="whitespace-nowrap py-4 text-sm  flex flex-wrap align-top">
                            {data?.topic?.jsonTags?.map(topic => (
                                <span
                                    className="truncate capitalize whitespace-nowrap mr-3 mt-3 rounded bg-gray-400 px-2 py-1 text-xs font-medium text-gray-50"
                                    key={topic}
                                >
                                    {topic}
                                </span>
                            ))}
                        </div>

                        <div className="mt-4">
                            <h2 className="text-xl font-normal tracking-tight text-gray-900">
                                Pain Points and Challenges:
                            </h2>
                            {data?.topic?.jsonPainPointsAndChallenges.length ==
                            0 ? (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    <li className="whitespace-pre-lines">
                                        None Mentioned
                                    </li>
                                </ul>
                            ) : (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    {data?.topic?.jsonPainPointsAndChallenges.map(
                                        topic => (
                                            <li
                                                className="whitespace-pre-lines"
                                                key={topic}
                                            >
                                                {topic}.
                                            </li>
                                        ),
                                    )}
                                </ul>
                            )}
                        </div>

                        <div className="mt-4">
                            <h2 className="text-xl font-normal tracking-tight text-gray-900">
                                Customer Preferences:
                            </h2>
                            {data?.topic?.jsonCustomerPreferences.length ==
                            0 ? (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    <li className="whitespace-pre-lines">
                                        None Mentioned
                                    </li>
                                </ul>
                            ) : (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    {data?.topic?.jsonCustomerPreferences.map(
                                        gap => (
                                            <li
                                                className="whitespace-pre-lines"
                                                key={gap}
                                            >
                                                {gap}.
                                            </li>
                                        ),
                                    )}
                                </ul>
                            )}
                        </div>

                        <div className="mt-4">
                            <h2 className="text-xl font-normal tracking-tight text-gray-900">
                                Desired Features and Capabilities:
                            </h2>
                            {data?.topic?.jsonDesiredFeaturesAndCapabilities
                                .length == 0 ? (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    <li className="whitespace-pre-lines">
                                        None Mentioned
                                    </li>
                                </ul>
                            ) : (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    {data?.topic?.jsonDesiredFeaturesAndCapabilities.map(
                                        topic => (
                                            <li
                                                className="whitespace-pre-lines"
                                                key={topic}
                                            >
                                                {topic}.
                                            </li>
                                        ),
                                    )}
                                </ul>
                            )}
                        </div>

                        <div className="mt-4">
                            <h2 className="text-xl font-normal tracking-tight text-gray-900">
                                Open Questions:
                            </h2>
                            {data?.topic?.jsonOpenQuestions.length == 0 ? (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    <li className="whitespace-pre-lines">
                                        None Mentioned
                                    </li>
                                </ul>
                            ) : (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    {data?.topic?.jsonOpenQuestions.map(
                                        topic => (
                                            <li
                                                className="whitespace-pre-lines"
                                                key={topic}
                                            >
                                                {topic}.
                                            </li>
                                        ),
                                    )}
                                </ul>
                            )}
                        </div>

                        <div className="mt-4">
                            <h2 className="text-xl font-normal tracking-tight text-gray-900">
                                Knowledge Gap:
                            </h2>
                            {data?.topic?.jsonKnowledgeGaps.length == 0 ? (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    <li className="whitespace-pre-lines">
                                        None Mentioned
                                    </li>
                                </ul>
                            ) : (
                                <ul className="list-disc flex flex-col  mt-2 ml-6">
                                    {data?.topic?.jsonKnowledgeGaps.map(
                                        topic => (
                                            <li
                                                className="whitespace-pre-lines"
                                                key={topic}
                                            >
                                                {topic}.
                                            </li>
                                        ),
                                    )}
                                </ul>
                            )}
                        </div>
                    </div>
                    <div className="px-4 sm:px-6 lg:px-8 mt-6">
                        <div className="flex justify-between">
                            <h4 className="text-xl text-gray-900 font-semibold">
                                Skryb Notes {tab}
                            </h4>
                            <span className="isolate inline-flex rounded-md shadow-sm">
                                <button
                                    className={classNames(
                                        tab === 1
                                            ? 'bg-orange-200 ring-orage-300 hover:bg-orange-200'
                                            : 'bg-gray-200 ring-gray-300 hover:bg-orange-200',
                                        'relative inline-flex items-center rounded-l-md px-3 py-2 text-sm font-medium text-gray-900 uppercase ring-0 ring-inset focus:z-10',
                                    )}
                                    onClick={() => switchTab(1)}
                                    type="button"
                                >
                                    Tiles
                                </button>
                                <button
                                    className={classNames(
                                        tab === 2
                                            ? 'bg-orange-200 ring-orage-300 hover:bg-orange-200'
                                            : 'bg-gray-200 ring-gray-300 hover:bg-orange-200',
                                        'relative -ml-px inline-flex items-center px-3 py-2 text-sm font-medium text-gray-900 uppercase ring-0 ring-inset ring-gray-300 focus:z-10',
                                    )}
                                    onClick={() => switchTab(2)}
                                    type="button"
                                >
                                    Timeline
                                </button>
                                <button
                                    className={classNames(
                                        tab === 3
                                            ? 'bg-orange-200 ring-orage-300 hover:bg-orange-200'
                                            : 'bg-gray-200 ring-gray-300 hover:bg-orange-200',
                                        'relative -ml-px inline-flex items-center px-3 py-2 text-sm font-medium text-gray-900 uppercase ring-0 ring-inset ring-gray-300 focus:z-10',
                                    )}
                                    onClick={() => switchTab(3)}
                                    type="button"
                                >
                                    Knowledge
                                </button>
                            </span>
                        </div>
                    </div>

                    {tab === 1 && (
                        <ListMeetings meetings={data?.topic?.meetings?.edges} />
                    )}
                    {tab === 2 && (
                        <ListMeetingsHarzintal
                            meetings={data?.topic?.meetings?.edges}
                        />
                    )}
                    {tab === 3 && (
                        <VisNetwork
                            edges={data?.topic?.network?.edges}
                            nodes={data?.topic?.network?.nodes}
                        />
                    )}
                </main>
            </div>
        </>
    );
}

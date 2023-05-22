import { Fragment, useCallback, useContext, useState } from 'react';
import { Dialog, Menu, Transition } from '@headlessui/react';
import {
    Bars3Icon,
    BellIcon,
    CalendarIcon,
    Cog6ToothIcon,
    DocumentDuplicateIcon,
    FolderIcon,
    HomeIcon,
    UsersIcon,
    QuestionMarkCircleIcon,
    StarIcon,
    XMarkIcon,
} from '@heroicons/react/24/outline';
import {
    ChevronDownIcon,
    MagnifyingGlassIcon,
    PlusIcon,
} from '@heroicons/react/20/solid';

const navigation = [
    { name: 'Home', href: '/', icon: HomeIcon, current: false },
    { name: 'My favourites', href: '#', icon: StarIcon, current: false },
    {
        name: 'Topics',
        href: '/topics',
        icon: DocumentDuplicateIcon,
        current: true,
    },
    { name: 'Notes', href: '/notes', icon: FolderIcon, current: false },
    { name: 'Calendar', href: '#', icon: CalendarIcon, current: false },
];
const settings = [
    { name: 'Team', href: '/team', icon: UsersIcon, current: false },
    { name: 'Help', href: '#', icon: QuestionMarkCircleIcon, current: false },
    {
        name: 'Settings',
        href: '#',
        icon: Cog6ToothIcon,
        current: false,
    },
];
const userNavigation = [
    { name: 'Your profile', href: '#' },
    { name: 'Sign out', href: '#' },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(' ');
}

import CreateTopic from '@/components/modals/CreateTopic';
import { useDispatch, useSelector } from 'react-redux';
import { openModal } from '@/store/slices/createTopicSlice';
import { selectEvent } from '@/store/slices/eventSlice';
import { UserContext } from '../../contexts/user';
import { NextRouter, useRouter } from 'next/router';
import Link from 'next/link';

export default function Layout({ children }) {
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const router: NextRouter = useRouter();

    const dispatch = useDispatch();

    const baseEvent = useSelector(selectEvent);

    function openCreateModal(e) {
        dispatch(openModal(true));
    }

    const user = useContext(UserContext);

    const signOut = () => {
        localStorage.removeItem('auth');
        router.push('/');
    };

    return (
        <>
            <CreateTopic />
            <div>
                <Transition.Root as={Fragment} show={sidebarOpen}>
                    <Dialog
                        as="div"
                        className="relative z-20 lg:hidden "
                        onClose={setSidebarOpen}
                    >
                        <Transition.Child
                            as={Fragment}
                            enter="transition-opacity ease-linear duration-300"
                            enterFrom="opacity-0"
                            enterTo="opacity-100"
                            leave="transition-opacity ease-linear duration-300"
                            leaveFrom="opacity-100"
                            leaveTo="opacity-0"
                        >
                            <div className="fixed inset-0 bg-gray-900/80" />
                        </Transition.Child>

                        <div className="fixed inset-0 flex">
                            <Transition.Child
                                as={Fragment}
                                enter="transition ease-in-out duration-300 transform"
                                enterFrom="-translate-x-full"
                                enterTo="translate-x-0"
                                leave="transition ease-in-out duration-300 transform"
                                leaveFrom="translate-x-0"
                                leaveTo="-translate-x-full"
                            >
                                <Dialog.Panel className="relative mr-16 flex w-full max-w-xs flex-1">
                                    <Transition.Child
                                        as={Fragment}
                                        enter="ease-in-out duration-300"
                                        enterFrom="opacity-0"
                                        enterTo="opacity-100"
                                        leave="ease-in-out duration-300"
                                        leaveFrom="opacity-100"
                                        leaveTo="opacity-0"
                                    >
                                        <div className="absolute left-full top-0 flex w-16 justify-center pt-5">
                                            <button
                                                className="-m-2.5 p-2.5"
                                                onClick={() =>
                                                    setSidebarOpen(false)
                                                }
                                                type="button"
                                            >
                                                <span className="sr-only">
                                                    Close sidebar
                                                </span>
                                                <XMarkIcon
                                                    aria-hidden="true"
                                                    className="h-6 w-6 text-white"
                                                />
                                            </button>
                                        </div>
                                    </Transition.Child>
                                    {/* Sidebar component, swap this element with another sidebar if you like */}
                                    <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6">
                                        <div className="flex h-16 shrink-0 items-center">
                                            <img
                                                alt="QuikBuy"
                                                className="h-8 w-auto"
                                                src="/Skryb.svg"
                                            />{' '}
                                        </div>
                                        <nav className="flex flex-1 flex-col">
                                            <ul
                                                className="flex flex-1 flex-col gap-y-7"
                                                role="list"
                                            >
                                                <li className="w-full">
                                                    {baseEvent.event_type ===
                                                        'skrybing' &&
                                                    baseEvent.data !==
                                                        '100%' ? (
                                                        <div className="flex-shrink-0">
                                                            <button
                                                                className=" w-full text-center justify-center relative inline-flex items-center gap-x-1.5 rounded-md bg-pink-600 px-4 py-2 text-sm font-semibold text-white shadow-sm disabled:bg-pink-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
                                                                disabled={true}
                                                                onClick={
                                                                    openCreateModal
                                                                }
                                                                type="button"
                                                            >
                                                                Skrybing{' '}
                                                                {baseEvent.data}
                                                            </button>
                                                        </div>
                                                    ) : (
                                                        <div className="flex-shrink-0">
                                                            <button
                                                                className=" w-full text-center justify-center relative inline-flex items-center gap-x-1.5 rounded-md bg-pink-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-pink-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
                                                                onClick={
                                                                    openCreateModal
                                                                }
                                                                type="button"
                                                            >
                                                                Start Skrybing
                                                            </button>
                                                        </div>
                                                    )}
                                                </li>
                                                <li>
                                                    <ul
                                                        className="-mx-2 space-y-1"
                                                        role="list"
                                                    >
                                                        {navigation.map(
                                                            item => (
                                                                <li
                                                                    key={
                                                                        item.name
                                                                    }
                                                                >
                                                                    <Link
                                                                        className={classNames(
                                                                            router.asPath ==
                                                                                item.href
                                                                                ? 'bg-gray-900 text-pink-600'
                                                                                : 'text-gray-400 hover:text-pink-600 hover:bg-gray-800',
                                                                            'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold',
                                                                        )}
                                                                        href={
                                                                            item.href
                                                                        }
                                                                    >
                                                                        <item.icon
                                                                            aria-hidden="true"
                                                                            className={classNames(
                                                                                router.asPath ==
                                                                                    item.href
                                                                                    ? 'text-pink-600'
                                                                                    : 'text-gray-400 group-hover:text-pink-600',
                                                                                'h-6 w-6 shrink-0',
                                                                            )}
                                                                        />
                                                                        {
                                                                            item.name
                                                                        }
                                                                    </Link>
                                                                </li>
                                                            ),
                                                        )}
                                                    </ul>
                                                </li>
                                                <li>
                                                    <div className="text-xs font-semibold leading-6 text-gray-400">
                                                        SETTINGS
                                                    </div>
                                                    <ul
                                                        className="-mx-2 mt-2 space-y-1"
                                                        role="list"
                                                    >
                                                        {settings.map(item => (
                                                            <li key={item.name}>
                                                                <Link
                                                                    className={classNames(
                                                                        router.asPath ==
                                                                            item.href
                                                                            ? 'bg-gray-900 text-pink-600'
                                                                            : 'text-gray-400 hover:text-pink-600 hover:bg-gray-800',
                                                                        'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold',
                                                                    )}
                                                                    href={
                                                                        item.href
                                                                    }
                                                                >
                                                                    <item.icon
                                                                        aria-hidden="true"
                                                                        className={classNames(
                                                                            router.asPath ==
                                                                                item.href
                                                                                ? 'text-pink-600'
                                                                                : 'text-gray-400 group-hover:text-pink-600',
                                                                            'h-6 w-6 shrink-0',
                                                                        )}
                                                                    />
                                                                    {item.name}
                                                                </Link>
                                                            </li>
                                                        ))}
                                                    </ul>
                                                </li>
                                            </ul>
                                        </nav>
                                    </div>
                                </Dialog.Panel>
                            </Transition.Child>
                        </div>
                    </Dialog>
                </Transition.Root>

                {/* Static sidebar for desktop */}
                <div className="hidden lg:fixed lg:inset-y-0 lg:z-10 lg:flex lg:w-72 lg:flex-col">
                    {/* Sidebar component, swap this element with another sidebar if you like */}
                    <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6">
                        <div className="flex h-16 shrink-0 items-center">
                            <img
                                alt="QuikBuy"
                                className="h-8 w-auto"
                                src="/Skryb.svg"
                            />{' '}
                        </div>
                        <nav className="flex flex-1 flex-col">
                            <ul
                                className="flex flex-1 flex-col gap-y-7"
                                role="list"
                            >
                                <li className="w-full">
                                    {baseEvent.event_type === 'skrybing' &&
                                    baseEvent.data !== '100%' ? (
                                        <div className="flex-shrink-0">
                                            <button
                                                className=" w-full text-center justify-center relative inline-flex items-center gap-x-1.5 rounded-md bg-pink-600 px-4 py-2 text-sm font-semibold text-white shadow-sm disabled:bg-pink-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
                                                disabled={true}
                                                onClick={openCreateModal}
                                                type="button"
                                            >
                                                Skrybing {baseEvent.data}
                                            </button>
                                        </div>
                                    ) : (
                                        <div className="flex-shrink-0">
                                            <button
                                                className=" w-full text-center justify-center relative inline-flex items-center gap-x-1.5 rounded-md bg-pink-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-pink-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
                                                onClick={openCreateModal}
                                                type="button"
                                            >
                                                Start Skrybing
                                            </button>
                                        </div>
                                    )}
                                </li>
                                <li>
                                    <ul className="-mx-2 space-y-1" role="list">
                                        {navigation.map(item => (
                                            <li key={item.name}>
                                                <Link
                                                    className={classNames(
                                                        router.asPath ==
                                                            item.href
                                                            ? 'bg-gray-900 text-pink-600'
                                                            : 'text-gray-400 hover:text-pink-600 hover:bg-gray-800',
                                                        'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold',
                                                    )}
                                                    href={item.href}
                                                >
                                                    <item.icon
                                                        aria-hidden="true"
                                                        className={classNames(
                                                            router.asPath ==
                                                                item.href
                                                                ? 'text-pink-600'
                                                                : 'text-gray-400 group-hover:text-pink-600',
                                                            'h-6 w-6 shrink-0',
                                                        )}
                                                    />
                                                    {item.name}
                                                </Link>
                                            </li>
                                        ))}
                                    </ul>
                                </li>
                                <li>
                                    <div className="text-xs font-semibold leading-6 text-gray-400">
                                        SETTINGS
                                    </div>
                                    <ul
                                        className="-mx-2 mt-2 space-y-1"
                                        role="list"
                                    >
                                   {settings.map(item => (
                                                            <li key={item.name}>
                                                                <Link
                                                                    className={classNames(
                                                                        router.asPath ==
                                                                            item.href
                                                                            ? 'bg-gray-900 text-pink-600'
                                                                            : 'text-gray-400 hover:text-pink-600 hover:bg-gray-800',
                                                                        'group flex gap-x-3 rounded-md p-2 text-sm leading-6 font-semibold',
                                                                    )}
                                                                    href={
                                                                        item.href
                                                                    }
                                                                >
                                                                    <item.icon
                                                                        aria-hidden="true"
                                                                        className={classNames(
                                                                            router.asPath ==
                                                                                item.href
                                                                                ? 'text-pink-600'
                                                                                : 'text-gray-400 group-hover:text-pink-600',
                                                                            'h-6 w-6 shrink-0',
                                                                        )}
                                                                    />
                                                                    {item.name}
                                                                </Link>
                                                            </li>
                                                        ))}
                                    </ul>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>

                <div className="lg:pl-72">
                    <div className="sticky top-0 z-10 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 bg-white px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
                        <button
                            className="-m-2.5 p-2.5 text-gray-900 lg:hidden"
                            onClick={() => setSidebarOpen(true)}
                            type="button"
                        >
                            <span className="sr-only">Open sidebar</span>
                            <Bars3Icon aria-hidden="true" className="h-6 w-6" />
                        </button>

                        {/* Separator */}
                        <div
                            aria-hidden="true"
                            className="h-6 w-px bg-gray-200 lg:hidden"
                        />

                        <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
                            <form
                                action="#"
                                className="relative flex flex-1"
                                method="GET"
                            >
                                <label
                                    className="sr-only"
                                    htmlFor="search-field"
                                >
                                    Search
                                </label>
                                <MagnifyingGlassIcon
                                    aria-hidden="true"
                                    className="pointer-events-none absolute inset-y-0 left-0 h-full w-5 text-gray-400"
                                />
                                <input
                                    className="block h-full w-full border-0 py-0 pl-8 pr-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm"
                                    id="search-field"
                                    name="search"
                                    placeholder="Search..."
                                    type="search"
                                />
                            </form>
                            <div className="flex items-center gap-x-4 lg:gap-x-6">
                                <button
                                    className="-m-2.5 p-2.5 text-gray-400 hover:text-gray-500"
                                    type="button"
                                >
                                    <span className="sr-only">
                                        View notifications
                                    </span>
                                    <BellIcon
                                        aria-hidden="true"
                                        className="h-6 w-6"
                                    />
                                </button>

                                {/* Separator */}
                                <div
                                    aria-hidden="true"
                                    className="hidden lg:block lg:h-6 lg:w-px lg:bg-gray-200"
                                />

                                {/* Profile dropdown */}
                                <Menu as="div" className="relative">
                                    <Menu.Button className="-m-1.5 flex items-center p-1.5">
                                        <span className="sr-only">
                                            Open user menu
                                        </span>
                                        <img
                                            alt=""
                                            className="h-8 w-8 rounded-full bg-gray-50"
                                            src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                        />
                                        <span className="hidden lg:flex lg:items-center">
                                            <span
                                                aria-hidden="true"
                                                className="ml-4 text-sm font-semibold leading-6 text-gray-900"
                                            >
                                                {user?.email}
                                            </span>
                                            <ChevronDownIcon
                                                aria-hidden="true"
                                                className="ml-2 h-5 w-5 text-gray-400"
                                            />
                                        </span>
                                    </Menu.Button>
                                    <Transition
                                        as={Fragment}
                                        enter="transition ease-out duration-100"
                                        enterFrom="transform opacity-0 scale-95"
                                        enterTo="transform opacity-100 scale-100"
                                        leave="transition ease-in duration-75"
                                        leaveFrom="transform opacity-100 scale-100"
                                        leaveTo="transform opacity-0 scale-95"
                                    >
                                        <Menu.Items className="absolute right-0 z-10 mt-2.5 w-32 origin-top-right rounded-md bg-white py-2 shadow-lg ring-1 ring-gray-900/5 focus:outline-none">
                                            {userNavigation.map(item => (
                                                <Menu.Item key={item.name}>
                                                    {({ active }) => (
                                                        <a
                                                            className={classNames(
                                                                active
                                                                    ? 'bg-gray-50'
                                                                    : '',
                                                                'block px-3 py-1 text-sm leading-6 text-gray-900 cursor-pointer',
                                                            )}
                                                            onClick={signOut}
                                                        >
                                                            {item.name}
                                                        </a>
                                                    )}
                                                </Menu.Item>
                                            ))}
                                        </Menu.Items>
                                    </Transition>
                                </Menu>
                            </div>
                        </div>
                    </div>

                    <main className="py-10 overflow-auto">
                        <div className="px-4 sm:px-6 lg:px-8">{children}</div>
                    </main>
                </div>
            </div>
        </>
    );
}

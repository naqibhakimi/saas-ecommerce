import { TOPIC_EVENTS } from '@/services/topic';
import { setEvent } from '@/store/slices/eventSlice';
import { useSubscription } from '@/utils/subscription';
import { XMarkIcon } from '@heroicons/react/20/solid';
import { useDispatch, useSelector } from 'react-redux';

export default function TopicEventsBanner() {
    const [data] = useSubscription({
        query: TOPIC_EVENTS,
        variables: { id: 'not required' },
        fetchPolicy: 'no-cache',
    });

    const dispatch = useDispatch();

    const close = () => {
        data.topicEvents = null;
    };

    if (data?.topicEvents == 'Done'){
        window.location.reload();
    }

    return (
        <>
            {data?.topicEvents ? (
                <div className="fixed inset-x-0 bottom-0 z-50">
                    <div className="flex items-center gap-x-6 bg-gray-900 py-2.5 px-6 sm:px-3.5 sm:before:flex-1">
                        <p className="text-sm leading-6 text-white">
                            <a href="#">
                                <strong className="font-semibold">
                                    Skrybing :{' '}
                                </strong>
                                {data?.topicEvents}
                            </a>
                        </p>
                        <div className="flex flex-1 justify-end">
                            {/* <button
 className="-m-3 p-3 focus-visible:outline-offset-[-4px]"
 onClick={close}
 type="button"
 >
 <span className="sr-only">Dismiss</span>
 <XMarkIcon
 aria-hidden="true"
 className="h-5 w-5 text-white"
 />
 </button> */}
                        </div>
                    </div>
                </div>
            ) : (
                <></>
            )}
        </>
    );
}

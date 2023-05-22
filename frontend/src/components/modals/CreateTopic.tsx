import {
    ChangeEvent,
    Fragment,
    useCallback,
    useEffect,
    useRef,
    useState,
} from 'react';
import { Dialog, Transition } from '@headlessui/react';

import { useDispatch, useSelector } from 'react-redux';

import { selectModalState } from '@/store/slices/createTopicSlice';

import { openModal } from '@/store/slices/createTopicSlice';
import { PhotoIcon } from '@heroicons/react/20/solid';
import { useMutation } from '@apollo/client';
import { _CREATE_MEETING, _UPDATE_MEETINGS } from '@/services/meeting';
import { FieldValues, useForm } from 'react-hook-form';
import { LOGIN_WELLCOME_MESSAGE } from '@/constents';
import { setErrors } from '@/store/slices/errorSlice';
import {
    clearSuccessMessage,
    setSuccessMessage,
} from '@/store/slices/successMessage';
import { NextRouter } from 'next/router';
import { setEvent } from '@/store/slices/eventSlice';
import { useDropzone } from 'react-dropzone';

const resetFile = file => {
    if (file?.current) {
        file.current.value = '';
    }
};

export default function CreateTopic() {
    const isOpened = useSelector(selectModalState);
    const dispatch = useDispatch();
    const [progress, setProgress] = useState(null);
    const [open, setOpen] = useState(false);
    const [fileEmpty, setFileEmpty] = useState(null);

    const onDrop = useCallback(acceptedFiles => {
        console.log('---');
        console.log(acceptedFiles);
        setFileEmpty(acceptedFiles[0]);
    }, []);
    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
    });

    const {
        register,
        handleSubmit,
        reset,
        trigger,
        formState: { errors, isValid },
    } = useForm({ mode: 'all' });

    useEffect(() => {
        setOpen(isOpened);
        reset();
        setProgress(0);
    }, [isOpened]);

    const file = useRef();

    const cancelButtonRef = useRef(null);

    useEffect(() => {
        if (!open) {
            dispatch(openModal(false));
        }
    }, [open]);

    const [creatMeeting, { data: createMeetingData }] = useMutation(
        _CREATE_MEETING,
        {
            onError(error) {
                dispatch(setErrors([{ message: error.message }]));
                dispatch(clearSuccessMessage(null));
            },
        },
    );

    const [updateMeeting, { data: updateMeetingData, loading }] = useMutation(
        _UPDATE_MEETINGS,
        {
            onError(error) {
                dispatch(setErrors([{ message: error.message }]));
                dispatch(clearSuccessMessage(null));
            },
        },
    );

    if (loading) {
        dispatch(setSuccessMessage('Loading...'));
    }

    if (createMeetingData?.createMeeting?.errors) {
        dispatch(
            setErrors(createMeetingData.createMeeting.errors.nonFieldErrors),
        );
    }

    useEffect(() => {
        if (createMeetingData?.createMeeting.success) {
            resetFile(file);
            dispatch(setSuccessMessage('File Uploaded'));
            trigger('file_bin');
        }
    }, [createMeetingData]);

    useEffect(() => {
        if (updateMeetingData?.updateMeeting.success) {
            setOpen(false);
            dispatch(
                setEvent({
                    event_id: '',
                    event_type: 'meeting_created',
                    data: createMeetingData.createMeeting.meeting,
                }),
            );
        }
    }, [updateMeetingData?.updateMeeting.success]);

    const onClose = () => {
        setOpen(false);
    };
    const onSubmit = data => {
        console.log('onSubmit');
        setOpen(false);
        creatMeeting({
            variables: { input: { meeting: { fileBin: fileEmpty } } },
            context: {
                hasUpload: true,
                fetchOptions: {
                    useUpload: true,
                    onProgress: (ev: ProgressEvent) => {
                        resetFile(file);
                        dispatch(
                            setEvent({
                                event_id: '',
                                event_type: 'skrybing',
                                data:
                                    ((ev.loaded / ev.total) * 100).toFixed(0) +
                                    '%',
                            }),
                        );
                    },
                    onAbortPossible: (abortHandler: any) => {
                        resetFile(file);
                    },
                },
            },
        });
    };

    const fileChanged = ({ target: { files = [] } }) => {
        console.log(files);
        setFileEmpty(files[0]);
    };
    return (
        <>
            <Transition.Root as={Fragment} show={open}>
                <Dialog
                    as="div"
                    className="relative z-10"
                    initialFocus={cancelButtonRef}
                    onClose={onClose}
                >
                    <Transition.Child
                        as={Fragment}
                        enter="ease-out duration-300"
                        enterFrom="opacity-0"
                        enterTo="opacity-100"
                        leave="ease-in duration-200"
                        leaveFrom="opacity-100"
                        leaveTo="opacity-0"
                    >
                        <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                    </Transition.Child>

                    <div className="fixed inset-0 z-10 overflow-y-auto">
                        <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                            <Transition.Child
                                as={Fragment}
                                enter="ease-out duration-300"
                                enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                                enterTo="opacity-100 translate-y-0 sm:scale-100"
                                leave="ease-in duration-200"
                                leaveFrom="opacity-100 translate-y-0 sm:scale-100"
                                leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                            >
                                <Dialog.Panel className="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:w-full sm:max-w-lg">
                                    <form
                                        className="bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-xl md:col-span-2"
                                        noValidate
                                        onSubmit={handleSubmit(onSubmit)}
                                    >
                                        <div className="px-4 py-6 sm:p-8">
                                            <div className="">
                                                <h3 className=" text-gray-900 h-3 font-bold mb-4">
                                                    Upload Your Video, Audio,
                                                    and Text Files Here
                                                </h3>
                                                <h6 className="text-gray-900 h-6 mb-20">
                                                    This modal allows you to
                                                    easily upload video, audio,
                                                    and text files to be
                                                    QuikBuyd. Simply drag and
                                                    drop your files, review the
                                                    preview, and click Skryb It
                                                    to start the upload and
                                                    skrybing process.
                                                </h6>
                                                <div
                                                    className=""
                                                    {...getRootProps()}
                                                >
                                                    <div className="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                                                        <div className="text-center">
                                                            <PhotoIcon
                                                                aria-hidden="true"
                                                                className="mx-auto h-12 w-12 text-gray-300"
                                                            />
                                                            <div className="mt-4 flex text-sm leading-6 text-gray-600">
                                                                <label
                                                                    className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-offset-2"
                                                                    htmlFor="file_bin"
                                                                >
                                                                    <span>
                                                                        Upload a
                                                                        file
                                                                    </span>
                                                                    <input
                                                                        {...getInputProps()}
                                                                        ref={
                                                                            file
                                                                        }
                                                                        {...register(
                                                                            'file_bin',
                                                                            {
                                                                                required:
                                                                                    true,
                                                                            },
                                                                        )}
                                                                        className="sr-only"
                                                                        id="file_bin"
                                                                        name="file_bin"
                                                                        onChange={
                                                                            fileChanged
                                                                        }
                                                                        type="file"
                                                                    />
                                                                </label>
                                                                <p className="pl-1">
                                                                    or drag and
                                                                    drop
                                                                </p>
                                                            </div>
                                                            <p className="text-xs leading-5 text-gray-600">
                                                                MP4, MP3, WAV
                                                                and TXT file up
                                                                to 1GB are
                                                                supported
                                                            </p>
                                                        </div>
                                                    </div>
                                                    {progress ? (
                                                        <div>
                                                            <div className="mb-1 text-base font-medium text-blue-700 dark:text-blue-500">
                                                                {progress}
                                                            </div>
                                                            <div className="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
                                                                <div
                                                                    className="bg-gray-900 h-2.5 rounded-full"
                                                                    style={{
                                                                        width: progress,
                                                                    }}
                                                                ></div>
                                                            </div>
                                                        </div>
                                                    ) : (
                                                        <></>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                        <div className="flex items-center justify-end gap-x-6 border-t border-gray-900/10 px-4 py-4 sm:px-8">
                                            <button
                                                className="text-sm font-semibold leading-6 text-gray-900"
                                                onClick={onClose}
                                                type="button"
                                            >
                                                Cancel
                                            </button>
                                            <button
                                                className="disabled:bg-gray-500 px-5 rounded-md bg-gray-900 py-2 text-sm font-semibold text-white shadow-sm hover:bg-gray-800 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-800"
                                                disabled={!fileEmpty}
                                                onClick={onSubmit}
                                                type="submit"
                                            >
                                                Skryb it
                                            </button>
                                            {/* {JSON.stringify(errors)} */}
                                        </div>
                                    </form>
                                </Dialog.Panel>
                            </Transition.Child>
                        </div>
                    </div>
                </Dialog>
            </Transition.Root>
        </>
    );
}

import Topic from '@/components/topic';

import Layout from '@/components/layout/Layout';

import React, { useCallback, useMemo, useState } from 'react';
import isHotkey from 'is-hotkey';
import { Editable, Slate, useSlate, withReact } from 'slate-react';
import { useDispatch, useSelector } from 'react-redux';

import Breadcrumbs from '@/components/Breadcrumbs';

import {
    createEditor,
    Descendant,
    Editor,
    Element as SlateElement,
    Transforms,
} from 'slate';
import { withHistory } from 'slate-history';

import { Button, Icon, Toolbar } from '@/components/editor/component';
import { useRouter } from 'next/router';
import { useMutation, useQuery } from '@apollo/client';
import { _MEETING, _UPDATE_MEETINGS } from '@/services/meeting';

import { setErrors } from '@/store/slices/errorSlice';
import { classNames } from '@/utils/helpers';

import { clearSuccessMessage } from '@/store/slices/successMessage';

const HOTKEYS = {
    'mod+b': 'bold',
    'mod+i': 'italic',
    'mod+u': 'underline',
    'mod+`': 'code',
};

const LIST_TYPES = ['numbered-list', 'bulleted-list'];
const TEXT_ALIGN_TYPES = ['left', 'center', 'right', 'justify'];

const MeetingNotes = () => {
    const renderElement = useCallback(props => <Element {...props} />, []);
    const renderLeaf = useCallback(props => <Leaf {...props} />, []);
    const editor = useMemo(() => withHistory(withReact(createEditor())), []);

    const dispatch = useDispatch();

    const [updateMeeting, { data: updateMeetingData, loading }] = useMutation(
        _UPDATE_MEETINGS,
        {
            onError(error) {
                dispatch(setErrors([{ message: error.message }]));
                dispatch(clearSuccessMessage(null));
            },
        },
    );

    const router = useRouter();
    const { meetingId } = router.query;

    const { data } = useQuery(_MEETING, {
        variables: { id: meetingId },
    });

    if (!data?.Meeting) {
        return (
            <Layout>
                <></>
            </Layout>
        );
    }

    return (
        <Layout>
            <Slate
                editor={editor}
                onChange={value => {
                    const isAstChange = editor.operations.some(
                        op => 'set_selection' !== op.type,
                    );
                    if (isAstChange) {
                        // Save the value to Local Storage.
                        const content = JSON.stringify(value);
                        localStorage.setItem('content', content);
                        updateMeeting({
                            variables: {
                                input: {
                                    meeting: {
                                        id: meetingId,
                                        notes: content,
                                    },
                                },
                            },
                        });
                    }
                }}
                value={JSON.parse(data.Meeting.notes)}
            >
                <Toolbar>
                    <Breadcrumbs title="Meeting Notes" />
                    <MarkButton format="bold" icon="format_bold" />
                    <MarkButton format="italic" icon="format_italic" />
                    <MarkButton format="underline" icon="format_underlined" />
                    <MarkButton format="code" icon="code" />
                    <BlockButton format="heading-one" icon="looks_one" />
                    <BlockButton format="heading-two" icon="looks_two" />
                    <BlockButton format="heading-three" icon="looks_3" />
                    <BlockButton format="heading-four" icon="looks_4" />
                    <BlockButton
                        format="numbered-list"
                        icon="format_list_numbered"
                    />
                    <BlockButton
                        format="bulleted-list"
                        icon="format_list_bulleted"
                    />
                    <BlockButton format="left" icon="format_align_left" />
                    <BlockButton format="center" icon="format_align_center" />
                    <BlockButton format="right" icon="format_align_right" />
                    <BlockButton format="justify" icon="format_align_justify" />

                    <BlockButton format="move_left" icon="west" />
                    <BlockButton format="move_right" icon="east" />
                    <BlockButton format="save" icon="save" />
                </Toolbar>
                <Editable
                    autoFocus
                    className="pt-32"
                    onKeyDown={event => {
                        for (const hotkey in HOTKEYS) {
                            if (isHotkey(hotkey, event as any)) {
                                event.preventDefault();
                                const mark = HOTKEYS[hotkey];
                                toggleMark(editor, mark);
                            }
                        }
                    }}
                    placeholder="Meeting Notes ..."
                    renderElement={renderElement}
                    renderLeaf={renderLeaf}
                    spellCheck
                />
            </Slate>
        </Layout>
    );
};

export default MeetingNotes;

const toggleBlock = (editor, format) => {
    const isActive = isBlockActive(
        editor,
        format,
        TEXT_ALIGN_TYPES.includes(format) ? 'align' : 'type',
    );
    const isList = LIST_TYPES.includes(format);

    Transforms.unwrapNodes(editor, {
        match: n =>
            !Editor.isEditor(n) &&
            SlateElement.isElement(n) &&
            LIST_TYPES.includes(n.type) &&
            !TEXT_ALIGN_TYPES.includes(format),
        split: true,
    });
    let newProperties: Partial<SlateElement>;
    if (TEXT_ALIGN_TYPES.includes(format)) {
        newProperties = {
            align: isActive ? undefined : format,
        };
    } else {
        newProperties = {
            type: isActive ? 'paragraph' : isList ? 'list-item' : format,
        };
    }
    Transforms.setNodes<SlateElement>(editor, newProperties);

    if (!isActive && isList) {
        const block = { type: format, children: [] };
        Transforms.wrapNodes(editor, block);
    }

    if (format === 'move_left' || format === 'move_right') {
        newProperties = {
            type: format,
        };
        Transforms.setNodes<SlateElement>(editor, newProperties);
    }

    if (format === 'move_left' || format === 'move_right') {
        newProperties = {
            type: format,
        };
        Transforms.setNodes<SlateElement>(editor, newProperties);
    }
};

const toggleMark = (editor, format) => {
    const isActive = isMarkActive(editor, format);

    if (isActive) {
        Editor.removeMark(editor, format);
    } else {
        Editor.addMark(editor, format, true);
    }
};

const isBlockActive = (editor, format, blockType = 'type') => {
    const { selection } = editor;
    if (!selection) {
        return false;
    }

    const [match] = Array.from(
        Editor.nodes(editor, {
            at: Editor.unhangRange(editor, selection),
            match: n =>
                !Editor.isEditor(n) &&
                SlateElement.isElement(n) &&
                n[blockType] === format,
        }),
    );

    return !!match;
};

const isMarkActive = (editor, format) => {
    const marks = Editor.marks(editor);
    return marks ? marks[format] === true : false;
};

const Element = ({ attributes, children, element }) => {
    const style = { textAlign: element.align };
    switch (element.type) {
        case 'block-quote':
            return (
                <blockquote style={style} {...attributes}>
                    {children}
                </blockquote>
            );

        case 'list-item':
            style.marginTop = '10px';
            return (
                <li style={style} {...attributes}>
                    {children}
                </li>
            );
        case 'numbered-list':
            return (
                <ol class="list-decimal ml-6" style={style} {...attributes}>
                    {children}
                </ol>
            );
        case 'bulleted-list':
            return (
                <ul className="list-disc list-inside" style={style} {...attributes}>
                    {children}
                </ul>
            );
        case 'circle-list':
            style.marginLeft = '30px';
            return (
                <ul className="list-[circle]" style={style} {...attributes}>
                    {children}
                </ul>
            );

        case 'image-list':
            return (
                <ul
                    className="list-image-[double_arrow.svg] list-inside"
                    style={style}
                    {...attributes}
                >
                    {children}
                </ul>
            );
        case 'heading-one':
            return (
                <h1 className="text-2xl" style={style} {...attributes}>
                    {children}
                </h1>
            );
        case 'heading-two':
            return (
                <h2 className="text-xl" style={style} {...attributes}>
                    {children}
                </h2>
            );

        case 'heading-three':
            return (
                <h3 className="text-md" style={style} {...attributes}>
                    {children}
                </h3>
            );

        case 'heading-four':
            return (
                <h3 className="text-sm" style={style} {...attributes}>
                    {children}
                </h3>
            );

        case 'move_left':
            // style.paddingRight = '20px';

            return (
                <div style={style} {...attributes}>
                    {children}
                </div>
            );
        case 'move_right':
            // style.paddingLeft = '20px';
            return (
                <div style={style} {...attributes}>
                    {children}
                </div>
            );
        default:
            return (
                <p style={style} {...attributes}>
                    {children}
                </p>
            );
    }
};

const Leaf = ({ attributes, children, leaf }) => {
    if (leaf.bold) {
        children = <strong>{children}</strong>;
    }

    if (leaf.code) {
        children = <code>{children}</code>;
    }

    if (leaf.italic) {
        children = <em>{children}</em>;
    }

    if (leaf.underline) {
        children = <u>{children}</u>;
    }

    if (leaf.code) {
        children = <code>{children}</code>;
    }

    return <span {...attributes}>{children}</span>;
};

const BlockButton = ({ format, icon }) => {
    const editor = useSlate();
    return (
        <Button
            active={isBlockActive(
                editor,
                format,
                TEXT_ALIGN_TYPES.includes(format) ? 'align' : 'type',
            )}
            onMouseDown={event => {
                event.preventDefault();
                toggleBlock(editor, format);
            }}
        >
            <Icon>{icon}</Icon>
        </Button>
    );
};

const MarkButton = ({ format, icon }) => {
    const editor = useSlate();
    return (
        <Button
            active={isMarkActive(editor, format)}
            onMouseDown={event => {
                event.preventDefault();
                toggleMark(editor, format);
            }}
        >
            <Icon>{icon}</Icon>
        </Button>
    );
};

export async function getStaticProps(context) {
    return {
        props: {
            protected: true,
        },
    };
}

export async function getStaticPaths(context) {
    return {
        paths: [],
        fallback: true,
    };
}

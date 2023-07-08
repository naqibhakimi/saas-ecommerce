import { useEffect, useState } from 'react';

type Node = Record<string, unknown>;
type Edges = [
    {
        node: Node[];
    },
];

export function convertEdgeToList(edges: Edges) {
    if (edges){
        return edges.map(edge => edge.node);
    }
    return [];
}

export function classNames(...classes) {
    return classes.filter(Boolean).join(' ');
}

export function truncate(str, n, useWordBoundary) {
    if (str.length <= n) {
        return str;
    }
    const subString = str.slice(0, n - 1); // the original check
    return (
        (useWordBoundary
            ? subString.slice(0, subString.lastIndexOf(' '))
            : subString) + '...'
    );
}

export function useWindowSize(cardRef) {
    const [windowSize, setWindowSize] = useState({
        width: undefined,
        height: undefined,
    });

    useEffect(() => {
        function handleResize() {
            setWindowSize({
                width: cardRef.current?.offsetWidth,
                height: cardRef.current?.offsetHeight,
            });
        }
        window.addEventListener('resize', handleResize);

        const interval = setInterval(() => {
            handleResize();
        }, 200);

        if (windowSize?.width > 10) {
            clearInterval(interval);
        }

        // Remove event listener on cleanup
        return () => {
            clearInterval(interval);
            window.removeEventListener('resize', handleResize);
        };
    }, [cardRef?.current]); // Empty array ensures that effect is only run on mount
    return windowSize;
}

const parseHeaders = (rawHeaders: string) => {
    const headers = new Headers();
    const preProcessedHeaders = rawHeaders.replace(/\r?\n[\t ]+/g, ' ');
    preProcessedHeaders.split(/\r?\n/).forEach((line: string) => {
        const parts: string[] = line.split(':');
        const key: string | undefined = parts.shift().trim();
        if (key) {
            const value = parts.join(':').trim();
            headers.append(key, value);
        }
    });
    return headers;
};

export const uploadFetch = (url: string, options: Record<string, any>) =>
    new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.onload = () => {
            const opts: Record<string, any> = {
                status: xhr.status,
                statusText: xhr.statusText,
                headers: parseHeaders(xhr.getAllResponseHeaders() || ''),
            };
            opts.url =
                'responseURL' in xhr
                    ? xhr.responseURL
                    : opts.headers.get('X-Request-URL');
            const body =
                'response' in xhr ? xhr.response : (xhr as any).responseText;
            resolve(new Response(body, opts));
        };
        xhr.onerror = () => {
            reject(new TypeError('Network request failed'));
        };
        xhr.ontimeout = () => {
            reject(new TypeError('Network request failed'));
        };
        xhr.open(options.method, url, true);

        Object.keys(options.headers).forEach(key => {
            xhr.setRequestHeader(key, options.headers[key]);
        });

        if (xhr.upload) {
            xhr.upload.onprogress = options.onProgress;
        }

        options.onAbortPossible(() => {
            xhr.abort();
        });

        xhr.send(options.body);
    });

export const customFetch = (uri: string, options: Record<string, any>) => {
    if (options.useUpload) {
        return uploadFetch(uri, options);
    }
    return fetch(uri, options);
};

export const debounce = (func, wait, immediate) => {
    let timeout;
    return  () => {
        const context = this,
            args = arguments;
        const later = function () {
            timeout = null;
            if (!immediate) {
                func.apply(context, args);
            }
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) {
            func.apply(context, args);
        }
    };
}

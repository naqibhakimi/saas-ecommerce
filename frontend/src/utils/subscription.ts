import client from '@/services/apolloClient';
import { FetchResult, SubscriptionOptions } from '@apollo/client';
import { useEffect, useState } from 'react';

export const useSubscription = (options: SubscriptionOptions): [unknown] => {
    const [data, setData] = useState({
        data: undefined,
        loading: false,
        extensions: undefined,
        context: undefined,
    });

    useEffect(() => {
        client
            .subscribe(options)
            .subscribe((res: Partial<FetchResult>) => setData(res));
    }, [data, setData]);

    return [data];
};

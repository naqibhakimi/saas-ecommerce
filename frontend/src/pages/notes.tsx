import ListMeetings from '@/components/listMeetings';

import Layout from '@/components/layout/Layout';

import Breadcrumbs from '@/components/Breadcrumbs';
import { useQuery } from '@apollo/client';
import { _MEETINGS } from '@/services/meeting';
export default function Index() {
    const { data, error, loading } = useQuery(_MEETINGS);

    if (loading) {
        return (
            <Layout>
                <></>
            </Layout>
        );
    }

    if (error) {
        return (
            <Layout>
                <></>
            </Layout>
        );
    }

    return (
        <>
            <Layout>
                <Breadcrumbs title="Notes" />
                <ListMeetings meetings={data?.Meetings?.edges}></ListMeetings>
            </Layout>
        </>
    );
}

export async function getStaticProps() {
    return {
        props: {
            protected: true,
        },
    };
}

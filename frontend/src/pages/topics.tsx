import ListTopics from '@/components/listTopic';

import Layout from '@/components/layout/Layout';

import Breadcrumbs from '@/components/Breadcrumbs';
export default function Index() {
    return (
        <>
            <Layout>
            <Breadcrumbs title="Topics" />
                <ListTopics></ListTopics>
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

import ListTopics from '@/components/listTopic';

import Layout from '@/components/layout/Layout';

import Breadcrumbs from '@/components/Breadcrumbs';
export default function Index() {
    return (
        <>
            <Layout>
            <Breadcrumbs title="Home" />
                <h2>Welcome Home!</h2>
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

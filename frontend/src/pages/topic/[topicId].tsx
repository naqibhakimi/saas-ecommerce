import Topic from '@/components/topic';

import Layout from '@/components/layout/Layout';

export default function Index() {
    return (
        <>
            <Layout>
                <Topic></Topic>
            </Layout>
        </>
    );
}

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

import type { CodegenConfig } from '@graphql-codegen/cli';

const config: CodegenConfig = {
    overwrite: true,
    schema: 'http://backend/graphql/',
    documents: 'src/**/*.ts',
    generates: {
        './src/types/graphql.ts': {
            plugins: ['typescript'],
        },
    },
    hooks: {
        afterAllFileWrite: ['prettier --write'],
    },
};

export default config;

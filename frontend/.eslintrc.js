const prettierConfig = require('./.prettierrc.js');

module.exports = {
    env: {
        browser: true,
        commonjs: true,
        es2021: true,
        node: true,
    },
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'plugin:react-hooks/recommended',
        'plugin:prettier/recommended',
        'plugin:@typescript-eslint/eslint-recommended',
        'plugin:@typescript-eslint/recommended',
        'next/core-web-vitals',
    ],
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 12,
        sourceType: 'module',
    },
    plugins: ['react'],
    rules: {
        // Possible warns
        'no-console': 'warn',
        // Best practices
        'dot-notation': 'warn',
        'no-else-return': 'warn',
        'no-floating-decimal': 'warn',
        'no-sequences': 'warn',
        // Stylistic
        'array-bracket-spacing': 'warn',
        'computed-property-spacing': ['warn', 'never'],
        curly: 'warn',
        'no-lonely-if': 'warn',
        'no-unneeded-ternary': 'warn',
        'one-var-declaration-per-line': 'warn',
        quotes: [
            'warn',
            'single',
            {
                allowTemplateLiterals: false,
                avoidEscape: true,
            },
        ],
        // ES6
        'array-callback-return': 'off',
        'prefer-const': 'warn',
        // Imports
        'import/prefer-default-export': 'off',
        'sort-imports': [
            'warn',
            {
                ignoreCase: true,
                ignoreDeclarationSort: true,
            },
        ],
        'no-unused-expressions': 'off',
        'no-prototype-builtins': 'off',
        // REACT
        'react/jsx-uses-react': 'off',
        'react/react-in-jsx-scope': 'off',
        'jsx-a11y/href-no-hash': [0],
        'react/display-name': 0,
        'react/no-deprecated': 'warn',
        'react/no-unsafe': [
            'warn',
            {
                checkAliases: true,
            },
        ],
        'react/jsx-sort-props': [
            'warn',
            {
                ignoreCase: true,
            },
        ],
        'react-hooks/rules-of-hooks': 'warn',
        'react-hooks/exhaustive-deps': 0,
        // Prettier
        // eslint looks for the prettier config at the top level of the package/app
        // but the config lives in the `config/` directory. Passing the config here
        // to get around this.
        'prettier/prettier': ['warn', prettierConfig],
    },
    settings: {
        react: {
            version: 'detect',
        },
    },
};

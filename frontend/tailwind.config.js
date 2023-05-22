const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
    content: ['./src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Open Sans', ...defaultTheme.fontFamily.sans],
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('tailwind-scrollbar-hide'),
    ],
};

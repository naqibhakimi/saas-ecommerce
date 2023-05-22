/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
    experimental: {
        appDir: false,
    },
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'tailwindui.com',
                port: '',
                pathname: '/**',
            },
        ],
    },
    typescript: {
        // !! WARN !!
        // Dangerously allow production builds to successfully complete even if
        // your project has type errors.
        // !! WARN !!
        ignoreBuildErrors: true,
    },

    eslint: {
        // Warning: This allows production builds to successfully complete even if
        // your project has ESLint errors.
        ignoreDuringBuilds: true,
    },
};

module.exports = nextConfig;

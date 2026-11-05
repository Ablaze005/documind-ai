import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{js,ts,jsx,tsx,mdx}', './components/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        slate: {
          950: '#020817'
        }
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(148,163,184,0.2), 0 10px 30px rgba(15,23,42,0.35)'
      }
    }
  },
  plugins: []
};

export default config;

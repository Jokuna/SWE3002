// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/eslint'
  ],
  plugins: ['~/plugins/vuex.js'],
  tailwindcss: {
    cssPath: ['~/assets/css/tailwind.css', { injectPosition: "first" }],
    configPath: 'tailwind.config',
    exposeConfig: {
      level: 2
    },
    config: {},
    viewer: true,
  },
  nitro: {
    routeRules: {
      "/backend/**": {
        proxy: process.env.NODE_ENV === 'development' ? "http://localhost:8000/backend/**" : "",
      },
    },
  },
  experimental: { appManifest: false },
})

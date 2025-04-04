// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	srcDir: 'app',
	compatibilityDate: '2024-11-01',
	devtools: { enabled: true },
	modules: [
		'@nuxtjs/tailwindcss',
		'@nuxtjs/color-mode',
		'@vee-validate/nuxt',
		'@pinia/nuxt',
		'pinia-plugin-persistedstate',
		'@nuxt/eslint',
	],
	colorMode: {
		preference: 'system',
		fallback: 'dark',
		dataValue: 'theme',
	},
	components: [
		{
			path: '~/components',
		},
		{
			path: '~/components/ui',
			pathPrefix: false,
		},
	],
	piniaPluginPersistedstate: {
		storage: 'cookies',
		cookieOptions: {
			sameSite: 'lax',
		},
	},
})

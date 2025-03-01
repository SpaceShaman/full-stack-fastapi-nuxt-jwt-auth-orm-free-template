export default defineNuxtPlugin(() => {
	return {
		provide: {
			api: createAPI('/api', 'backend', 8000),
		},
	}
})

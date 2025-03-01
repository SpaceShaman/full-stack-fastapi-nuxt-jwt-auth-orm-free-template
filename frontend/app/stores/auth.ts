export const useAuthStore = defineStore('auth', {
	persist: true,
	state: () => ({
		authenticated: false,
		token: '',
	}),
})

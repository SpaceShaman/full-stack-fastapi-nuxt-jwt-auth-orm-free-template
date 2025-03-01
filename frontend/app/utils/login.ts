export default async function login(username: string, password: string) {
	await useNuxtApp().$api<{ token: string }>('/auth/login', {
		method: 'POST',
		body: { username, password },
		onResponse: ({ response }) => {
			if (response.ok) {
				const authStore = useAuthStore()
				authStore.token = response._data.access_token
				authStore.authenticated = true
				showSuccessAlert('Logged in successfully')
				navigateTo('/')
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 401) {
				showErrorAlert('Invalid username or password')
			} else if (response.status === 403) {
				showErrorAlert('Account is not activated, please check your email')
			}
		},
	})
}

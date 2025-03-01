export default async function logout() {
	const authStore = useAuthStore()
	authStore.token = ''
	authStore.authenticated = false
	await navigateTo('/login')
}

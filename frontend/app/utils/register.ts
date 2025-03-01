export default async function register(
	username: string,
	email: string,
	password: string
) {
	await useNuxtApp().$api('/auth/register', {
		method: 'POST',
		body: { username, email, password },
		onResponse: ({ response }) => {
			if (response.ok) {
				showSuccessAlert(
					'Account created successfully, go to your email to activate it'
				)
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 403) {
				showErrorAlert('Username or email already exists')
			} else {
				showErrorAlert('An error occurred')
			}
		},
	})
	await navigateTo('/')
}

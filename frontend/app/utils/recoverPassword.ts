export default async function recoverPassword(
	code: string,
	newPassword: string
) {
	await useNuxtApp().$api(`/users/auth/recover/${code}`, {
		method: 'POST',
		body: { new_password: newPassword },
		onResponse: ({ response }) => {
			if (response.ok) {
				showSuccessAlert('Password changed successfully')
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 401) {
				showErrorAlert('Incorrect password')
			} else {
				showErrorAlert('The password could not be changed')
			}
		},
	})
	await navigateTo('/')
}

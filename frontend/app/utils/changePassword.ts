export default async function changePassword(
	oldPassword: string,
	newPassword: string
) {
	await useNuxtApp().$api('/auth/change-password', {
		method: 'POST',
		body: { old_password: oldPassword, new_password: newPassword },
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

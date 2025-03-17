export default async function activateAccount(activationCode: string) {
	await useNuxtApp().$api(`/users/auth/activate/${activationCode}`, {
		method: 'GET',
		onResponse: ({ response }) => {
			if (response.ok) {
				showSuccessAlert('Account activated successfully')
				navigateTo('/login')
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 400) {
				showErrorAlert('Invalid activation code')
			} else {
				showErrorAlert('Failed to activate account')
			}
			navigateTo('/login')
		},
	})
}

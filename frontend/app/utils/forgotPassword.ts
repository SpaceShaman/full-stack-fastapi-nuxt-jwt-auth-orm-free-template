export default async function forgotPassword(email: string) {
	await useNuxtApp().$api<{ token: string }>('/auth/forgot-password', {
		method: 'POST',
		body: { email },
		onResponse: ({ response }) => {
			if (response.ok) {
				showSuccessAlert('Password reset email sent')
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 404) {
				showErrorAlert('Email not found')
			}
		},
	})
}

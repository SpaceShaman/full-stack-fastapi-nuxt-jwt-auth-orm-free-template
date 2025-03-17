export default async function forgotPassword(email: string) {
	await useNuxtApp().$api<{ token: string }>('/users/auth/recover', {
		method: 'POST',
		body: { email },
		onResponse: ({ response }) => {
			if (response.ok) {
				showSuccessAlert('Password reset email sent')
			}
		},
		onResponseError: ({ response }) => {
			if (response.status === 403) {
				showErrorAlert('Email not found')
			}
		},
	})
}

<script setup lang="ts">
	const { code } = defineProps<{
		code: string
	}>()
	const { errors, handleSubmit, defineField } = useForm({
		validationSchema: recoverPasswordSchema,
	})

	const loading = ref(false)

	const [password] = defineField('password')
	const [passwordConfirmation] = defineField('passwordConfirmation')

	const submit = handleSubmit(async (value) => {
		loading.value = true
		try {
			await recoverPassword(code, value.password)
		} finally {
			loading.value = false
		}
	})
</script>
<template>
	<form class="card-body" @submit.prevent="submit">
		<div class="form-control">
			<PasswordInput
				v-model="password"
				:error-message="errors.password"
				placeholder="New Password"
				:disabled="loading"
			/>
			<PasswordInput
				v-model="passwordConfirmation"
				:error-message="errors.passwordConfirmation"
				placeholder="Password confirmation"
				:disabled="loading"
			/>
		</div>
		<Button text="Recover Password" :disabled="loading" />
	</form>
</template>

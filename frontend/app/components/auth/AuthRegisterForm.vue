<script setup lang="ts">
	const { errors, handleSubmit, defineField } = useForm({
		validationSchema: registerSchema,
	})

	const loading = ref(false)

	const [username] = defineField('username')
	const [email] = defineField('email')
	const [password] = defineField('password')
	const [passwordConfirmation] = defineField('passwordConfirmation')

	const submit = handleSubmit(async (value) => {
		loading.value = true
		try {
			await register(value.username, value.email, value.password)
		} finally {
			loading.value = false
		}
	})
</script>
<template>
	<form class="card-body" @submit.prevent="submit">
		<progress v-if="loading" class="progress mb-3" />
		<div class="form-control">
			<UsernameInput
				v-model="username"
				:error-message="errors.username"
				:disabled="loading"
			/>
		</div>
		<div class="form-control">
			<EmailInput
				v-model="email"
				:error-message="errors.email"
				:disabled="loading"
			/>
		</div>
		<div class="form-control">
			<PasswordInput
				v-model="password"
				:error-message="errors.password"
				:disabled="loading"
			/>
		</div>
		<div class="form-control">
			<PasswordInput
				v-model="passwordConfirmation"
				:error-message="errors.passwordConfirmation"
				placeholder="Password confirmation"
				:disabled="loading"
			/>
		</div>
		<Button text="Register" :disabled="loading" />
	</form>
</template>

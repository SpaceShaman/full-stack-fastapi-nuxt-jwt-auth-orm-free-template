<script setup lang="ts">
	const { errors, handleSubmit, defineField } = useForm({
		validationSchema: loginSchema,
	})

	const loading = ref(false)

	const [username] = defineField('username')
	const [password] = defineField('password')

	const submit = handleSubmit(async (value) => {
		loading.value = true
		try {
			await login(value.username, value.password)
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
			<PasswordInput
				v-model="password"
				:error-message="errors.password"
				:disabled="loading"
			/>
			<div class="label">
				<span />
				<span
					class="link-hover link label-text-alt"
					@click="$emit('forgot-password')"
				>
					Forgot password?
				</span>
			</div>
		</div>
		<Button text="Login" :disabled="loading" />
	</form>
</template>

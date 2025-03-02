<script setup lang="ts">
	const { errors, handleSubmit, defineField } = useForm({
		validationSchema: forgotPasswordSchema,
	})

	const loading = ref(false)

	const [email] = defineField('email')

	const submit = handleSubmit(async (value) => {
		loading.value = true
		try {
			await forgotPassword(value.email)
		} finally {
			loading.value = false
		}
	})
</script>
<template>
	<form class="card-body" @submit.prevent="submit">
		<progress v-if="loading" class="progress mb-3" />
		<div class="form-control">
			<EmailInput
				v-model="email"
				:error-message="errors.email"
				:disabled="loading"
			/>
		</div>
		<Button text="Send reset link" :disabled="loading" />
	</form>
</template>

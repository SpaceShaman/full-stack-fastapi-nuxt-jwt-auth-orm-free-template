<script setup lang="ts">
	const { code } = defineProps<{
		code: string
	}>()
	const { errors, handleSubmit, defineField } = useForm({
		validationSchema: recoverPasswordSchema,
	})

	const loading = ref(false)

	const [newPassword] = defineField('newPassword')

	const submit = handleSubmit(async (value) => {
		loading.value = true
		try {
			await recoverPassword(code, value.newPassword)
		} finally {
			loading.value = false
		}
	})
</script>
<template>
	<form class="card-body" @submit.prevent="submit">
		<div class="form-control">
			<PasswordInput
				v-model="newPassword"
				:error-message="errors.newPassword"
				placeholder="New Password"
				:disabled="loading"
			/>
		</div>
		<Button text="Recover Password" :disabled="loading" />
	</form>
</template>

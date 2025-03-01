<script setup lang="ts">
	const forgotPasswordTab = ref(false)
</script>
<template>
	<Tablist>
		<TablistItem label="Login" checked @click="forgotPasswordTab = false">
			<AuthLoginForm
				v-if="!forgotPasswordTab"
				@forgot-password="forgotPasswordTab = true"
			/>
			<AuthForgotPasswordForm v-else />
		</TablistItem>
		<TablistItem label="Register" @click="forgotPasswordTab = false">
			<AuthRegisterForm />
		</TablistItem>
	</Tablist>
</template>

<script setup lang="ts">
	definePageMeta({
		layout: 'unlogged',
	})
	useHead({
		title: 'Recover your account',
	})
	const { recoverCode } = useRoute().params
	const code = Array.isArray(recoverCode) ? recoverCode[0] : recoverCode
</script>
<template>
	<Hero>
		<Article>
			<AuthRecoverPasswordForm :code="code" />
		</Article>
	</Hero>
</template>

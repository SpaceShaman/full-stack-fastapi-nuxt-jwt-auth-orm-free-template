<script setup lang="ts">
	defineProps<{
		alert: Alert
	}>()
</script>
<template>
	<div
		role="alert"
		class="alert"
		:class="{
			'alert-success': alert.type === 'success',
			'alert-error': alert.type === 'error',
			'alert-warning': alert.type === 'warning',
			'alert-info': alert.type === 'info',
		}"
	>
		<p />
		<span>{{ alert.message }}</span>
		<CloseButton @click="$emit('close')" />
	</div>
</template>

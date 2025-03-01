<script setup lang="ts">
	const { alerts } = useAlertsStore()
</script>

<template>
	<div class="toast toast-center toast-top z-50">
		<Alert
			v-for="alert in alerts"
			:key="alert.id"
			:alert="alert"
			@close="alerts.splice(alerts.indexOf(alert), 1)"
		/>
	</div>
</template>

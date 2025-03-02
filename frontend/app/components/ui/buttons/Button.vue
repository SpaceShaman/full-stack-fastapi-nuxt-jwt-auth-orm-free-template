<script setup lang="ts">
	defineProps({
		text: String,
		disabled: {
			type: Boolean,
			default: false,
		},
	})
</script>
<template>
	<button class="btn btn-primary" :disabled="disabled">{{ text }}</button>
</template>

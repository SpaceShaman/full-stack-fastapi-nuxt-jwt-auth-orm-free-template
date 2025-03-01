<script setup lang="ts">
	defineProps({
		text: String,
	})
</script>
<template>
	<button class="btn btn-primary">{{ text }}</button>
</template>

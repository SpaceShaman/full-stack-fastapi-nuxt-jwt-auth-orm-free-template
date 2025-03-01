<script setup lang="ts">
	defineEmits(['click'])
</script>
<template>
	<button class="btn btn-circle btn-outline btn-xs" @click="$emit('click')">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class="h-4 w-4 shrink-0 stroke-current"
			fill="none"
			viewBox="0 0 24 24"
			stroke="currentColor"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2.5"
				d="M6 18L18 6M6 6l12 12"
			/>
		</svg>
	</button>
</template>

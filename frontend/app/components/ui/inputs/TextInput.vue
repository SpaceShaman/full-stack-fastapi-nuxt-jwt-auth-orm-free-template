<script setup lang="ts">
	const value = defineModel<string>()
	defineProps({
		placeholder: String,
		type: {
			type: String,
			default: 'text',
		},
		errorMessage: String,
		disabled: {
			type: Boolean,
			default: false,
		},
	})
</script>
<template>
	<label
		class="input input-bordered flex items-center gap-2"
		:class="{ 'input-error': errorMessage }"
	>
		<slot name="prepend-icon"></slot>
		<input
			v-model="value"
			:type="type"
			class="grow"
			:placeholder="placeholder"
			:disabled="disabled"
		/>
	</label>
	<div class="label">
		<span class="label-text-alt text-error">{{ errorMessage }}</span>
	</div>
</template>

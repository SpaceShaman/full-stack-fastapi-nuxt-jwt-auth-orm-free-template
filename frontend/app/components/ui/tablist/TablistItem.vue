<script setup lang="ts">
	defineProps({
		label: String,
		checked: {
			type: Boolean,
			default: false,
		},
		tabsGroup: {
			type: String,
			default: 'tabs',
		},
	})
	defineEmits(['click'])
</script>
<template>
	<input
		type="radio"
		:name="tabsGroup"
		role="tab"
		class="tab"
		:aria-label="label"
		:checked="checked"
		@click="$emit('click')"
	/>
	<div
		role="tabpanel"
		class="tab-content rounded-box border-base-300 bg-base-100 shadow-2xl"
	>
		<slot />
	</div>
</template>

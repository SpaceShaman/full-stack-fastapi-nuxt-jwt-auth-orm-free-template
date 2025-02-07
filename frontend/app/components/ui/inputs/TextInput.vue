<script setup lang="ts">
const value = defineModel<string>();
defineProps({
  placeholder: String,
  type: {
    type: String,
    default: "text",
  },
  errorMessage: String,
});
</script>
<template>
  <label class="input input-bordered flex items-center gap-2">
    <slot name="prepend-icon"></slot>
    <input
      :type="type"
      class="grow"
      :class="{ 'input-error': errorMessage }"
      :placeholder="placeholder"
      :value="value"
    />
    <div class="label">
      <span class="label-text-alt">{{ errorMessage }}</span>
    </div>
  </label>
</template>

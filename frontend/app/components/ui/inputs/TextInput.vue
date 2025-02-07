<script setup lang="ts">
const value = defineModel<string>();
defineProps({
  placeholder: String,
  type: {
    type: String,
    default: "text",
  },
});
</script>
<template>
  <label class="input input-bordered flex items-center gap-2">
    <slot name="prepend-icon"></slot>
    <input
      :type="type"
      class="grow"
      :placeholder="placeholder"
      :value="value"
    />
  </label>
</template>

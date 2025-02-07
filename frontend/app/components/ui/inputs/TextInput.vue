<script setup lang="ts">
const value = defineModel<string>();
defineProps({
  placeholder: String,
});
</script>
<template>
  <label class="input input-bordered flex items-center gap-2">
    <slot name="prepend-icon"></slot>
    <input type="text" class="grow" :placeholder="placeholder" :value="value" />
  </label>
</template>

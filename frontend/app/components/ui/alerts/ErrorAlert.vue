<script setup lang="ts">
defineProps<{
  message: string;
}>();
</script>
<template>
  <div role="alert" class="alert alert-error">
    <p />
    <span>{{ message }}</span>
    <CloseButton @click="$emit('close')" />
  </div>
</template>

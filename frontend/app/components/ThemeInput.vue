<script setup lang="ts">
defineProps<{ name: string }>();
</script>

<template>
  <li>
    <input
      type="radio"
      name="theme-dropdown"
      class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
      :aria-label="name.charAt(0).toUpperCase() + name.slice(1)"
      :value="name"
    />
  </li>
</template>

<script setup lang="ts">
const { data } = useAPI("/test");
</script>
<template>
  {{ data }}
  <ThemeSelector class="absolute top-1 right-2" />
  <NuxtLayout>
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "unlogged",
});
useHead({
  title: "Login Page",
});
</script>
<template>
  <Hero>
    <AuthTabs />
    <template #contentRight>
      <AuthAbout class="ml-8" />
    </template>
  </Hero>
</template>

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
      <AuthAbout />
    </template>
  </Hero>
</template>

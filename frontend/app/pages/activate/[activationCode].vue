<script setup lang="ts">
definePageMeta({
  layout: "unlogged",
});
useHead({
  title: "Account Activation",
});
const { activationCode } = useRoute().params;
const code = Array.isArray(activationCode) ? activationCode[0] : activationCode;

onMounted(async () => {
  await activateAccount(code);
});
</script>
<template>
  <Hero>
    <Prose>
      <h1>Activating account...</h1>
    </Prose>
  </Hero>
</template>

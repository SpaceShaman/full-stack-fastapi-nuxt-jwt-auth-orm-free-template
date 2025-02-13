<script setup lang="ts">
definePageMeta({
  layout: "unlogged",
});
useHead({
  title: "Account Activation",
});

const { activationCode } = useRoute().params;
</script>
<template>Acount activation {{ activationCode }}</template>

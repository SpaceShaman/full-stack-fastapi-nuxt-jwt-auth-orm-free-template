<script setup lang="ts">
const email = ref<string>();
</script>
<template>
  <form class="card-body">
    <div class="form-control">
      <EmailInput v-model="email" />
    </div>
    <Button text="Send reset link" />
  </form>
</template>

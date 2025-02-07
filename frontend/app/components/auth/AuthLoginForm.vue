<script setup lang="ts">
const username = ref<string>();
const password = ref<string>();
</script>
<template>
  <form class="card-body">
    <div class="form-control">
      <UsernameInput v-model="username" />
    </div>
    <div class="form-control">
      <PasswordInput v-model="password" />
      <div class="label">
        <span />
        <span
          class="label-text-alt link link-hover"
          @click="$emit('forgot-password')"
          >Forgot password?</span
        >
      </div>
    </div>
    <Button text="Login" />
  </form>
</template>

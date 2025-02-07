<script setup lang="ts">
const username = ref<string>();
const password = ref<string>();
const email = ref<string>();
const passwordConfirmation = ref<string>();
</script>
<template>
  <form class="card-body">
    <div class="form-control">
      <UsernameInput v-model="username" />
    </div>
    <div class="form-control">
      <EmailInput v-model="email" />
    </div>
    <div class="form-control">
      <PasswordInput v-model="password" />
    </div>
    <div class="form-control">
      <PasswordInput
        v-model="passwordConfirmation"
        placeholder="Password confirmation"
      />
    </div>
    <button class="btn btn-primary">Register</button>
  </form>
</template>

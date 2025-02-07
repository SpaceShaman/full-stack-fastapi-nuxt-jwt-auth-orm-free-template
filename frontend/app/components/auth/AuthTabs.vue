<script setup lang="ts">
const forgotPasswordTab = ref(false);
</script>
<template>
  <div role="tablist" class="w-full max-w-sm tabs tabs-lifted">
    <input
      type="radio"
      name="tabs"
      role="tab"
      class="tab"
      aria-label="Login"
      checked
      @click="forgotPasswordTab = false"
    />
    <div
      role="tabpanel"
      class="tab-content bg-base-100 border-base-300 rounded-box shadow-2xl"
    >
      <AuthLoginForm
        v-if="!forgotPasswordTab"
        @forgot-password="forgotPasswordTab = true"
      />
      <AuthForgotPasswordForm v-else />
    </div>

    <input
      type="radio"
      name="tabs"
      role="tab"
      class="tab"
      aria-label="Register"
      @click="forgotPasswordTab = false"
    />
    <div
      role="tabpanel"
      class="tab-content bg-base-100 border-base-300 rounded-box shadow-2xl"
    >
      <AuthRegisterForm />
    </div>
  </div>
</template>

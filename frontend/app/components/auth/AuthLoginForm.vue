<script setup lang="ts">
const { errors, handleSubmit, defineField } = useForm({
  validationSchema: loginSchema,
});

const [username] = defineField("username");
const [password] = defineField("password");

const submit = handleSubmit(async (value) => {
  try {
    await login(value.username, value.password);
  } catch (statusCode) {
    if (statusCode === 401) {
      showErrorAlert("Invalid username or password");
    } else {
      showErrorAlert("An error occurred");
    }
  }
});
</script>
<template>
  <form class="card-body" @submit.prevent="submit">
    <div class="form-control">
      <UsernameInput v-model="username" :error-message="errors.username" />
    </div>
    <div class="form-control">
      <PasswordInput v-model="password" :error-message="errors.password" />
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

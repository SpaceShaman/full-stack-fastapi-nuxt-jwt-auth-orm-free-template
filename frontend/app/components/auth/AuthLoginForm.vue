<script setup lang="ts">
import * as yup from "yup";

const { errors, handleSubmit, defineField } = useForm({
  validationSchema: yup.object().shape({
    username: yup
      .string()
      .min(3, "Username must be at least 3 characters")
      .required("Username is required"),
    password: yup
      .string()
      .min(8, "Password must be at least 8 characters")
      .matches(
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/,
        "Password is weak"
      )
      .required("Password is required"),
  }),
});

const [username] = defineField("username");
const [password] = defineField("password");

const submit = handleSubmit(async (value) => {
  console.log(value);
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

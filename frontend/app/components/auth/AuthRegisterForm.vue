<script setup lang="ts">
const { errors, handleSubmit, defineField } = useForm({
  validationSchema: registerSchema,
});

const [username] = defineField("username");
const [email] = defineField("email");
const [password] = defineField("password");
const [passwordConfirmation] = defineField("passwordConfirmation");

const errorMessage = ref();

const submit = handleSubmit(async (value) => {
  try {
    await register(value.username, value.email, value.password);
  } catch (statusCode) {
    if (statusCode === 403) {
      errorMessage.value = "Username or email already exists";
    } else {
      errorMessage.value = "An error occurred";
    }
  }
});
</script>
<template>
  <form class="card-body" @submit.prevent="submit">
    <ErrorAlert
      v-if="errorMessage"
      :message="errorMessage"
      @close="errorMessage = null"
    />
    <div class="form-control">
      <UsernameInput v-model="username" :error-message="errors.username" />
    </div>
    <div class="form-control">
      <EmailInput v-model="email" :error-message="errors.email" />
    </div>
    <div class="form-control">
      <PasswordInput v-model="password" :error-message="errors.password" />
    </div>
    <div class="form-control">
      <PasswordInput
        v-model="passwordConfirmation"
        :error-message="errors.passwordConfirmation"
        placeholder="Password confirmation"
      />
    </div>
    <Button text="Register" />
  </form>
</template>

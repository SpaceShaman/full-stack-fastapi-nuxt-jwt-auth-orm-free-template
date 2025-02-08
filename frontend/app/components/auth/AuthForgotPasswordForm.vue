<script setup lang="ts">
const { errors, handleSubmit, defineField } = useForm({
  validationSchema: forgotPasswordSchema,
});

const [email] = defineField("email");

const submit = handleSubmit(async (value) => {
  showInfoAlert("Reset link sent to your email");
});
</script>
<template>
  <form class="card-body" @submit.prevent="submit">
    <div class="form-control">
      <EmailInput v-model="email" :error-message="errors.email" />
    </div>
    <Button text="Send reset link" />
  </form>
</template>

<script setup lang="ts">
const { errors, handleSubmit, defineField } = useForm({
  validationSchema: changePasswordSchema,
});

const [oldPassword] = defineField("oldPassword");
const [newPassword] = defineField("newPassword");

const submit = handleSubmit(async (value) => {});
</script>
<template>
  <form class="card-body" @submit.prevent="submit">
    <div class="form-control">
      <PasswordInput
        v-model="oldPassword"
        :error-message="errors.oldPassword"
        placeholder="Old Password"
      />
    </div>
    <div class="form-control">
      <PasswordInput
        v-model="newPassword"
        :error-message="errors.newPassword"
        placeholder="New Password"
      />
    </div>
    <Button text="Change Password" />
  </form>
</template>

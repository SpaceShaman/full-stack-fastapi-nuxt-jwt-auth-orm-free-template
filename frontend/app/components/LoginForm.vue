<template>
  <form class="card-body">
    <div class="form-control">
      <label class="label">
        <span class="label-text">Username</span>
      </label>
      <input
        type="text"
        placeholder="Username"
        class="input input-bordered"
        required
      />
    </div>
    <div class="form-control">
      <label class="label">
        <span class="label-text">Password</span>
      </label>
      <input
        type="password"
        placeholder="Password"
        class="input input-bordered"
        required
      />
      <div
        class="label-text-alt link link-hover pt-2"
        @click="$emit('forgot-password')"
      >
        Forgot password?
      </div>
    </div>
    <div class="form-control mt-4">
      <button class="btn btn-primary">Login</button>
    </div>
  </form>
</template>

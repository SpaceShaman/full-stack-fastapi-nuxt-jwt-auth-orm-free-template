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
        placeholder="password"
        class="input input-bordered"
        required
      />
      <label class="label">
        <a href="#" class="label-text-alt link link-hover">Register</a>
      </label>
    </div>
    <div class="form-control mt-6">
      <button class="btn btn-primary">Login</button>
    </div>
  </form>
</template>

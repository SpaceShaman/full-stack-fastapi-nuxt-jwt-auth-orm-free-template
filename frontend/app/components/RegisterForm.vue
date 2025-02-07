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
        <span class="label-text">Email</span>
      </label>
      <input
        type="email"
        placeholder="Email"
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
    </div>
    <div class="form-control">
      <label class="label">
        <span class="label-text">Confirm Password</span>
      </label>
      <input
        type="password"
        placeholder="password"
        class="input input-bordered"
        required
      />
    </div>
    <div class="form-control mt-6">
      <button class="btn btn-primary">Register</button>
    </div>
  </form>
</template>

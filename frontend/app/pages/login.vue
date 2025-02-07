<template>
  <div class="hero bg-base-200 min-h-screen">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Login now!</h1>
        <p class="py-6">
          I'm a full stack developer living in the milky way, focused much more
          on the backend. I love designing IT systems based on clean
          architecture. My native language is Python and my favorite
          technologies include Django, Django Ninja, Pydantic, Celery, FastAPI,
          Transformers, Marvin, Pytest, Factory Boy, Docker, Docker Compose, and
          I also love creating user interfaces using Nuxt.js. I try to stay up
          to date with all technological innovations and use the latest
          technologies to facilitate work. I am also a fan of TDD and DDD
          methodologies. You can find me on
          <a href="https://github.com/SpaceShaman">GitHub</a>
        </p>
      </div>
      <div class="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
        <form class="card-body">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Email</span>
            </label>
            <input
              type="email"
              placeholder="email"
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
      </div>
    </div>
  </div>
</template>

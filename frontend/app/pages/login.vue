<template>
  <div class="hero bg-base-200 min-h-screen">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <h1 class="text-5xl font-bold">Login now!</h1>
        <p class="py-6">
          Hi, I am SpaceShaman and I have prepared for you this full stack
          aplication template using Fastapi, Nuxt, TailwindCSS, DaisyUI, SQLite,
          JWT authentiation. You can find the source code and more interesting
          projects on my github
          <a href="https://github.com/SpaceShaman">github.com/SpaceShaman</a>
        </p>
      </div>
      <div class="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
        <LoginForm />
      </div>
    </div>
  </div>
</template>

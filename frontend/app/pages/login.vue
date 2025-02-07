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
          <a class="link-hover" href="https://github.com/SpaceShaman"
            >github.com/SpaceShaman</a
          >
        </p>
      </div>

      <div role="tablist" class="w-full max-w-sm shadow-2xl tabs tabs-lifted">
        <input
          type="radio"
          name="tabs"
          role="tab"
          class="tab"
          aria-label="Login"
          checked
        />
        <div
          role="tabpanel"
          class="tab-content bg-base-100 border-base-300 rounded-box p-6"
        >
          <LoginForm />
        </div>

        <input
          type="radio"
          name="tabs"
          role="tab"
          class="tab"
          aria-label="Register"
        />
        <div
          role="tabpanel"
          class="tab-content bg-base-100 border-base-300 rounded-box p-6"
        >
          <RegisterForm />
        </div>
      </div>
    </div>
  </div>
</template>

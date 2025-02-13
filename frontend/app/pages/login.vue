<script setup lang="ts">
definePageMeta({
  layout: "unlogged",
});
useHead({
  title: "Login Page",
});
</script>
<template>
  <Hero>
    <AuthTabs />
    <template #contentRight>
      <article class="prose">
        <h1>Hello, Earthlings 🧑‍🚀</h1>
        <p>
          I'm a full stack developer living in the milky way, focused much more
          on the backend. I love designing IT systems based on clean
          architecture. My native language is Python and my favorite
          technologies include Django, Django Ninja, Pydantic, Celery, FastAPI,
          Transformers, Marvin, Pytest, Factory Boy, Docker, Docker Compose, and
          I also love creating user interfaces using Nuxt.js. I try to stay up
          to date with all technological innovations and use the latest
          technologies to facilitate work. I am also a fan of TDD and DDD
          methodologies.
        </p>
        <p>
          You can find the source code and more interesting projects on my
          github
          <a class="link-hover" href="https://github.com/SpaceShaman"
            >github.com/SpaceShaman</a
          >
        </p>
      </article>
    </template>
  </Hero>
</template>

<script setup lang="ts">
const themes = [
  "light",
  "dark",
  "cupcake",
  "bumblebee",
  "emerald",
  "corporate",
  "synthwave",
  "retro",
  "cyberpunk",
  "valentine",
  "halloween",
  "garden",
  "forest",
  "aqua",
  "lofi",
  "pastel",
  "fantasy",
  "wireframe",
  "black",
  "luxury",
  "dracula",
  "cmyk",
  "autumn",
  "business",
  "acid",
  "lemonade",
  "night",
  "coffee",
  "winter",
  "dim",
  "nord",
  "sunset",
];
</script>
<template>
  <div class="dropdown">
    <div tabindex="0" role="button" class="btn m-1">
      Theme
      <svg
        width="12px"
        height="12px"
        class="inline-block h-2 w-2 fill-current opacity-60"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 2048 2048"
      >
        <path
          d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"
        ></path>
      </svg>
    </div>
    <ul
      tabindex="0"
      class="dropdown-content bg-base-300 rounded-box z-[1] shadow-2xl overflow-y-scroll h-96"
    >
      <li v-for="theme in themes" :key="theme">
        <input
          type="radio"
          name="theme-dropdown"
          class="btn btn-sm btn-block btn-ghost"
          :aria-label="theme.charAt(0).toUpperCase() + theme.slice(1)"
          :value="theme"
          :checked="$colorMode.preference === theme"
          @click="$colorMode.preference = theme"
        />
      </li>
    </ul>
  </div>
</template>

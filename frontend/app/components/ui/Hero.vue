<template>
  <div class="hero bg-base-200 min-h-screen">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left">
        <slot name="contentRight" />
      </div>
      <slot />
    </div>
  </div>
</template>

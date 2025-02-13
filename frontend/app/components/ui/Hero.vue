<template>
  <div class="hero bg-base-200 min-h-screen">
    <div class="hero-content flex-col lg:flex-row-reverse">
      <div class="text-center lg:text-left prose">
        <slot name="contentRight" />
      </div>
      <div class="prose">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  label: String,
  checked: {
    type: Boolean,
    default: false,
  },
  tabsGroup: {
    type: String,
    default: "tabs",
  },
});
</script>
<template>
  <input
    type="radio"
    :name="tabsGroup"
    role="tab"
    class="tab"
    :aria-label="label"
    :checked="checked"
    @click="$emit('click')"
  />
  <div
    role="tabpanel"
    class="tab-content bg-base-100 border-base-300 rounded-box shadow-2xl"
  >
    <slot />
  </div>
</template>

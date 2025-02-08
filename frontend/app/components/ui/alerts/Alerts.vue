<script setup lang="ts">
const { alerts } = useAlertsStore();
</script>

<template>
  <div class="toast toast-top toast-center z-50">
    <Alert
      v-for="(alert, index) in alerts"
      :key="index"
      :alert="alert"
      @close="alerts.splice(index, 1)"
    />
  </div>
</template>

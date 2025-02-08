export const useAlertsStore = defineStore("alerts", () => {
  const alerts = ref<Alert[]>([
    { message: "This is an info alert", type: "info" },
  ]);

  const addAlert = (alert: Alert) => {
    alerts.value.push(alert);
  };

  return {
    alerts,
    addAlert,
  };
});

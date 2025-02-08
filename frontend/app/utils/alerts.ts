function showErrorAlert(message: string) {
  useAlertsStore().addAlert({ message, type: "error" });
}

export { showErrorAlert };

export const useAlertsStore = defineStore('alerts', () => {
	const alerts = ref<Alert[]>([])

	const addAlert = (alert: Alert) => {
		alert.id = Date.now()
		alerts.value.push(alert)
		setTimeout(() => {
			alerts.value.splice(alerts.value.indexOf(alert), 1)
		}, 5000)
	}

	return {
		alerts,
		addAlert,
	}
})

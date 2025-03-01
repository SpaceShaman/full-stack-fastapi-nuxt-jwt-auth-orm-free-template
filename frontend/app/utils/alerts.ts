function showErrorAlert(message: string) {
	useAlertsStore().addAlert({ message, type: 'error' })
}

function showSuccessAlert(message: string) {
	useAlertsStore().addAlert({ message, type: 'success' })
}

function showInfoAlert(message: string) {
	useAlertsStore().addAlert({ message, type: 'info' })
}

function showWarningAlert(message: string) {
	useAlertsStore().addAlert({ message, type: 'warning' })
}

export { showErrorAlert, showInfoAlert, showSuccessAlert, showWarningAlert }

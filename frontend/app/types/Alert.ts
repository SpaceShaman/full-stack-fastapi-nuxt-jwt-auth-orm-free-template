declare global {
	export interface Alert {
		id?: number
		message: string
		type: 'info' | 'success' | 'error' | 'warning'
	}
}

import type { UseFetchOptions } from 'nuxt/app'

export function useAPI<T>(
	url: string | (() => string),
	options: Omit<UseFetchOptions<T> & { $fetch?: any }, '$fetch'> = {}
) {
	return useFetch(url, {
		...options,
		$fetch: useNuxtApp().$api,
	})
}

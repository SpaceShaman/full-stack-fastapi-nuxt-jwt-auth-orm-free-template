export default async function login(username: string, password: string) {
  const { token } = await useNuxtApp().$api<{ token: string }>("/auth/login", {
    method: "POST",
    body: { username, password },
    onResponseError: (r) => {
      throw r.response.status;
    },
  });
  const authStore = useAuthStore();
  authStore.token = token;
  authStore.authenticated = true;
  await navigateTo("/");
}

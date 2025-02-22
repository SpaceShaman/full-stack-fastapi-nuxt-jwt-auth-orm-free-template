export default async function login(username: string, password: string) {
  const { token } = await useNuxtApp().$api<{ token: string }>("/auth/login", {
    method: "POST",
    body: { username, password },
    onResponse: ({ response }) => {
      if (response.ok) {
        showSuccessAlert("Logged in successfully");
        navigateTo("/");
      }
    },
    onResponseError: ({ response }) => {
      if (response.status === 401) {
        showErrorAlert("Invalid username or password");
      } else if (response.status === 403) {
        showErrorAlert("Account is not activated, please check your email");
      }
    },
  });
  const authStore = useAuthStore();
  authStore.token = token;
  authStore.authenticated = true;
  await navigateTo("/");
}

export default async function register(
  username: string,
  email: string,
  password: string
) {
  await useNuxtApp().$api("/auth/register", {
    method: "POST",
    body: { username, email, password },
    onResponseError: (r) => {
      throw r.response.status;
    },
  });
  await navigateTo("/");
}

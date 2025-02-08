export const useAuthStore = defineStore("auth", {
  persist: true,
  state: () => ({
    authenticated: false,
    token: "",
  }),
  actions: {
    async login(username: string, password: string) {
      const { token } = await useNuxtApp().$api<{ token: string }>(
        "/auth/login",
        {
          method: "POST",
          body: { username, password },
          onResponseError: (r) => {
            throw r.response.status;
          },
        }
      );
      this.token = token;
      this.authenticated = true;
      await navigateTo("/");
    },
    async logout() {
      this.token = "";
      this.authenticated = false;
      await navigateTo("/login");
    },
  },
});

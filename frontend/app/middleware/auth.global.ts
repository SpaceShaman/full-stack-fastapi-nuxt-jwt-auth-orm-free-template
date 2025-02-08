export default defineNuxtRouteMiddleware((to) => {
  const { authenticated } = useAuthStore();
  if (!authenticated && to.path !== "/login") {
    return navigateTo("/login");
  }
  if (authenticated && to.path === "/login") {
    return navigateTo("/");
  }
});

export default defineNuxtRouteMiddleware((to) => {
  const { authenticated } = useAuthStore();
  if (!authenticated && !isPublicPath(to.path)) {
    return navigateTo("/login");
  }
  if (authenticated && isPublicPath(to.path)) {
    return navigateTo("/");
  }
});

function isPublicPath(path: string): boolean {
  const publicPaths = ["/login", /^\/activate\/?(\w+)?$/];
  return publicPaths.some((publicPath) => {
    if (typeof publicPath === "string") {
      return path === publicPath;
    }
    return publicPath.test(path);
  });
}

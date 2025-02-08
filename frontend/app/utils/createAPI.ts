export default function createAPI(baseURL: string, host: string, port: number) {
  if (isClientSide() && isDevelopment()) {
    baseURL = `http://${window.location.hostname}:${port}${baseURL}`;
  } else if (isServerSide()) {
    baseURL = `http://${host}:${port}${baseURL}`;
  }
  return $fetch.create({
    baseURL: baseURL,
    onRequest({ options }) {
      const headers = new Headers(options.headers);
      headers.set("Authorization", `Bearer ${useAuthStore().token}`);
      options.headers = headers;
    },

    onResponseError({ response }) {
      handleErrors(response);
    },
  });
}

function isClientSide() {
  return import.meta.client;
}

function isServerSide() {
  return !isClientSide();
}

function isDevelopment() {
  return (
    window.location.hostname.includes("localhost") &&
    window.location.port === "3000"
  );
}

function handleErrors(response: Response) {
  if (response.status === 401) {
    useAuthStore().logout();
  } else if (response.status === 403) {
    displayError(403, "You are not authorized to access this resource.");
  } else {
    displayError(response.status, response.statusText);
  }
}

function displayError(statusCode: number, message: string) {
  if (isClientSide()) {
    throw showError({
      statusCode: statusCode,
      message: message,
      fatal: true,
    });
  } else {
    throw createError({
      statusCode: statusCode,
      message: message,
      fatal: true,
    });
  }
}

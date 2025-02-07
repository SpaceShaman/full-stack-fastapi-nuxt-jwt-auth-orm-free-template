import * as yup from "yup";

const passwordValidator = yup
  .string()
  .min(8, "Password must be at least 8 characters")
  .matches(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/,
    "Password is weak"
  )
  .required("Password is required");

const usernameValidator = yup
  .string()
  .min(3, "Username must be at least 3 characters")
  .required("Username is required");

export { passwordValidator, usernameValidator };

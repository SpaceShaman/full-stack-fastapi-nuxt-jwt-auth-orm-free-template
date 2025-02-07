import * as yup from "yup";

const usernameValidator = yup
  .string()
  .min(3, "Username must be at least 3 characters")
  .required("Username is required");

const emailValidator = yup
  .string()
  .email("Invalid email")
  .required("Email is required");

const passwordValidator = yup
  .string()
  .min(8, "Password must be at least 8 characters")
  .matches(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/,
    "Password is weak"
  )
  .required("Password is required");

export default yup.object().shape({
  username: usernameValidator,
  email: emailValidator,
  password: passwordValidator,
  passwordConfirmation: passwordValidator,
});

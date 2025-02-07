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
  .required("Password is required");

const passwordConfirmationValidator = yup
  .string()
  .oneOf([yup.ref("password")], "Passwords must match")
  .required("Password confirmation is required");

const loginSchema = yup.object().shape({
  username: usernameValidator,
  password: passwordValidator,
});

const registerSchema = yup.object().shape({
  username: usernameValidator,
  email: emailValidator,
  password: passwordValidator,
  passwordConfirmation: passwordConfirmationValidator,
});

const forgotPasswordSchema = yup.object().shape({
  email: emailValidator,
});

export { forgotPasswordSchema, loginSchema, registerSchema };

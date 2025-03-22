import * as yup from 'yup'

const usernameValidator = yup
	.string()
	.min(3, 'Username must be at least 3 characters')
	.required('Username is required')

const emailValidator = yup
	.string()
	.email('Invalid email')
	.required('Email is required')

const passwordValidator = yup
	.string()
	.min(8, 'Password must be at least 8 characters')
	.matches(
		/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})/,
		'Password must contain at least one uppercase letter, one lowercase letter, one number and one special character'
	)
	.required('Password is required')

const passwordConfirmationValidator = yup
	.string()
	.oneOf([yup.ref('password')], 'Passwords must match')
	.required('Password confirmation is required')

const loginSchema = yup.object().shape({
	username: usernameValidator,
	password: passwordValidator,
})

const registerSchema = yup.object().shape({
	username: usernameValidator,
	email: emailValidator,
	password: passwordValidator,
	passwordConfirmation: passwordConfirmationValidator,
})

const forgotPasswordSchema = yup.object().shape({
	email: emailValidator,
})

const recoverPasswordSchema = yup.object().shape({
	password: passwordValidator,
	passwordConfirmation: passwordConfirmationValidator,
})

const changePasswordSchema = yup.object().shape({
	oldPassword: yup.string().required('Old password is required'),
	newPassword: passwordValidator,
})

export {
	changePasswordSchema,
	forgotPasswordSchema,
	loginSchema,
	recoverPasswordSchema,
	registerSchema,
}

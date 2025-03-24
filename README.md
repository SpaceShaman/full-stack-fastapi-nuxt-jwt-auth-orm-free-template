# Full Stack FastAPI Nuxt.js JWT Auth ORM Free Template

[![GitHub License](https://img.shields.io/github/license/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)](https://github.com/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template?tab=MIT-1-ov-file)
[![Tests](https://img.shields.io/github/actions/workflow/status/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template/deploy.yml?label=tests)](https://github.com/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template/blob/master/.github/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)](https://codecov.io/gh/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)
[![Python](https://img.shields.io/badge/language-Python-yellow?logo=python&logoColor=yellow)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/language-TypeScript-yellow?logo=typescript&logoColor=yellow)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/framework-FastAPI-green?logo=fastapi&logoColor=green)](https://fastapi.tiangolo.com/)
[![Nuxt.js](https://img.shields.io/badge/framework-Nuxt-green?logo=nuxt.js&logoColor=green)](https://nuxt.com/)
[![Docker](https://img.shields.io/badge/technology-Docker-blue?logo=docker&logoColor=blue)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/technology-Docker%20Compose-blue?logo=docker&logoColor=blue)](https://docs.docker.com/compose/)
[![Poetry](https://img.shields.io/badge/technology-Poetry-blue?logo=python&logoColor=blue)](https://python-poetry.org)
[![Pydantic](https://img.shields.io/badge/technology-Pydantic-blue?logo=pydantic&logoColor=blue)](https://docs.pydantic.dev)
[![Tailwind CSS](https://img.shields.io/badge/styling-Tailwind%20CSS-blue?logo=tailwind-css&logoColor=blue)](https://tailwindcss.com/)
[![daisyUI](https://img.shields.io/badge/styling-daisyUI-blue?logo=daisyui&logoColor=blue)](https://daisyui.com/)
[![VeeValidate](https://img.shields.io/badge/validation-VeeValidate-blue?logo=vee-validate&logoColor=blue)](https://vee-validate.logaretm.com)
[![Yup](https://img.shields.io/badge/validation-Yup-blue?logo=yup&logoColor=blue)](https://yup-docs.vercel.app/)
[![Jinja](https://img.shields.io/badge/templating-Jinja-blue?logo=jinja&logoColor=blue)](https://jinja.palletsprojects.com/)
[![JWT](https://img.shields.io/badge/authentication-JWT-blue?logo=json-web-tokens&logoColor=blue)](https://jwt.io/)
[![Pytest](https://img.shields.io/badge/testing-Pytest-red?logo=pytest&logoColor=red)](https://docs.pytest.org/)
[![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey?logo=sqlite&logoColor=blue)](https://www.sqlite.org/)
[![SQLift](https://img.shields.io/badge/migration-SQLift-purple)](https://github.com/SpaceShaman/SQLift)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/badge/linting-Ruff-black?logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff)
[![Code formatter: Prettier](https://img.shields.io/badge/code%20formatter-Prettier-ff69b4)](https://prettier.io/)
[![Linting: ESLint](https://img.shields.io/badge/linting-ESLint-4B32C3)](https://eslint.org/)

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
    - 📦 [**Poetry**](https://python-poetry.org) for dependency management.
    - 🐶 [**Ruff**](https://github.com/astral-sh/ruff) for linting.
    - 📝 [**Pydantic**](https://docs.pydantic.dev) for data validation.
    - 🗃 [**SQLite**](https://www.sqlite.org) as database.
    - 🆓 **ORM Free**: Use raw SQL queries by leveraging the repository pattern.
    - 🛠 [**SQLift**](https://github.com/SpaceShaman/SQLift) for database migrations.
- 🚀 [**Nuxt.js**](https://nuxt.com) for the frontend.
    - 🟦 [**TypeScript**](https://www.typescriptlang.org) for static type checking.
    - 🖌 [**Prettier**](https://prettier.io) for code formatting.
    - ✨ [**ESLint**](https://eslint.org) for linting.
    - 🎨 [**TailwindCSS**](https://tailwindcss.com) for styling.
    - 🧩 [**daisyUI**](https://daisyui.com) for ready-to-use [**TailwindCSS**](https://tailwindcss.com) components.
    - 🔐 Middleware for authentication.
    - 📝 Form validation via [**VeeValidate**](https://vee-validate.logaretm.com) and [**Yup**](https://yup-docs.vercel.app/)
    - 🎨 Theme selector with 32 themes from [**daisyUI**](https://daisyui.com).
    - 🚨 Alerts and toasts via simple utility functions.
        - ❌ Call `showErrorAlert('message')` to show an error message.
        - ✅ Call `showSuccessAlert('message')` to show a success message.
        - 💡 Call `showInfoAlert('message')` to show an info message.
        - ⚠️ Call `showWarningAlert('message')` to show a warning message.
- 🔑 **JWT** (JSON Web Token) authentication.
- 📝 Registration with email based account activation.
- 🔒 Secure password hashing.
- 📫 Email based password recovery.
- 📧 SMTP email integration for sending emails.
- ✉️ Jinja templates for email messages.
- ✅ Tests with [Pytest](https://pytest.org).
- 🚢 Deployment instructions using Docker Compose.
- 🔄 **CI/CD** with GitHub Actions
    - 🧪 Automated testing before deployment
    - 📊 Code coverage reporting with Codecov
    - 🚀 Continuous integration and deployment pipeline
    - 📦 Ready-to-use workflow configurations in `.github/workflows/`

### Login Page

![Login](img/login.png)
![Login](img/login-dark.png)

### Register Page

![Register](img/register.png)

### Password Recovery

![Password Recovery](img/password-recovery.png)

### Theme Selector

![Theme Selector](img/theme-selector.png)

### Alerts and Toasts

![Alerts and Toasts](img/alerts-and-toasts.png)

### Validation

![Validation](img/validation.png)

### Simple Dashboard

![Dashboard](img/dashboard.png)

### Activation Email

![Activation Email](img/activation-email.png)

## How To Use It

You can **just fork or clone** this repository and use it as is.

✨ It just works. ✨

### Configure

You need to configure the environment variables to set your own values.
You can copy the example `.env` files:

```bash
cp .env.default .env
```

And then edit the `.env` file and set your own values.

### Run

#### Run in development environment

```bash
docker-compose -f docker-compose.dev.yml up
```

#### Run in production environment

```bash
docker-compose up
```

### CI/CD

This project has a CI/CD pipeline with GitHub Actions.
You can see the workflow configuration in [.github/workflows/](.github/workflows/).
To use it, you need to set the following secrets in your repository settings:

```bash
CODECOV_TOKEN   # Your Codecov token
HOST            # Your SSH host
SSH_KEY         # Your SSH private key
USERNAME        # Your SSH username
```

### Comunication between FastAPI and Nuxt.js

The communication between FastAPI and Nuxt.js is done via plugin `api' which is located in [frontend/plugins/api.ts](frontend/plugins/api.ts).
This plugin uses the [$fetch](https://nuxt.com/docs/getting-started/data-fetching) to make requests to the FastAPI backend.
You can use this plugin in two ways:

#### Like useFetch

```typescript
const { data: users } = await useAPI<User[]>('/users', {
    method: 'get',
    ...
})
```

#### Like $fetch

```typescript
await useNuxtApp().$api<{ token: string }>('/auth/login', {
    method: 'POST',
    ...
})
```

## License

This project is licensed under the terms of the [MIT license](/LICENSE).

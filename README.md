# Full Stack FastAPI Nuxt.js JWT Auth ORM Free Template

[![GitHub License](https://img.shields.io/github/license/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)](https://github.com/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template?tab=MIT-1-ov-file)
[![Tests](https://img.shields.io/github/actions/workflow/status/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template/release.yml?label=tests)](https://github.com/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template/blob/master/.github/workflows/tests.yml)
[![Codecov](https://img.shields.io/codecov/c/github/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)](https://codecov.io/gh/SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template)
[![Python](https://img.shields.io/badge/language-Python-yellow?logo=python&logoColor=yellow)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/language-TypeScript-yellow?logo=typescript&logoColor=yellow)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/framework-FastAPI-green?logo=fastapi&logoColor=green)](https://fastapi.tiangolo.com/)
[![Nuxt.js](https://img.shields.io/badge/framework-Nuxt-green?logo=nuxt.js&logoColor=green)](https://nuxt.com/)
[![Docker](https://img.shields.io/badge/technology-Docker-blue?logo=docker&logoColor=blue)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/technology-Docker%20Compose-blue?logo=docker&logoColor=blue)](https://docs.docker.com/compose/)
[![Pydantic](https://img.shields.io/badge/technology-Pydantic-blue?logo=pydantic&logoColor=blue)](https://docs.pydantic.dev)
[![Tailwind CSS](https://img.shields.io/badge/styling-Tailwind%20CSS-blue?logo=tailwind-css&logoColor=blue)](https://tailwindcss.com/)
[![daisyUI](https://img.shields.io/badge/styling-daisyUI-blue?logo=daisyui&logoColor=blue)](https://daisyui.com/)
[![VeeValidate](https://img.shields.io/badge/validation-VeeValidate-blue?logo=vee-validate&logoColor=blue)](https://vee-validate.logaretm.com)
[![Yup](https://img.shields.io/badge/validation-Yup-blue?logo=yup&logoColor=blue)](https://yup-docs.vercel.app/)
[![Jinja](https://img.shields.io/badge/templating-Jinja-blue?logo=jinja&logoColor=blue)](https://jinja.palletsprojects.com/)
[![JWT](https://img.shields.io/badge/authentication-JWT-blue?logo=json-web-tokens&logoColor=blue)](https://jwt.io/)
[![Pytest](https://img.shields.io/badge/testing-Pytest-red?logo=pytest&logoColor=red)](https://docs.pytest.org/)
[![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey?logo=sqlite&logoColor=blue)](https://www.sqlite.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/badge/linting-Ruff-black?logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff)
[![Code formatter: Prettier](https://img.shields.io/badge/code%20formatter-Prettier-ff69b4)](https://prettier.io/)

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
    - 📦 [**Poetry**](https://python-poetry.org) for dependency management.
    - 🗃 [**SQLite**](https://www.sqlite.org) as database.
    - 🆓 **ORM Free**: Use raw SQL queries by leveraging the repository pattern.
    - 🛡 JWT token authentication.
- 🚀 [**Nuxt.js**](https://nuxt.com) for the frontend.
    - 🟦 [**TypeScript**](https://www.typescriptlang.org) for static type checking.
    - 🎨 [**TailwindCSS**](https://tailwindcss.com) for styling.
    - 🧩 [**daisyUI**](https://daisyui.com) for ready-to-use [**TailwindCSS**](https://tailwindcss.com) components.
    - 🔐 Middleware for authentication.
    - 📝 Form validation via [**VeeValidate**](https://vee-validate.logaretm.com) and [**Yup**](https://yup-docs.vercel.app/)
    - 🎨 Theme selector with 32 themes from [**daisyUI**](https://daisyui.com).
    - 🚨 Alerts and toasts via simple utility functions.
        - ❌ Call `showErrorMessage('message')` to show an error message.
        - ✅ Call `showSuccessMessage('message')` to show a success message.
        - 💡 Call `showInfoMessage('message')` to show an info message.
        - ⚠️ Call `showWarningMessage('message')` to show a warning message.
- 🔑 **JWT** (JSON Web Token) authentication.
- 📝 Registration with email based account activation.
- 🔒 Secure password hashing.
- 📫 Email based password recovery.
- 📧 SMTP email integration for sending emails.
- ✉️ Jinja templates for email messages.
- ✅ Tests with [Pytest](https://pytest.org).
- 🚢 Deployment instructions using Docker Compose.

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

## How To Use It

You can **just fork or clone** this repository and use it as is.

✨ It just works. ✨

### How to Use a Private Repository

If you want to have a private repository, GitHub won't allow you to simply fork it as it doesn't allow changing the visibility of forks.

But you can do the following:

- Create a new GitHub repo, for example `my-full-stack`.
- Clone this repository manually, set the name with the name of the project you want to use, for example `my-full-stack`:

```bash
git clone git@github.com:SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template my-full-stack
```

- Enter into the new directory:

```bash
cd my-full-stack
```

- Set the new origin to your new repository, copy it from the GitHub interface, for example:

```bash
git remote set-url origin git@github.com:octocat/my-full-stack.git
```

- Add this repo as another "remote" to allow you to get updates later:

```bash
git remote add upstream git@github.com:SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template
```

- Push the code to your new repository:

```bash
git push -u origin master
```

### Update From the Original Template

After cloning the repository, and after doing changes, you might want to get the latest changes from this original template.

- Make sure you added the original repository as a remote, you can check it with:

```bash
git remote -v

origin    git@github.com:octocat/my-full-stack.git (fetch)
origin    git@github.com:octocat/my-full-stack.git (push)
upstream    git@github.com:SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template.git (fetch)
upstream    git@github.com:SpaceShaman/full-stack-fastapi-nuxt-jwt-auth-orm-free-template.git (push)
```

- Pull the latest changes without merging:

```bash
git pull --no-commit upstream master
```

This will download the latest changes from this template without committing them, that way you can check everything is right before committing.

- If there are conflicts, solve them in your editor.

- Once you are done, commit the changes:

```bash
git merge --continue
```

### Configure

You need to configure the environment variables to set your own values.
You can copy the example `.env` files:

```bash
cp .env.default .env
```

And then edit the `.env` file and set your own values.

### Run the Full Stack

You can run the full stack with:

```bash
docker-compose up
```

## License

This project is licensed under the terms of the [MIT license](/LICENSE).

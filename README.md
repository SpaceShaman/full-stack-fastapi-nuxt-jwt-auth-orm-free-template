# Full Stack FastAPI Nuxt.js JWT Auth ORM Free Template

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
    - 🗃 [**SQLite**](https://www.sqlite.org) as database.
    - 🆓 **ORM Free**: Use raw SQL queries by leveraging the repository pattern.
    - 🛡 JWT token authentication.
- 🚀 [**Nuxt.js**](https://nuxt.com) for the frontend.
    - 🟦 [**TypeScript**](https://www.typescriptlang.org) for static type checking.
    - 🎨 [**TailwindCSS**](https://tailwindcss.com) for styling.
    - 🧩 [**daisyUI**](https://daisyui.com) for ready-to-use [**TailwindCSS**](https://tailwindcss.com) components.
    - 🔐 Middleware for authentication.
    - 📝 Form validation via [**VeeValidate**](https://vee-validate.logaretm.com) and [**Yup**](https://yup-docs.vercel.app/)
- 🔑 **JWT** (JSON Web Token) authentication.
- 📝 Registration with email based account activation.
- 🔒 Secure password hashing.
- 📫 Email based password recovery.
- 📧 SMTP email integration for sending emails.
- ✉️ Jinja templates for email messages.
- ✅ Tests with [Pytest](https://pytest.org).
- 🚢 Deployment instructions using Docker Compose.

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
upstream    git@github.com:fastapi/full-stack-fastapi-template.git (fetch)
upstream    git@github.com:fastapi/full-stack-fastapi-template.git (push)
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

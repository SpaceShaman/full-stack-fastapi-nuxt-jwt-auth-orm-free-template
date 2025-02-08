FROM node:20.10-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm i
COPY . .

FROM base AS dev
CMD ["npm", "run", "dev"]

FROM base AS build
RUN npm run build

FROM node:20.10-alpine AS prod
COPY --from=build /app/.output /.output
CMD [ "node", "/.output/server/index.mjs" ]
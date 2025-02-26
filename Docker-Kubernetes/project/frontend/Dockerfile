FROM node:16-alpine AS builder
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
CMD ["npm","run","build"]

FROM nginx
# You copy some parts from the builder phase (--from=builder - Declared on the top)
# We copy /app/build that is produced in the "npm run build" command and paste it inside the /usr/share/nginx/html
COPY --from=builder /app/build /usr/share/nginx/html

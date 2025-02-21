# Base image

FROM node:14-alpine

# Copy everything for cwd to docker container
COPY ./ ./

# install dependencies
RUN npm install

# Execute when container starts

CMD ["npm","start"] 
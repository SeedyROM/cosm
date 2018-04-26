#==================== Building Stage ================================================ 

# Create the image based on the official Node 8.9.0 image from Dockerhub
FROM node:8.9.0 as node

# Create a directory where our app will be placed. This might not be necessary
RUN mkdir -p /src

# Change directory so that our commands run inside this new directory
WORKDIR /src

# Copy dependency definitions
COPY package.json /src

# Install dependencies using npm
RUN npm install

# Get all the code needed to run the app
ADD . /src

# Expose the port the app runs in
EXPOSE 4000

#Build the app
RUN npm run build

#==================== Setting up stage ==================== 
# Create image based on the official nginx - Alpine image
FROM nginx:1.13.7-alpine

COPY --from=node /src/dist/ /usr/share/nginx/html

ADD ./config/nginx /etc/nginx/conf.d

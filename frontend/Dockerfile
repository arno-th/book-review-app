FROM node:22-alpine
WORKDIR /react

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build
CMD ["npm", "run", "dev"]
FROM node:20.11.1-alpine3.19

WORKDIR /quiz-daddy-client

COPY . .

RUN npm install

EXPOSE 4000

CMD ["npx", "run", "start"]
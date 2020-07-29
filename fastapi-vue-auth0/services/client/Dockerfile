FROM node:12.16.3-alpine

RUN mkdir /code
WORKDIR /code

ENV PATH /code/node_modules/.bin:$PATH

COPY package.json /code/package.json
RUN yarn install
RUN yarn global add @vue/cli@4.4.6

CMD ["yarn", "serve"]

ARG INSTALL_NGINX_VERSION=${INSTALL_NGINX_VERSION}
FROM nginx:${INSTALL_NGINX_VERSION}-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY dev.conf /etc/nginx/conf.d

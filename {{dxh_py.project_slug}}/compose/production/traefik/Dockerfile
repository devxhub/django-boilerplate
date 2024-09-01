FROM docker.io/traefik:3.1.2

# Install gettext for envsubst
RUN apk add --no-cache gettext nano

RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./compose/production/traefik/traefik.yml /etc/traefik

FROM alpine:3 as build

ARG VERSION

RUN case $(uname -m) in \
    x86_64) \
        echo linux-amd64 > /platform ;; \
    aarch64) \
        echo linux-arm64 > /platform ;; \
    *) \
        echo "Unknown architecture: $(uname -m)" \
        exit 1 ;; \
    esac

RUN echo Building $(cat /platform) image for ${VERSION}...

RUN echo Downloading: https://cdn.teleport.dev/teleport-${VERSION}-$(cat /platform)-bin.tar.gz

RUN wget -q https://cdn.teleport.dev/teleport-${VERSION}-$(cat /platform)-bin.tar.gz -O teleport.tar.gz

RUN tar xfz teleport.tar.gz teleport/teleport

RUN < /teleport/teleport sha1sum > /teleport/teleport.sha1

FROM debian:bookworm-slim as test

RUN mkdir /teleport
COPY --from=build /teleport/teleport /teleport/teleport

RUN teleport/teleport version

FROM debian:bookworm-slim

COPY --from=test /teleport/teleport /teleport
COPY --from=build /teleport/teleport.sha1 /teleport.sha1

COPY start /start
RUN chmod +x /start

ENV HOST_ROOT=/var/teleport-node

CMD ["/start"]

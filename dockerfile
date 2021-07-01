FROM ubuntu:18.04

# avoid tzdata
ENV DEBIAN_FRONTEND=noninteractive

COPY ./ndpisplit_rebuilded /

RUN ln -s /ndpisplit_rebuilded /usr/local/bin/ndpisplit



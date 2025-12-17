FROM ubuntu:22.04

RUN apt-get update && apt-get install -y gcc

WORKDIR /bench
COPY main.c .

RUN gcc -O2 main.c -o bench

CMD ["./bench"]


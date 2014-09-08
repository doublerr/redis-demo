# redis-demo

## Description

Super simple demo app to show off the power of Docker and Fig. The leverages tornado as the web/app server and redis as the key/value storage.

## Installation

This package can be built directly with `docker build`

    docker build -t redis-demo:latest .

## Usage
Once built, run the app as a docker container:

    docker run --rm --link redis:redis -p "5000:8888" -t redis-demo

The add should be available on port 5000 now. 

Note: This uses links to bind to a redis container named "redis" running on the same host. If you don't want to use links, you can pass these two environment variables in the docker run command instead:

    REDIS_PORT_6379_TCP_ADDR=<your redis host>
    REDIS_PORT_6379_TCP_PORT=6379

The app will throw a 500 error (by design) if it cannot reach redis.

## Fig
You can stand up a self contained environment that includes the app and redis via fig:

    git checkout fig
    fig up

## Authors
* Alex Brandt <alunduil@alunduil.com>
* Ryan Richard <ryanrichard07@gmail.com>
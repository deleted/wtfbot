#!/bin/bash
docker build -t wtfbot .
docker rm wtfbot
docker run --name wtfbot --link wtfbot-db-dev:db wtfbot

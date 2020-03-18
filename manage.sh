#!/usr/bin/env bash
docker-compose -f docker/docker-compose.prod.yml exec app "$@"

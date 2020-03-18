#!/usr/bin/env bash
docker-compose -f docker/docker-compose.local.yml exec app "$@"

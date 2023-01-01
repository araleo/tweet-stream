#!/bin/sh

if [ $# -lt 1 ] || [ $# -gt 2 ];
  then
   echo "Usage: run.sh <command>"
   echo "Available commands: dev stop"
   exit 1
fi

case $1 in
    "dev")
        docker-compose -f docker-compose.dev.yml up -d --build ;;
    "stop")
        docker-compose -f docker-compose.dev.yml down ;;
esac
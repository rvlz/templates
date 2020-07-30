#!/bin/bash

type=$1
failed_tests=""

inspect() {
  if [ $1 -ne 0 ]; then
    failed_tests="${failed_tests} $2"
  fi
}

test_api() {
  docker-compose up -d --build
  docker-compose exec api python manage.py init
  docker-compose exec api python manage.py test
  inspect $? api
  docker-compose exec api flake8 app manage.py
  inspect $? api-lint
  docker-compose down -v
}

test_client() {
  docker-compose up -d --build
  docker-compose exec client yarn test:unit
  inspect $? client
  docker-compose down -v
}

test_all() {
  docker-compose up -d --build
  docker-compose exec api python manage.py init
  docker-compose exec api python manage.py test
  inspect $? api
  docker-compose exec api flake8 app manage.py
  inspect $? api-lint
  docker-compose exec client yarn test:unit
  inspect $? client
  docker-compose down -v
}

if [[ "${type}" == "api" ]]; then
  echo "Running API tests."
  test_api
elif [[ "${type}" == "client" ]]; then
  echo "Running client tests."
  test_client
else
  echo "Running all tests."
  test_all
fi

if [[ -n ${failed_tests} ]]; then
  echo "TESTS FAILED:${failed_tests}"
  exit 1
else
  echo "TESTS SUCCEEDED"
  exit 0
fi

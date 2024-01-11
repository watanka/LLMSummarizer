all: down build up test

build: 
		docker-compose build
up:
		docker-compose up -d
down:
		docker-compose down --remove-orphans
unit-tests: 
		docker-compose run --rm --no-deps --entrypoint=pytest summarizer /summarizer/tests/unit
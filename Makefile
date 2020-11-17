build:
	docker build -t sa_notebook_builder .
test:
	docker run --rm -it -v $(shell pwd):/usr/src/app sa_notebook_builder

.PHONY: build test
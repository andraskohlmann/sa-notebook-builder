build:
	docker build -t sa_notebook_builder .
test:
	docker run --rm -it sa_notebook_builder

.PHONY: build test
.PHONY: test clean

test:
	python test

dist:
	python setup.py sdist

clean:
	rm -rf dist/*
	rm -rf ./**/*.pyc

install:
	pip install dist/*

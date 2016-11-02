dist:
	python setup.py sdist

clean:
	rm -rf dist/*

install:
	pip install dist/*
make: 
	scripts/make
build:
	scripts/make build
clean:
	scripts/make clean
install:
	scripts/make install
reinstall:
	scripts/make reinstall
uninstall:
	scripts/make uninstall
linters:
	scripts/make linters
pytest:
	scripts/make pytest
black:
	scripts/make black
testpypi:
	scripts/make testpypi
pypi:
	scripts/make pypi
tox:
	scripts/make tox

build:
	python setup.py build_ext --inplace
	mkdir -p src/rng
	cp -f build/lib.*/*rngcpp*.so src/rng/

clean:
	rm -rf build dist *.egg-info
	rm -f rngcpp*.so
	rm -f src/rng/rngcpp*.so

build:
	pip install -r requirements.txt
	pip install -e .

clean:
	rm -rf build dist
	rm -rf src/*.egg-info
	rm -rf src/rng/*.so
	rm -rf src/rng/__pycache__


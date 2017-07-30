.PHONY: publish
publish:
	rm -r build dist
	python setup.py bdist_wheel
	twine upload dist/*


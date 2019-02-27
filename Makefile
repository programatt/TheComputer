test:
	pytest

test-watch:
	ptw -v

coverage:
	pytest --cov-config .coveragerc --cov ./ tests

coverage-xml:
	pytest --cov-report xml --cov-config .coveragerc --cov ./ tests




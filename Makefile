test:
	ptw -v

coverage:
	pytest --cov-config .coveragerc --cov ./ tests

coverage-submit:
	pytest --cov-report xml --cov-config .coveragerc --cov ./ tests
	CODECOV_TOKEN=613f5cfb-d100-42b7-a52b-3cdef5f78965 codecov




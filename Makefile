.PHONY: requirements

ROOT = $(shell echo "$$PWD")

requirements:
	pip install -r requirements/base.txt

test.requirements: requirements
	pip install -r requirements/test.txt

docs.requirements: requirements
	pip install -r requirements/docs.txt

develop: requirements
	pip install -r requirements/test.txt
	pip install -r requirements/docs.txt

tests:
	nosetests hangmanbot

quality:
	pep8 hangmanbot
	PYTHONPATH=".:./hangmanbot:$PYTHONPATH" pylint --rcfile=./.pylintrc hangman dicts

hangmanbot.run:
	PYTHONPATH=".:./hangmanbot:$PYTHONPATH" python -m run

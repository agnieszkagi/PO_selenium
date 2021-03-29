.PHONY : test

test:
	PYTHONPATH=test_register_page.py pytest-3 --verbose -s

lint:
	black pages; \
	black locators.py; \
	black test_base.py; \
	black test_register_page.py

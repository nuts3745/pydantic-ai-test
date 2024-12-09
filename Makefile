.PHONY: init
init:
	uv sync
	echo GEMINI_API_KEY= > .env

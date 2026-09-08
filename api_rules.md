# API Coding Standard

Apply these standards to code that processes API requests or responses.

1. Endpoint handler names must use `snake_case`.
2. Validate required request fields before accessing them.
3. Return structured dictionaries; do not print from handlers.
4. Wrap external service calls in `try`/`except` and return a useful error.
5. Never hard-code credentials or API keys in source files.
6. Public handlers require a docstring.


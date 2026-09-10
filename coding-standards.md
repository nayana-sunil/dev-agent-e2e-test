# Coding Standards

Rules derived from the code in this repo (`payment_webhook.py`, `utils.py`). A testing/review agent should check code against these rules.

1. **No hardcoded secrets.** API keys and credentials must not be committed as string literals (e.g. `API_KEY = "..."` in `payment_webhook.py` and `utils.py`). Load them from environment variables or a secrets manager.
2. **No bare `except:` clauses.** Catch specific exception types (e.g. `requests.RequestException`) instead of swallowing everything, so unrelated bugs aren't hidden.
3. **No `print()` for error reporting.** Use the `logging` module so failures are captured, leveled, and routed to real log storage.
4. **Network calls must set an explicit timeout.** `requests.post`/`requests.get` calls must pass `timeout=...` to avoid hanging indefinitely.
5. **Failures must be surfaced, not silently returned as `None`.** Callers need to distinguish "no data" from "the call failed" — raise or return an explicit error/result type.

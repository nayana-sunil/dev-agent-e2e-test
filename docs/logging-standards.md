# Logging Standards

All log messages must include a timestamp and severity level.
Never log raw exception objects directly — always log `str(exc)`.

Never log secrets, tokens, or full request payloads — mask sensitive fields before logging.

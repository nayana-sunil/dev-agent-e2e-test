# Logging Standards

All log messages must include a timestamp and severity level.
Never log raw exception objects directly — always log `str(exc)`.

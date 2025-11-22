# Python Guidelines

1. **Modern standard only** – target Python 3.14+ and avoid legacy compatibility imports such as `from __future__ import annotations` or any other future flags already enabled by default.
2. **Type clarity** – prefer built-in typing helpers (`Literal`, `TypedDict`, `Annotated`, `Path`) and keep modules annotation-complete for mypy and IDEs.
3. **First-party first** – lean on the standard library before adding third-party helpers unless they unlock a significant feature (scraping, LLM access, data viz).
4. **Explicit contracts** – expose settings through typed Pydantic models, validate I/O schemas aggressively, and document any dynamic behavior inline.

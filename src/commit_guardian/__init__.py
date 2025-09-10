from typing import List

__all__: List[str] = ["ping", "__version__"]
__version__ = "0.0.1"


def ping() -> str:
    return "pong"

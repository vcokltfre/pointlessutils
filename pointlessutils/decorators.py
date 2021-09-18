from asyncio import iscoroutinefunction
from inspect import isfunction
from random import choice


def _deco_factory(c):
    def deco(func):
        if iscoroutinefunction(func):
            async def wrapper(*args, **kwargs):  # type: ignore
                return c() if isfunction(c) else c
        else:
            def wrapper(*args, **kwargs):
                return c() if isfunction(c) else c
        return wrapper
    return deco


none  = _deco_factory(None)
true  = _deco_factory(True)
false = _deco_factory(False)
maybe = _deco_factory(lambda: choice([True, False]))

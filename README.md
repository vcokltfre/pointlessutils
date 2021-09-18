# Pointless Utils

A collection of utilities that are (probably) pointless.

## Decorators

There are currently 6 pointless decorators available to use:

- `@none` - Causes the function to always return `None`
- `@true` - Causes the function to always return `True`
- `@false` - Causes the function to always return `False`
- `@maybe` - Causes the function to return a random choice of `True` or `False`
- `@never` - The function will never return and will block indefinitely
- `@always` - The function is now a generator that indefinitely yields `True`
- `@alwaysv(value)` - The function is now a generator that indefinitely yields the given value

These decorators can be used on either normal or async functions, except `alwaysv`. For example:

```py
@maybe
def ex_1():
    pass

@maybe
async def ex_2():
    pass
```

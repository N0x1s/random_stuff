from functools import wraps

# repeat function call untill it works or max attempts reached


def repeat(*, n=5):
    def innerrepeat(func=None):
        nonlocal n
        fn = func if func else n
        n = n if isinstance(n, int) else 5

        @wraps(fn)
        def wrapper(*args, **kw):
            nonlocal n
            while n:
                try:
                    return fn(*args, **kw)
                except Exception:
                    pass
                n -= 1
            raise ValueError('Max attempts reached') from None
        return wrapper if func else wrapper()
    return innerrepeat

# class repeat:
#     def __init__(self, func=None, *, n=5):
#         self.n = n
#         self.func = func
#
#     def __call__(sel

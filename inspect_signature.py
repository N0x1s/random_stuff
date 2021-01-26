from itertools import zip_longest
from inspect import Signature, Parameter, currentframe

_fields = ['age', 'hobbies']
sig = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
						for name in _fields])

def func(name, /, *args, **kwargs):
	fest = globals()[currentframe().f_code.co_name]
	for name, value in zip_longest(_fields, sig.bind_partial(*args, **kwargs
				).arguments.values()):
				if not hasattr(fest, name):
					print(f'SETTING {name!r}')
					setattr(fest, name, value)

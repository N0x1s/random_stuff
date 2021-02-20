import inspect

"""
def bind_with_default(sig, /, default=None, defaults={}, *agrs, **kwargs):
	args = sig.bind_partial(*agrs, **kwargs).arguments
	args.update({elem: defaults[elem] if elem in defaults else default
						for elem in sig.parameters if elem not in args})
	return args
"""

class Signature(inspect.Signature):
	"""Slighly modified Signature class to support bind with defaults"""
	def __init__(self, parameters=None, *, return_annotation=inspect._empty,
				 __validate_parameters__=True, default=None, defaults={}):
				 """
				 Parameters
				 ----------

				 	default: Any, optional
						default value for messing args (default is None)
					defaults: dict, optional
						special default value for some args(default is {})

				 Methods
				 -------
				 
				 	bind_with_defaults(*args, **kwargs):
					 	bind args and kwargs to signature with default support

				 """
				 self.default = default
				 self.defaults = defaults
				 super().__init__(parameters, return_annotation=return_annotation,
								__validate_parameters__=__validate_parameters__)

	def bind_with_defaults(self, *args, **kwargs):
		"""bind args and kwargs to signature with default args support"""
		args = super().bind_partial(*args, **kwargs).arguments
		args.update({elem: self.defaults[elem] if elem in self.defaults else self.default
							for elem in sig.parameters if elem not in args})
		return super().bind(**args)

_fields = ('age', 'hobbies')

sig = Signature([inspect.Parameter(name, inspect.Parameter.POSITIONAL_OR_KEYWORD)
						for name in _fields], default=None)

def func(name, /, *args, **kwargs):
	for name, value in sig.bind_with_defaults(*args, **kwargs).arguments.items():
		print(f'{name!r} = {value}')

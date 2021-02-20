from inspect import Signature
import functools

def annotation_check(method):
	_sig = Signature.from_callable(method)
	def wrapper(*args, **kwargs):
		nonlocal _sig
		bond = _sig.bind(*args, **kwargs)
		if not all(
			isinstance(bond.arguments.get(item), value.annotation)
				for item, value in _sig.parameters.items()
		):
			raise TypeError("Provided arguments doesn't match the annotation")
		return method(*args, **kwargs)
	return wrapper

@annotation_check
def hello(name: str, age: int):
	return f'hello {name}'

demos = (
	('name', 42),
	('name', '42'),
	('name', 42.2),
	('name', 'forty two'),
	(b'name', 42)
)
for demo in demos:
	try:
		print(hello(*demo))
	except Exception as e:
		print(f'{demo} failed: {e!r}')

import colorama
import inspect

for name, data in inspect.getmembers(colorama):
    if not name.startswith('_'):
        print(f'{name}: {type(data)}')



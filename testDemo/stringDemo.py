#string

str = 'adsdf*sd\dsaa/avc*?><|?,'
print(str)
print()
result = eval(repr(str).replace('\\', ''))
result = eval(repr(result).replace('/', ''))
result = eval(repr(result).replace('*', ''))
result = eval(repr(result).replace('?', ''))
result = eval(repr(result).replace('>', ''))
result = eval(repr(result).replace('<', ''))
result = eval(repr(result).replace('|', ''))
result = eval(repr(result).replace(',', ''))

print(result)
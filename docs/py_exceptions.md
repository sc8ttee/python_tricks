## [Python](.\python.html)
## Exceptions Clauses

#### Usage

* handles errors

#### Examples

```python
# example 1
startTime = time.time()
try:
	# Runs first
	f = open(path, mode="rb")
	data = f.read()
	return data
except FileNotFoundError as err:
	# Runs if exception occurs in try block
	logger.error(err)
	raise
else:
	# Executes if try block succeeds
	f.close()
finally:
	# This code always executes
	stopTime = time.time()
```

#### Disclaimers

* n/a

Sources: [_Socratica_](./sources.html)
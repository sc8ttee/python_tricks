## [Python](.\python.html)
## Filter

#### Usage

* filter data
* filter returns a filter object, so wrap in list

#### Examples

```python
# example 1
# create list of values greater than avg
data = [1, 2, 6, 9]
avg = statistics.mean(data)
list(filter(lambda x: x > avg, data))

# example 2
# remove None (e.g. "", 0, 0.0, [], (), {}, False, None)
countries = ["", "Argentina", "", "Brazil", "Chile"]
list(filter(None, countries))
```

#### Disclaimers

* when filtering None, beware of 0's. 0 is often valid data

Sources: [_Socratica_](./sources.html)
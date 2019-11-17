## [Python](.\python.html)
## Map

#### Usage

* apply function to iterable
* map returns an iterator object, so wrap in list

#### Examples

```python
# example 1
def area(r):
    return math.pi * (r**2)
radii = [2, 3, 6, 8]
list(map(area, radii))
```

#### Disclaimers

* n/a

Sources: [_Socratica_](https://youtu.be/hUes6y2b--0)
## Looping

#### Usage

* best way to loop over a collection

#### Examples

```python
colors = ['red', 'green', 'blue']
names = ['ray', 'dan', 'matt']

# example 1
for color in colors:
    print color

# example 2
# looping backwards
for color in reversed(colors):
    print color
    
# example 3
# looping with indicies
for index, color in enumerate(colors):
    print "index: {0}, value: {1}".format(index, color)
    
# example 4
# looping over two collections
for name, color in izip(names, colors):
    print "name: {0}, color: {1}".format(name, color)
    
# example 5
# looping in sorted order, reversed sorted order,
#     and sorted order by length
for color in sorted(colors):
    print color
    
for color in sorted(colors, reversed=True):
    print color
    
for color in sorted(colors, key=len):
    print color
    
# example 6
# loop until value 3 encountered
num = [1, 2, 3, 4, 5, 6]
for x in iter(num, 3):
    print x
    
# example 7
# loop with two outcomes
# if no break return -1, if break return i
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
```

#### Disclaimers

* n/a

Sources: [_Hettinger_](https://youtu.be/OSGv2VnC0go)
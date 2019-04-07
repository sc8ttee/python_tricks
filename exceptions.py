''' Standard Code and Examples for Exceptions in Python '''

''' assertions
    - internal self checks
    - passes error if impossible conditions are met

    disclaimers
    - Don't use for data validation
    - beware of asserts that never fail (i.e. tuples are truthy)

    source
    - "Python Tricks The Book, A Buffet of Awesome Python Features"
    - Dan Bader
'''
#example 1
shoes = {'name': 'Fancy Shoes', 'price': 14900}
def apply_discount(product, discount):
    price = product['price'] * (1.0 - discount)
    assert 0 <= price <= product['price']
    return price

#example 2
if cond == 'x':
    do_x()
elif cond == 'y':
    do_y()
else:
    assert False, ('impossible condition encountered')
import pizza

pizza.make_pizza(16, 'pepperoni')

import pizza as p

p.make_pizza('Super', 'cheese', 'pepperoni', 'feta')

from pizza import make_pizza

make_pizza(28, 'extra cheese')

from pizza import make_pizza as mp

mp('XXL', 'veggies')

from pizza import *

make_pizza(30, 'stupid cheese')
slice_pizza('large')

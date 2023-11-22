import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

print("x", x)
print("x.shape", x.shape)
print("y.shape", y.shape)

a,b = np.meshgrid(x, y)

print('a', a)
print('a.shape', a.shape)
print('b', b)
print('b.shape', b.shape)

stacked_mashgrid = np.vstack(np.meshgrid(x, y))

transposed_stacked_mashgrid = stacked_mashgrid.reshape(2, -1).T

print('stacked_mashgrid', stacked_mashgrid)
print('stacked_mashgrid.shape', stacked_mashgrid.shape)
print('transposed_stacked_mashgrid', transposed_stacked_mashgrid)
print('transposed_stacked_mashgrid.shape', transposed_stacked_mashgrid.shape)
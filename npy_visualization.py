"""
Written By Heechan Jeong 2020-11-27
BSD license
"""
import mouse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def det(m):
    dtnt = 0
    if m.shape[1] == 3:
        padded = np.pad(m, ((0,m.shape[1]-1), (0,0)), 'wrap')  # 상하좌우
        for i in range(m.shape[0]):
            dpadded = padded[i + 1:i+m.shape[0], 1:]
            dtnt += padded[i, 0]*det(dpadded)

    elif m.shape[0]==2:
        dtnt = m[0, 0]*m[1, 1]-m[0, 1]*m[1, 0]
    else:
        print("Wrong Shape! Please use 3x3 or 2x2!")
        dtnt = None

    return dtnt

basis1 = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])
basis2 = np.array([[1.5, 0, 0],
                   [0, 1.5, 0],
                   [0, 0, 1.5]])
a = np.array([4. , 4. , 4.])

print()
print("Visualizing Position Vector")
print()
print("Basis: ")
print(basis1)
print()
print("Default Position Vector: ")
print(a)
print()
print("Default LT Basis: ")
print(basis2)

foo = input("Please enter 'n' if you do not want to use Default position vector under this Basis: ")
if foo == 'n':
    print("Please enter your position vector...")
    x = input("type x coordinate(0.0~6.0): ")
    y = input("type y coordinate(0.0~6.0): ")
    z = input("type z coordinate(0.0~6.0): ")
    a = np.array([float(x), float(y), float(z)])

print()
print("Position Vector: ")
print(a)

foo = input("Please enter 'n' if you do not want to use Default Basis set for LT: ")
if foo == 'n':
    print("Please enter your Basis set for LT...")
    x = input("type the first element of the first basis(-3 ~ 3): ")
    y = input("type the second element of the first basis(-3 ~ 3): ")
    z = input("type the third element of the first basis(-3 ~ 3): ")
    n1 = [float(x), float(y), float(z)]
    x = input("type the first element of the second basis(-3 ~ 3): ")
    y = input("type the second element of the second basis(-3 ~ 3): ")
    z = input("type the third element of the second basis(-3 ~ 3): ")
    n2 = [float(x), float(y), float(z)]
    x = input("type the first element of the third basis(-3 ~ 3): ")
    y = input("type the second element of the third basis(-3 ~ 3): ")
    z = input("type the third element of the third basis(-3 ~ 3): ")
    n3 = [float(x), float(y), float(z)]
    basis2 = np.array([
        [n1[0],n2[0],n3[0]],
        [n1[1],n2[1],n3[1]],
        [n1[2],n2[2],n3[2]]
    ])

print()
print("Basis for LT: ")
print(basis2)

print()
print("a vector Before LT: ")
print(a)

b = np.dot(basis2, a.T)

print()
print("a vector After LT: ")
print(b)

print()
print("New Basis Determinant:")
print(det(basis2)) # 3.38 default



########################################################################################################################

fig = plt.figure(figsize=(20, 10))

elev=20
azim =60
lim = np.around(np.max(np.array([np.max(b), np.max(a), [10]])))
X = np.arange(-lim, lim, 3)
Y = np.arange(-lim, lim, 3)
Z = np.arange(-lim, lim, 3)
X_, Y_, Z_ = np.meshgrid(X, Y, Z)

XX = np.zeros_like(X)
YY = np.zeros_like(Y)
ZZ = np.zeros_like(Z)
ltX_, ltY_, ltZ_ = np.meshgrid(XX, YY, ZZ)
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Z)):
            temp = np.array([X_[i,j,k], Y_[i,j,k], Z_[i,j,k]])
            temp = np.dot(basis2, temp.T)
            temp = temp.T
            ltX_[i, j, k], ltY_[i, j, k], ltZ_[i, j, k] = temp[0],temp[1],temp[2]

ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.quiver(0, 0, 0, a[0], a[1], a[2], color ='cyan', arrow_length_ratio=0.2)
ax.quiver(0, 0, 0, 10, 0, 0, color = 'blue', lw = 3, arrow_length_ratio = 0.1 )
ax.quiver(0, 0, 0, 0, 10, 0, color = 'red', lw =3, arrow_length_ratio = 0.1 )
ax.quiver(0, 0, 0, 0, 0, 10, color = 'green', lw =3, arrow_length_ratio = 0.1 )
ax.text(a[0], a[1], a[2], 'a ('+str(a[0])+', '+str(a[1])+', '+str(a[2])+')', size = 15)
ax.title.set_text('standard basis')
ax.set_xlim(lim, -lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter3D(X_, Y_, Z_, c = X_+Y_+Z_, cmap='jet', marker = 'o', s = 5)
ax.view_init(elev=60, azim =20)
ax.grid()

ltax = fig.add_subplot(1, 2, 2, projection = '3d')
qvr = ltax.quiver(0, 0, 0, a[0], a[1], a[2], color ='cyan', arrow_length_ratio=0.1)
qvrx = ltax.quiver(0, 0, 0, 10, 0, 0, color = 'blue', arrow_length_ratio = 0.1 )
qvry = ltax.quiver(0, 0, 0, 0, 10, 0, color = 'red', arrow_length_ratio = 0.1 )
qvrz = ltax.quiver(0, 0, 0, 0, 0, 10, color = 'green', arrow_length_ratio = 0.1 )
ltax.text(b[0], b[1], b[2], 'b ('+str(b[0])+', '+str(b[1])+', '+str(b[2])+')', size = 15)
ltax.title.set_text('new basis')
ltax.set_xlim(lim, -lim)
ltax.set_ylim(-lim, lim)
ltax.set_zlim(-lim, lim)
ltax.set_xlabel('X')
ltax.set_ylabel('Y')
ltax.set_zlabel('Z')
ltsc_a = ltax.scatter3D(a[0], a[1], a[2], c='black', marker='o', s=10)
ltsc_b = ltax.scatter3D(b[0], b[1], b[2], c='black', marker='o', s=10)
ltsc = ltax.scatter3D(ltX_, ltY_, ltZ_, color='blue', marker='o', s=5)
lttx = ltax.text(5, 5, -3, "determinant: {}".format(det(basis1)), fontsize=20)
ltax.view_init(elev=elev, azim =azim)
ltax.grid()
########################################################################################################################

def animation_frame(frame):

    global qvr, qvrx, qvry, qvrz, ltsc, ltsc_a, ltsc_b, lttx, wheeldelta, i, pos  # 여기서의 qvr은 global인 qvr이므로 지역변수로 새로 선언하지 마라는 의미
    qvr.remove()
    qvrx.remove()
    qvry.remove()
    qvrz.remove()
    ltsc.remove()
    lttx.remove()

    if mouse.is_pressed():
        i = round(mouse.get_position()[0]/255, 2)
        if i > 10:
            i = 10
        elif i < 0:
            i = 0
    elif mouse.is_pressed(button='right'):
        pos=mouse.get_position()

    ltX = X_ + ((ltX_-X_)*i*0.1)
    ltY = Y_ + ((ltY_-Y_)*i*0.1)
    ltZ = Z_ + ((ltZ_-Z_)*i*0.1)
    ltsc = ltax.scatter3D(ltX, ltY, ltZ, c=X_+Y_+Z, cmap='jet', marker='o', s=5)
    lttx = ltax.text(-5, -5, -10, "determinant: {}".format(round((det(basis1) + (det(basis2)- det(basis1)) * i * 0.1), 3)), fontsize=20)

    ltax.view_init(azim=azim-((((pos[0]/2550)-0.5)*2)*90), elev=elev+((((pos[1]/1439)-0.5)*2)*90))

    qvr = ltax.quiver(0, 0, 0, a[0] + ((b[0]-a[0])*i*0.1), a[1] + ((b[1]-a[1])*i*0.1), a[2] + ((b[2]-a[2])*i*0.1), color ='cyan', arrow_length_ratio=0.2)
    qvrx = ltax.quiver(0, 0, 0, 10 + (basis2[0][0]-1)*i, basis2[0][1]*i, basis2[0][2]*i, color='blue', lw=3, arrow_length_ratio=0.1)
    qvry = ltax.quiver(0, 0, 0, 0 + ((basis2[1][0])*i), 10 + (basis2[1][1]-1)*i, basis2[1][2]*i, color='red', lw=3, arrow_length_ratio=0.1)
    qvrz = ltax.quiver(0, 0, 0, 0 + ((basis2[2][0])*i), basis2[2][1]*i, 10 + (basis2[2][2]-1)*i, color='green', lw=3, arrow_length_ratio=0.1)

    ltsc_a = ltax.scatter3D(a[0], a[1], a[2], c='black', marker='o', s=20)
    ltsc_b = ltax.scatter3D(b[0], b[1], b[2], c='black', marker='o', s=20)

i =0
pos = (1200, 700)

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.5), interval=30, repeat=True )
plt.show()
animation.save(r'C:\Users\JooHyunAhn\Interpine\GitRepos\numpy-playground\animation.gif', writer='pillow', fps=30)
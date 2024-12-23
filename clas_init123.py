import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# TODO add possibility to provide Z argument, then use plotly to draw rectangel or 3D cuboid DONE:)

class RectangleDraw():
    def __init__(self, arg1, arg2):
        self.posx = arg1
        self.posy = arg2
class CuboidDraw(RectangleDraw):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1, arg2)
        self.posz = arg3
position1 = CuboidDraw(11, 69, 6)


size = [position1.posx, position1.posy, position1.posz]
data = np.ones(size, dtype=np.bool)

fig =plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(data, facecolors="red")
# below dont work for some reason, in theory should chabge dimensions of generated Cube
Axes3D.set_box_aspect(aspect=(4,4,5), zoom=1)

plt.show()
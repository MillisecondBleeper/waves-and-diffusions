from manim import *
import numpy as np
import random


class Random3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )

        graph = ParametricFunction(lambda u: np.array([u,get_randomval(axes.y_range),get_randomval(axes.z_range)]), t_range=np.array(axes.x_range), color=BLUE).set_shade_in_3d(True)
        self.add(axes, graph)
        self.wait()
        # THE CAMERA IS AUTO SET TO PHI=0, THETA=-90
        # rotate camera every frame
        # transition from phi=0, theta=-90 to phi=90, theta=-90 smoothly
        self.move_camera(phi=45 * DEGREES, run_time=5)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
    
def get_randomval(rng):
    return random.uniform(rng[0], rng[1])
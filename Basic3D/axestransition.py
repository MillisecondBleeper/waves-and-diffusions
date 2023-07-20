from manim import *
import numpy as np

class AxesTransition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=8,
        )
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta= 15 * DEGREES, run_time=5)
        axes2 = axes.copy().shift(DOWN * 4)
        self.play(Transform(axes, axes2), run_time=1)
        self.wait()
        #axes.move_to(DOWN * 10)
        #self.remove(axes)

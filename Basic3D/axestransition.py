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
            x_axis_config= {
                "color": RED,
            },
            y_axis_config= {
                "color": GREEN,
            },
            z_axis_config= {
                "color": BLUE,
            },
        )
        self.add(axes)
        self.play(
            axes.animate.set_color(BLACK),
        )
        self.wait()

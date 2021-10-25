from manimlib import *
import math
import numpy as np

# 除了驱动点的连杆外，其他连杆不会独立存在，一定依附着从动点
from main import insec_of_circle


class DotFixed(Dot):
    CONFIG = {
        "color": BLUE
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DotDriver(Dot):
    CONFIG = {
        "color": RED
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def


class DotDriven(Dot):
    CONFIG = {
        "color": YELLOW
    }

    def __init__(self, d1, l1, d2, l2, **kwargs):
        c1 = insec_of_circle(d1, l1, d2, l2)[0]
        super().__init__(arc_centor=c1, **kwargs)

        self.driver1 = d1
        self.len1 = l1
        self.driver2 = d2
        self.len2 = l2
        self.rod1 = Line(self, d1)
        self.rod2 = Line(self, d2)

    def get_self_and_rods(self):
        return self, self.rod1, self.rod2

    def get_update_func_of_self_and_rods(self):
        self_updater = UpdateFromFunc(self, lambda e: e.move_arc_center_to(insec_of_circle(self.driver1, self.len1, self.driver2, self.len2)[0]))
        rod1_updater = UpdateFromFunc(self.rod1, lambda l: l.put_start_and_end_on(self.driver1.get_center(), self.get_center()))
        rod2_updater = UpdateFromFunc(self.rod2, lambda l: l.put_start_and_end_on(self.driver2.get_center(), self.get_center()))
        return self_updater, rod1_updater, rod2_updater


class Linkage1(Scene):
    def construct(self):
        radius = 3
        rod_length = 1.6

        fixed_o = Dot(ORIGIN).set_color(COLOR_FIXED)
        driver_a = Dot(RIGHT * radius).set_color(COLOR_DRIVER)
        target_b = Dot(RIGHT * radius / 2).set_color(COLOR_TARGET)

        rod_ab = Line(driver_a, target_b)
        rod_ob = Line(fixed_o, target_b)

        self.add(fixed_o, driver_a, target_b, rod_ab, rod_ob)
        # drive
        while True:
            self.play(
                MoveAlongPath(driver_a, Circle(radius=radius)),
                UpdateFromFunc(target_b, lambda d: d.move_arc_center_to(
                    insec_of_circle(fixed_o, rod_length, driver_a, rod_length)[0])),
                UpdateFromFunc(rod_ab, lambda l: l.put_start_and_end_on(driver_a.get_center(), target_b.get_center())),
                UpdateFromFunc(rod_ob, lambda l: l.put_start_and_end_on(fixed_o.get_center(), target_b.get_center()))
            )
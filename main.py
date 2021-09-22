from manimlib import *
import math
import numpy as np

# TODO: make them subclass.
COLOR_DRIVER = RED
COLOR_FIXED = BLUE
COLOR_DRIVEN = YELLOW
COLOR_TARGET = GREEN


# TODO: find a better way to run and debug.
# from manimlib.__main__ import main
# if __name__ == '__main__':
#     main()


class Linkage0(Scene):
    def construct(self):
        radius = 2

        fixed = Dot(ORIGIN).set_color(COLOR_FIXED)
        driver = Dot(RIGHT * radius).set_color(COLOR_DRIVER)
        rod = Line(fixed, driver)

        # TODO: put rod to lower-level.

        def update_func(mob):
            mob.put_start_and_end_on(fixed.get_center(), driver.get_center())

        self.add(fixed, driver, rod)
        # drive
        # TODO: find a better way to repeat.
        while True:
            self.play(
                # TODO: move in uniform speed
                MoveAlongPath(driver, Circle(radius=radius)),
                UpdateFromFunc(rod, update_func)
            )
        # TODO: draw locus.


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

        # 问题其实就是，给定两个点的坐标，和一个未知点到他俩的距离，需要求未知点的坐标.
        # TODO: 二维平面中可能有两个解，这个时候需要考虑让它的移动连贯


# 求圆的交点
class Test(Scene):
    def construct(self):
        circleA = Circle(arc_center=ORIGIN, radius=2).set_color(BLUE)
        circleB = Circle(arc_center=RIGHT * 2, radius=2).set_color(BLUE)
        self.add(circleA, circleB)
        d1, d2 = insec_of_circle(Dot(ORIGIN), 2, Dot(RIGHT * 2), 2)
        print(d1, d2)
        self.add(d1, d2)


# TODO: 换成更阳间的模版或者库函数
def insec_of_circle(p1, r1, p2, r2):
    x = p1.get_center()[0]
    y = p1.get_center()[1]
    R = r1
    a = p2.get_center()[0]
    b = p2.get_center()[1]
    S = r2
    d = math.sqrt((abs(a - x)) ** 2 + (abs(b - y)) ** 2)
    if d > (R + S) or d < (abs(R - S)):
        print("Two circles have no intersection")
        return
    elif d == 0 and R == S:
        print("Two circles have same center!")
        return
    else:
        A = (R ** 2 - S ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(R ** 2 - A ** 2)
        x2 = x + A * (a - x) / d
        y2 = y + A * (b - y) / d
        x3 = round(x2 - h * (b - y) / d, 2)
        y3 = round(y2 + h * (a - x) / d, 2)
        x4 = round(x2 + h * (b - y) / d, 2)
        y4 = round(y2 - h * (a - x) / d, 2)
        # print(x3, y3)
        # print(x4, y4)
        d1 = np.array((x3, y3, 0.))
        d2 = np.array((x4, y4, 0.))
        # print(d1, d2)
        return [d1, d2]


# TODO: specify a good initial status
class PeaucellierLinkage(Scene):
    def construct(self):
        radius = 3

        fixed_o = Dot(ORIGIN).set_color(COLOR_FIXED)
        fixed_a = Dot(LEFT * radius).set_color(COLOR_FIXED)
        driver_b = Dot(RIGHT * radius).set_color(COLOR_DRIVER)
        driven_c = Dot(RIGHT * 2 - UP).set_color(COLOR_DRIVEN)
        driven_d = Dot(RIGHT * 2 + UP).set_color(COLOR_DRIVEN)
        target_e = Dot(RIGHT * radius * 2).set_color(COLOR_TARGET)

        # TODO: refine codes.
        length_ad = 7
        rod_ad = Line(fixed_a, driven_d)
        length_ac = 7
        rod_ac = Line(fixed_a, driven_c)
        length_bd = 2
        rod_bd = Line(driver_b, driven_d)
        length_bc = 2
        rod_bc = Line(driver_b, driven_c)
        length_ce = 2
        rod_ce = Line(driven_c, target_e)
        length_de = 2
        rod_de = Line(driven_d, target_e)
        rod_ob = Line(fixed_o, driver_b)

        driver_path = Arc(-TAU / 8, TAU / 4, radius=radius)
        target_path = Line(RIGHT*4.42+UP*3.05, RIGHT*4.42+DOWN*3.05)

        self.add(fixed_o, fixed_a, driver_b, driven_c, driven_d, target_e, rod_ad, rod_ac, rod_bd, rod_bc, rod_ce, rod_de, rod_ob, driver_path, target_path)
        # drive
        self.play(
            MoveAlongPath(driver_b, driver_path),
            UpdateFromFunc(rod_ob, lambda l: l.put_start_and_end_on(fixed_o.get_center(), driver_b.get_center())),
            UpdateFromFunc(driven_c, lambda c: c.move_arc_center_to(insec_of_circle(fixed_a, length_ac, driver_b, length_bc)[0])),
            UpdateFromFunc(driven_d, lambda d: d.move_arc_center_to(insec_of_circle(fixed_a, length_ad, driver_b, length_bd)[1])),
            UpdateFromFunc(rod_ac, lambda l: l.put_start_and_end_on(fixed_a.get_center(), driven_c.get_center())),
            UpdateFromFunc(rod_ad, lambda l: l.put_start_and_end_on(fixed_a.get_center(), driven_d.get_center())),
            UpdateFromFunc(rod_bc, lambda l: l.put_start_and_end_on(driver_b.get_center(), driven_c.get_center())),
            UpdateFromFunc(rod_bd, lambda l: l.put_start_and_end_on(driver_b.get_center(), driven_d.get_center())),
            UpdateFromFunc(target_e, lambda e: e.move_arc_center_to(insec_of_circle(driven_c, length_ce, driven_d, length_de)[0])),
            UpdateFromFunc(rod_ce, lambda l: l.put_start_and_end_on(driven_c.get_center(), target_e.get_center())),
            UpdateFromFunc(rod_de, lambda l: l.put_start_and_end_on(driven_d.get_center(), target_e.get_center())),
        )

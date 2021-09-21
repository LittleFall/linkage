from manimlib import *

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
        line = Line(fixed, driver)

        # TODO: put line to lower-level.

        def update_func(mob):
            mob.put_start_and_end_on(fixed.get_center(), driver.get_center())

        self.add(fixed, driver, line)
        # drive
        # TODO: find a better way to repeat.
        while True:
            self.play(
                # TODO: move in uniform speed
                MoveAlongPath(driver, Circle(radius=radius)),
                UpdateFromFunc(line, update_func)
            )
        # TODO: draw locus.


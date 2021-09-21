from manimlib import *


class Linkage0(Scene):
    def construct(self):
        radius = 2

        fixed = Dot(ORIGIN)
        driver = Dot(RIGHT * radius)
        line = Line(fixed, driver)

        def update_func(mob):
            #mob.set_start_and_end_attrs(driver, driver)
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

# from manimlib.__main__ import main
# if __name__ == '__main__':
#     main()

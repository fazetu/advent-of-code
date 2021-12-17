from typing import Dict, List, Tuple, Optional
from matplotlib.axes import Axes
import seaborn as sns
from skopt.utils import use_named_args

Point = Tuple[int, int]
TargetArea = Tuple[Point, Point]
input = "target area: x=20..30, y=-10..-5"
# input = "target area: x=195..238, y=-93..-67"


def parse_target_area(target_area: str) -> TargetArea:
    x, y = target_area.replace("target area: ", "").split(", ")
    xmin, xmax = x.replace("x=", "").split("..")
    ymin, ymax = y.replace("y=", "").split("..")
    return ((int(xmin), int(xmax)), (int(ymin), int(ymax)))


def toward_0(val: int, by: int = 1) -> int:
    if val == 0:
        return 0
    elif val < 0:
        return val + by
    else:
        return val - by


class Probe:
    def __init__(
        self, velocity: Point, target_area: TargetArea, x: int = 0, y: int = 0
    ):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.target_area = target_area
        self.steps: List[Point] = [(x, y)]

    @property
    def xs(self) -> List[int]:
        return [step[0] for step in self.steps]

    @property
    def ys(self) -> List[int]:
        return [step[1] for step in self.steps]

    def step(self):
        vx, vy = self.velocity
        self.x += vx
        self.y += vy
        self.velocity = (toward_0(vx, 1), vy - 1)
        self.steps.append((self.x, self.y))

    def step_n(self, n: int):
        for _ in range(n):
            self.step()

    def undershot_target_area(self) -> bool:
        xmin, _ = self.target_area[0]
        _, ymax = self.target_area[1]
        return (self.x < xmin) and (self.y > ymax)

    def overshot_target_area(self) -> bool:
        _, xmax = self.target_area[0]
        _, ymax = self.target_area[1]
        return (self.x > xmax) and (self.y > ymax)

    def missed_target_area(self) -> bool:
        return self.undershot_target_area() or self.overshot_target_area()

    def in_target_area(self) -> bool:
        xmin, xmax = self.target_area[0]
        ymin, ymax = self.target_area[1]
        return (xmin <= self.x <= xmax) and (ymin <= self.y <= ymax)

    def run_result(self) -> str:
        made_it = False
        while not made_it:
            self.step()
            made_it = self.in_target_area()

            if self.undershot_target_area():
                return "undershot"

            if self.overshot_target_area():
                return "overshot"

        return "hit"

    def highest_y_reached(self) -> int:
        return max(self.ys)

    def plot(self) -> Axes:
        ax = sns.lineplot(x=self.xs, y=self.ys)
        return ax

def score_velocity(velocity: Point, target_area: TargetArea) -> Optional[int]:
    p = Probe(velocity, target_area)
    res = p.run_result()

    if res == "hit":
        return p.highest_y_reached()
    else:
        return None

def next_velocities_to_try(velocity: Point, input: str) -> List[Point]:
    p = Probe(velocity, parse_target_area(input))
    res = p.run_result()

    if res == "undershot":
        x, y = velocity
        return [(x + 1, y), (x, y + 1), (x + 1, y + 1)]
    elif res == "overshot":
        x, y = velocity
        return [(x - 1, y), (x, y - 1), (x - 1, y - 1)]
    else:
        # hit!
        return []

ta = parse_target_area(input)
runs = {}
start = (0, 0)
p = Probe(start, ta)
res = 
runs[start] = 
never_hit = True

while never_hit:






from skopt import gp_minimize
from skopt.space import Integer
from skopt.utils import use_named_args

search_space = [Integer(0, 100, name="x"), Integer(-100, 100, name="y")]
ta = parse_target_area(input)


@use_named_args(search_space)
def to_minimize(**params) -> int:
    vel = (params["x"], params["y"])
    p = Probe(vel, ta)
    res = p.run_result()

    print(vel)
    print(res)

    if res == "hit":
        # return the highest height as a really low value
        return p.highest_y_reached() - 1000000
    else:
        return 1000000


res = gp_minimize(
    to_minimize, dimensions=search_space, n_calls=100, n_initial_points=100, verbose=True
)

print(res)

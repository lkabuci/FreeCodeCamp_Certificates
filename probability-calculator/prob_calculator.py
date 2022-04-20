import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, n in kwargs.items():
            self.contents += [color] * n
                                
    def draw(self, n_balls):

        if n_balls > len(self.contents):
            return self.contents

        chosen_balls = random.sample(self.contents, n_balls)
        for ball in chosen_balls:
            self.contents.pop( self.contents.index(ball) )

        return chosen_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_appeared = 0

    for exp in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat)

        draw_result = copy_of_hat.draw(num_balls_drawn)
        balls_selected_from_draw = {i:draw_result.count(i) for i in draw_result}

        times_appeared_partielle = 0

        for draw_color in balls_selected_from_draw:
            for expected_color in expected_balls:
                if expected_color == draw_color:
                    if expected_balls[expected_color] <= balls_selected_from_draw[draw_color]:
                        times_appeared_partielle += 1
        if times_appeared_partielle == len(expected_balls):
            times_appeared += 1

    return times_appeared/num_experiments
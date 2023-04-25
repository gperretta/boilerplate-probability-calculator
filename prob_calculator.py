import copy
import random


class Hat:
  # :param items_contained: a variable number of arguments (** operator)
  def __init__(self, **items_contained):
    # instance variable - a list of strings
    self.contents = []
    for color, num in items_contained.items():
      for i in range(num):
        # each item in the 'contents' list should be a color name
        self.contents.append(color)

  # :param int amount: number of balls to draw
  # :return string[] draw_list: return the balls removed from 'contents'
  def draw(self, amount):
    draw_list = []
    # if the amount exceeds the available quantity, return all the balls
    if amount >= len(self.contents):
      return self.contents
    for i in range(amount):
      # the items should be removed randomly
      item_index = random.randrange(len(self.contents))
      removed = self.contents.pop(item_index)
      draw_list.append(removed)
    return draw_list


# :param Hat hat: object containing balls that should be copied
# :param dictionary expected_balls: group of balls to attempt to draw from the hat for the experiment
# :param int num_balls_drawn: number of balls to draw out in each experiment
# :param int num_experiments: number of experiments to perform
# :return probability (result counter/num of experiments)
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counter = 0
  for _ in range(num_experiments):
    # deep copy operation
    # :note: assignment statements in Python do NOT copy objects, they create bindings (target-object)
    copied = copy.deepcopy(hat)
    temp = copied.draw(num_balls_drawn)
    success = True
    for key, value in expected_balls.items():
      if temp.count(key) < value:
        success = False
        break
    if success:
      counter += 1
  return counter / num_experiments

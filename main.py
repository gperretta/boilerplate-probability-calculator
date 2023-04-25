# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

hat = prob_calculator.Hat(black=6, red=4, green=3)
probability = prob_calculator.experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print("Probability:", probability)

main(module='test_module', exit=False)
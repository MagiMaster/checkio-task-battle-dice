"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import random

TESTS = {
    "Basics": [],
    "Small": [],
    "Big": []
}

def addTest(c, i, a):
    TESTS[c].append({"input": i, "answer": a})

addTest("Basics", [['A', 'D'], 3, 3], 0.00000)
addTest("Basics", [['A', 'D'], 4, 3], 1.00000)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 3, 4], 0.01863)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 4, 4], 0.40788)
addTest("Basics", [['AA', 'A', 'D', 'DD'], 5, 4], 0.90733)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 3, 4], 0.01636)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 4, 4], 0.43456)
addTest("Basics", [['AA', 'A', 'D', 'DD', 'AD'], 5, 4], 0.93766)

addTest("Small", [['A', ''], 1, 2], 0.04762)
addTest("Small", [['A', ''], 2, 2], 0.41587)
addTest("Small", [['A', ''], 3, 2], 0.84803)
addTest("Small", [['AA', 'A', ''], 1, 2], 0.04808)
addTest("Small", [['AA', 'A', ''], 2, 2], 0.25433)
addTest("Small", [['AA', 'A', ''], 3, 2], 0.60996)
addTest("Small", [['A', 'AD', 'D'], 1, 2], 0.00000)
addTest("Small", [['A', 'AD', 'D'], 2, 2], 0.44762)
addTest("Small", [['A', 'AD', 'D'], 3, 2], 0.98352)

addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 9, 10], 0.29073)
addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 10, 10], 0.49085)
addTest("Big", [['AAA', 'AAD', 'ADD', 'DDD', '', ''], 10, 9], 0.69431)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 9, 10], 0.08213)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 10, 10], 0.47264)
addTest("Big", [['A', 'A', 'A', 'A', 'A', 'A', 'D', 'D', 'D', ''], 10, 9], 0.89720)

import time

from multiple_choice import generate_multiple_choice
from tools import MultipleChoiceArgs

args = MultipleChoiceArgs()
args.filename = "test.txt"
args.max_questions = 10
args.generate_count = 10

time_start = time.time()
questions = generate_multiple_choice(args)
time_finish = time.time() - time_start
print(time_finish)
print(questions)
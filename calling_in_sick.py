# Calling in Sick by John Bagshaw

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

calling_in_sick = None

if actually_sick and sick_days > 0:
	calling_in_sick = True
	print("I am actually sick and need a day off")
elif kinda_sick and hate_your_job and sick_days > 0:
	calling_in_sick = True
	print("I am kinda sick and need a day off")
else:
	calling_in_sick = False
	print("I am not sick")

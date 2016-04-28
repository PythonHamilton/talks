import inflect
p = inflect.engine()

instructions = ["go outside", "turn left", "turn left", "turn left", "turn left", "arrive"]

for i, instruction in enumerate(instructions):
    print("{0}, {1}".format(p.ordinal(i + 1), instruction))


# 1st, go outside
# 2nd, turn left
# 3rd, turn left
# 4th, turn left
# 5th, turn left
# 6th, arrive

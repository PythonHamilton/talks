import inflect
p = inflect.engine()

dorothy_fears = ["lions", "tigers", "bears"]

print("{0}, oh my!".format(p.join(dorothy_fears)))

# lions, tigers, and bears, oh my!

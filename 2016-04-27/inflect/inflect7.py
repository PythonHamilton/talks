import inflect
p = inflect.engine()

# let's get pedantic!
p.classical(all=True)

print("The plural of formula is {0}.".format(p.plural("formula")))

# The plural of formula is formulae.

# or not
p.classical(all=False)

print("The plural of formula is {0}.".format(p.plural("formula")))

# The plural of formula is formulas.

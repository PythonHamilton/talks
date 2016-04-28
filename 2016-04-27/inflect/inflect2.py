import inflect
p = inflect.engine()

for n in range(3):
    print("There {0} {1} {2} currently online."
          .format(p.plural_verb("is", n),
                  n,
                  p.plural("user", n)))

# There are 0 users currently online.
# There is 1 user currently online.
# There are 2 users currently online.

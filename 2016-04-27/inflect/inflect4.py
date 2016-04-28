import inflect
p = inflect.engine()

print("Most style guides recommend:")
print("- words for small numbers, such as {0}".format(p.number_to_words(5, threshold=10)))
print("- numerals for larger numbers, such as {0}".format(p.number_to_words(50, threshold=10)))

# Most style guides recommend:
# - words for small numbers, such as five
# - numerals for larger numbers, such as 50

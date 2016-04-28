import inflect
p = inflect.engine()

phone_number = 5554908

print("Call me at: {0}.".format(p.number_to_words(phone_number, group=1, zero="oh")))

# Call me at: five, five, five, four, nine, oh, eight.

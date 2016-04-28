import inflect
p = inflect.engine()

big_number = 2234259.53

print(p.number_to_words(big_number))

# two million, two hundred and thirty-four thousand, two hundred and fifty-nine point five three

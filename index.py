from data.morse_codes import morse_codes
from helpers import probs_average, entropy

# 1a

def probs_in_morse_codes(character):
  probabilities = []
  for code in morse_codes:
    numerator = 0
    for letter in code:
      if letter == character:
        numerator += 1
    probabilities.append(numerator/len(code))
  return probabilities

def entropy_random():
  source = []
  for character in ['0', '1']:
    probabilities = probs_in_morse_codes(character)
    p = probs_average(probabilities)
    source.append(p)
  e = entropy(source)
  return [e, source]

e = entropy_random()
print(e)

# 1b



print('END')
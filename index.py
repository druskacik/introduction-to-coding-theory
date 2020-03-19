from data.morse_codes import morse_codes
from data.frequencies import frequencies
from helpers import average, entropy, entropy_random

# 1a

[e, source] = entropy_random()
print('Probability of a dot in morse code of a purely random string is ' + str(source[0]))
print('Probability of a dash in morse code of a purely random string is ' + str(source[1]))
print('Entropy in this scenario is ' + str(e) + '\n')

# 1b

def prob_in_english_text(character):
  probabilities = []
  for i, code in enumerate(morse_codes):
    frequency = frequencies[i]
    numerator = 0
    for letter in code:
      if letter == character:
        numerator += 1
    probabilities.append(numerator*frequency/len(code))
  return probabilities


def entropy_english_text():
  source = []
  for character in ['0', '1']:
    probabilities = prob_in_english_text(character)
    p = sum(probabilities)
    source.append(p)
  e = entropy(source)
  return [e, source]

[e, source] = entropy_english_text()
print('Probability of a dot in morse code of a random English text is ' + str(source[0]))
print('Probability of a dash in morse code of a random English text is ' + str(source[1]))
print('Entropy in this scenario is ' + str(e) + '\n')

print('END')
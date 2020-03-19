import math
from data.morse_codes import morse_codes

def average(probabilities):
  return sum(probabilities)/len(probabilities)

def entropy(source):
  summ = 0
  for p in source:
    summ -= p*math.log(p, 2)
  return summ

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
    p = average(probabilities)
    source.append(p)
  e = entropy(source)
  return [e, source]
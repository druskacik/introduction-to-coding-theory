from helpers import average, entropy, entropy_random
from data.morse_codes import morse_codes

def space_probability():
  avg_lenght = average([len(code) for code in morse_codes])
  return 1/(1 + avg_lenght)

def source_with_space():
  source = []
  default_source = entropy_random()[1]
  space_prob = space_probability()
  for value in default_source:
    source.append((1 - space_prob)*value)
  source.append(space_prob)
  e = entropy(source)
  return [e, source]

# 2a

[e, source] = source_with_space()
print('Probability of a dot in morse code of a random string with spaces is ' + str(source[0]))
print('Probability of a dash in morse code of a random string with spaces is ' + str(source[1]))
print('Probability of a space is ' + str(source[2]))
print('Entropy in this scenario is ' + str(e) + '\n')

print('END')
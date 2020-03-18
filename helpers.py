import math

def probs_average(probabilities):
  sum = 0
  for prob in probabilities:
    sum += prob
  return sum/len(probabilities)

def entropy(source):
  sum = 0
  for p in source:
    sum -= p*math.log(p, 2)
  return sum
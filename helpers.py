import math

def average(probabilities):
  return sum(probabilities)/len(probabilities)

def entropy(source):
  summ = 0
  for p in source:
    summ -= p*math.log(p, 2)
  return summ
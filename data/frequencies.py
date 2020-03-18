import json
import os, sys

def list_of_frequencies():
  with open(os.path.join(os.path.dirname(__file__), 'letter_frequency.json'), 'r') as f:
    frequencies = []
    json_frequencies = json.load(f)
    for e in json_frequencies:
      frequencies.append(json_frequencies[e]*0.01)
  return frequencies

frequencies = list_of_frequencies()

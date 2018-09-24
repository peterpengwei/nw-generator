#!/usr/bin/python

import os
import sys
import random

arg_len = len(sys.argv)

if arg_len != 4:
  print "usage python %s filename #pairs error_ratio".format(sys.argv[0])
  exit(1)

filename = sys.argv[1]
num_pairs = int(sys.argv[2])
error_ratio = float(sys.argv[3])

output = open(filename, 'w')

def generate_pair(error_ratio):
  first = []
  for i in range(0, 128):
    first.append(random.choice(['A', 'C', 'G', 'T']))
  second = []
  for i in range(0, 128):
    x = random.uniform(0, 1)
    if x > error_ratio:
      second.append(first[i])
    else:
      choices = ['A', 'C', 'G', 'T']
      choices.remove(first[i])
      tmp = random.choice(choices)
      second.append(tmp)
  return (first, second)

for i in range(0, num_pairs):

  str_pair = generate_pair(error_ratio)
  output.write(''.join(str_pair[0]) + '\n')
  output.write(''.join(str_pair[1]) + '\n')

output.close()

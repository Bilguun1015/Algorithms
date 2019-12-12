#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  a = ['rock', 'paper', 'scissors']
  if n == 0:
    return [[]]
  prevList = rock_paper_scissors(n-1)
  newList = []
  for item in prevList:
    rock = item[:].append(a[0])
    paper = item[:].append(a[1])
    scissors = item[:].append(a[2])
    newList.append(rock)
    newList.append(paper)
    newList.append(scissors)

  return newList


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


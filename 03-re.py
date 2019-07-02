#!/usr/bin/env python

import re

def main():
  string = "a123"
  pattern = re.compile('\d{2}')
  #pattern = re.compile('\d+')
  #pattern = re.compile('\d')
  ret = pattern.search(string)
  #ret = pattern.match(string)
  print ret.group()

if __name__ == "__main__":
  main()

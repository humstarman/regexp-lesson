#!/usr/bin/env python

import re

def main():
  string = """a123
    b456"""
  #pattern = re.compile('[0-9]')
  pattern = re.compile('[a-zA-Z0-9\s]+',re.S)
  ret = pattern.search(string)
  print ret.group()

if __name__ == "__main__":
  main()

#!/usr/bin/env python

import re

def main():
  string = """a161231651215b25352345234545b
    1243834723498B"""
  pattern = re.compile('a(.*)b',re.S|re.I)
  ret = pattern.findall(string)
  print ret

if __name__ == "__main__":
  main()

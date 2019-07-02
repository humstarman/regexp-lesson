#!/usr/bin/env python

import re

def main():
  string = "a161231651215b25352345234545b"
  pattern = re.compile('a(.*?)b')
  ret = pattern.findall(string)
  print ret

if __name__ == "__main__":
  main()

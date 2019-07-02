#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re

# <a href="http://www.xinhuanet.com/politics/2019-07/02/c_1124698571.htm" target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=1">习近平向2019世界新能源汽车大会致贺信 </a>

def main():
  string = """<a href="http://www.xinhuanet.com/politics/2019-07/02/c_1124698571.htm" target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=1">习近平向2019世界新能>源汽车大会致贺信 </a>"""
  pattern = re.compile('[\u4e00-\u9fa5]+')
  ret = pattern.findall(string)
  print(ret)

if __name__ == "__main__":
  main()

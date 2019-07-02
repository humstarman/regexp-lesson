#!/usr/bin/env python3

import requests 
import re

def main():
  #"https://3w.huanqiu.com/a/34f321/7NYDI8H4hUs?p=4&agt=8"
  base_url = "https://3w.huanqiu.com/a/34f321/7NYDI8H4hUs?p="
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
  }
  rets = [] 
  for i in range(4):
    j = i+1
    url = base_url + str(j) + """&agt=8"""
    resp = requests.get(url, headers=header)
    data = resp.content.decode("utf-8")
  
    pattern = re.compile("""<p>(.*)</p>""")
    ret = pattern.findall(data)
    rets.append(ret)
  print(rets)

if __name__ == "__main__":
  main()

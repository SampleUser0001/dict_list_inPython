# -*- coding: utf-8 -*-

def loop_dict(items):
  for key in items:
    print(items[key])

def loop_list(items):
  for i in range(len(items)):
    print(items[i])
    
if __name__ == '__main__':
  tmp_list = ['a','b','c']
  tmp_dict = {
    'key01': 'hoge',
    'key02': 'piyo'}
  
  loop_dict(tmp_dict)
  loop_list(tmp_list)
  
  # loop_dict(tmp_list)
  # loop_list(tmp_dict)
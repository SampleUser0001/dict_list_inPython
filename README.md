# dict list inPython

dictとlistを同じループで動かしたい。（無理ー）

listはint, dictはstringでループを回さないといけないから無理…ということだと思う。

## ソース

### loop_dict

``` python
def loop_dict(items):
  for key in items:
    print(items[key])
```

### loop_list

``` python
def loop_list(items):
  for i in range(len(items)):
    print(items[i])
```

## 実際に使ってみる

### loop_dict(tmp_list)

``` txt
loop_python | Traceback (most recent call last):
loop_python |   File "/opt/app/src/app.py", line 20, in <module>
loop_python |     loop_dict(tmp_list)
loop_python |   File "/opt/app/src/app.py", line 5, in loop_dict
loop_python |     print(items[key])
loop_python | TypeError: list indices must be integers or slices, not str
```

### loop_list(tmp_dict)

``` txt
loop_python | Traceback (most recent call last):
loop_python |   File "/opt/app/src/app.py", line 21, in <module>
loop_python |     loop_list(tmp_dict)
loop_python |   File "/opt/app/src/app.py", line 9, in loop_list
loop_python |     print(items[i])
loop_python | KeyError: 0
```


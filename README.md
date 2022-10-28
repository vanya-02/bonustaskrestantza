Console output upon running:

`server1`:
```
┌──(vanya㉿vanya)-[~/Documents/pr]
└─$ /usr/bin/python /home/vanya/Documents/pr/server1.py                                                                                                                                                130 ⨯
 * Serving Flask app 'server1' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5001/ (Press CTRL+C to quit)
[{'thread': 1, 'ii': 1}]
127.0.0.1 - - [28/Oct/2022 09:30:22] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}]
127.0.0.1 - - [28/Oct/2022 09:30:22] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}]
127.0.0.1 - - [28/Oct/2022 09:30:23] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}]
127.0.0.1 - - [28/Oct/2022 09:30:25] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}]
127.0.0.1 - - [28/Oct/2022 09:30:26] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}]
127.0.0.1 - - [28/Oct/2022 09:30:28] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}]
127.0.0.1 - - [28/Oct/2022 09:30:28] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}]
127.0.0.1 - - [28/Oct/2022 09:30:29] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}]
127.0.0.1 - - [28/Oct/2022 09:30:29] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}]
127.0.0.1 - - [28/Oct/2022 09:30:30] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}]
127.0.0.1 - - [28/Oct/2022 09:30:31] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}]
127.0.0.1 - - [28/Oct/2022 09:30:32] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}]
127.0.0.1 - - [28/Oct/2022 09:30:33] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}]
127.0.0.1 - - [28/Oct/2022 09:30:34] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}]
127.0.0.1 - - [28/Oct/2022 09:30:36] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}]
127.0.0.1 - - [28/Oct/2022 09:30:36] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}, {'thread': 0, 'ii': 17}]
127.0.0.1 - - [28/Oct/2022 09:30:37] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}, {'thread': 0, 'ii': 17}, {'thread': 2, 'ii': 18}]
127.0.0.1 - - [28/Oct/2022 09:30:38] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}, {'thread': 0, 'ii': 17}, {'thread': 2, 'ii': 18}, {'thread': 1, 'ii': 19}]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}, {'thread': 0, 'ii': 17}, {'thread': 2, 'ii': 18}, {'thread': 1, 'ii': 19}, {'thread': 0, 'ii': 20}]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
[{'thread': 1, 'ii': 1}, {'thread': 0, 'ii': 2}, {'thread': 1, 'ii': 3}, {'thread': 1, 'ii': 4}, {'thread': 1, 'ii': 5}, {'thread': 2, 'ii': 6}, {'thread': 2, 'ii': 7}, {'thread': 3, 'ii': 8}, {'thread': 0, 'ii': 9}, {'thread': 1, 'ii': 10}, {'thread': 1, 'ii': 11}, {'thread': 0, 'ii': 12}, {'thread': 0, 'ii': 13}, {'thread': 1, 'ii': 14}, {'thread': 0, 'ii': 15}, {'thread': 3, 'ii': 16}, {'thread': 0, 'ii': 17}, {'thread': 2, 'ii': 18}, {'thread': 1, 'ii': 19}, {'thread': 0, 'ii': 20}, {'thread': 0, 'ii': 21}]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
```

`server2`:
```
┌──(vanya㉿vanya)-[~/Documents/pr]
└─$ /usr/bin/python /home/vanya/Documents/pr/server2.py
 * Serving Flask app 'server2' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5002/ (Press CTRL+C to quit)
{'thread': 5, 'counter': 1}
[1]
127.0.0.1 - - [28/Oct/2022 09:30:20] "POST /api HTTP/1.1" 200 -
{'thread': 4, 'counter': 2}
[1, 2]
127.0.0.1 - - [28/Oct/2022 09:30:21] "POST /api HTTP/1.1" 200 -
{'thread': 5, 'counter': 3}
[]
127.0.0.1 - - [28/Oct/2022 09:30:23] "POST /api HTTP/1.1" 200 -
{'thread': 3, 'counter': 4}
[]
127.0.0.1 - - [28/Oct/2022 09:30:25] "POST /api HTTP/1.1" 200 -
{'thread': 4, 'counter': 5}
[]
127.0.0.1 - - [28/Oct/2022 09:30:26] "POST /api HTTP/1.1" 200 -
{'thread': 2, 'counter': 6}
[]
127.0.0.1 - - [28/Oct/2022 09:30:28] "POST /api HTTP/1.1" 200 -
{'thread': 4, 'counter': 7}
[7]
127.0.0.1 - - [28/Oct/2022 09:30:28] "POST /api HTTP/1.1" 200 -
{'thread': 1, 'counter': 8}
[]
127.0.0.1 - - [28/Oct/2022 09:30:29] "POST /api HTTP/1.1" 200 -
{'thread': 3, 'counter': 9}
[]
127.0.0.1 - - [28/Oct/2022 09:30:29] "POST /api HTTP/1.1" 200 -
{'thread': 0, 'counter': 10}
[]
127.0.0.1 - - [28/Oct/2022 09:30:30] "POST /api HTTP/1.1" 200 -
{'thread': 3, 'counter': 11}
[]
127.0.0.1 - - [28/Oct/2022 09:30:32] "POST /api HTTP/1.1" 200 -
{'thread': 5, 'counter': 12}
[]
127.0.0.1 - - [28/Oct/2022 09:30:32] "POST /api HTTP/1.1" 200 -
{'thread': 5, 'counter': 13}
[]
127.0.0.1 - - [28/Oct/2022 09:30:34] "POST /api HTTP/1.1" 200 -
{'thread': 5, 'counter': 14}
[]
127.0.0.1 - - [28/Oct/2022 09:30:34] "POST /api HTTP/1.1" 200 -
{'thread': 0, 'counter': 15}
[]
127.0.0.1 - - [28/Oct/2022 09:30:36] "POST /api HTTP/1.1" 200 -
{'thread': 4, 'counter': 16}
[]
127.0.0.1 - - [28/Oct/2022 09:30:37] "POST /api HTTP/1.1" 200 -
{'thread': 1, 'counter': 17}
[]
127.0.0.1 - - [28/Oct/2022 09:30:37] "POST /api HTTP/1.1" 200 -
{'thread': 2, 'counter': 18}
[]
127.0.0.1 - - [28/Oct/2022 09:30:38] "POST /api HTTP/1.1" 200 -
{'thread': 0, 'counter': 19}
[]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
{'thread': 1, 'counter': 20}
[]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
{'thread': 3, 'counter': 21}
[]
127.0.0.1 - - [28/Oct/2022 09:30:39] "POST /api HTTP/1.1" 200 -
^C^CException ignored in: <module 'threading' from '/usr/lib/python3.10/threading.py'>
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1567, in _shutdown
    lock.acquire()
KeyboardInterrupt: 
```

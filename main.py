import requests, json, time, msvcrt
from collections import deque
with requests.Session() as s:
  dq = deque()
  account = [{
    'username': 'username', #change this
    'password': 'password' #this too
  }]
  auth = []
  p = s.post('https://codefun.vn/api/auth', data = account[0]) #i dont have the api so i "borrowed" it from somebody
  text = json.loads(p.text)
  print(text)
  auth.append(text["data"])
  done = False
  cur = ""
  last = time.time() - 93 #for first submit
  while not done:
    if msvcrt.kbhit(): #kills on ctrl + c. or any combination idk
      ch = msvcrt.getche() #for some reason doesnt erase after backspace entered
      if ch == b'\r':
        dq.append(cur) #need to check cur too ughhhhh
        print(f"{cur} added to queue\n")
        cur = ""
      elif ch == b'\x08': #handling erase
        if cur:
          cur = cur[:-1]
      else:
        ballsack = ch.decode('ASCII')
        cur += ballsack
    if dq: #look at me. i'm a motherfucking deque user who uses it in python.
      piss = time.time()
      if piss - last >= 93: #delaying submit, must be at least 90
        pr = dq[0]
        try:
          fd = open(f"{dq[0]}.cpp") #very important, change the file extension to your language or whatever
        except OSError: 
          print(f"can't read {dq[0]}.cpp, mate\n") #you can change the text of ts if you want
          continue
        submit = {
          'code': fd.read(), 
          'language': 'C++', #change this to c++ or py or whatever. look in the submit page
          'problem': f'{pr}'
        }
        r = s.post('https://codefun.vn/api/submit',
        headers = {'Authorization': 'Bearer ' + auth[0]}, 
        data = submit)
        print(f"submitted {dq[0]}.cpp\n") #same here
        last = piss
        dq.popleft()
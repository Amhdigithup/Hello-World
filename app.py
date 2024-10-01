# im searching for some one to adjest my code and conteribe with me to init this repo
import termcolor
import random

def log(d):
    datas = d.split(' ')
    colors = list(termcolor.COLORS.keys())
    fainltext = ''
    for d in datas:
        fainltext += termcolor.colored(d,random.choice(colors))
    print(fainltext)

msg = ' Hello World'
for i in range(10):
    log(msg * i)
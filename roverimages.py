import requests
import webbrowser
import sys
from random import randint

key = "LlgNiDnuThl6Btx89hbHZljZbm1HYCD2p7n41gwI"

camlist = ["FHAZ", "RHAZ", "FHAZ", "RHAZ", "FHAZ", "RHAZ", "MAHLI", "MARDI", "NAVCAM", "NAVCAM", "NAVCAM", "PANCAM", "MINITES"]
roverlist = ["curiosity", "opportunity", "spirit"]

def make_req(sol, key, camlist, roverlist):
    cam = camlist[randint(0, len(camlist) - 1)]
    sol = sol
    rover = roverlist[randint(0, len(roverlist) - 1)]
    
    URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/"+rover+"/photos?sol="+str(sol)+"&api_key="+key+"&camera="+cam
    
    try:
        print("Attempting Request \n")
        res = requests.request(url=URL, method="GET").json()
        photoToOpen = randint(0, len(res["photos"]) - 1)
        print("Request Info \n --------------- \n", "URL:", URL, "\n", "Rover:", rover, "\n", "SOL:", sol, "\n", "Earth Date:", res["photos"][photoToOpen]["earth_date"], "\n", "Camera:", cam, "\n")
        webbrowser.open_new_tab(res["photos"][photoToOpen]["img_src"])
    except:
        print("Image not found.. Trying another")
        make_req(sol, key, camlist, roverlist)

if len(sys.argv) > 1:
    numOPhotos = sys.argv[1]
else:
    numOPhotos = 1

for i in range(int(numOPhotos)):
    make_req(randint(1, 2000), key, camlist, roverlist)
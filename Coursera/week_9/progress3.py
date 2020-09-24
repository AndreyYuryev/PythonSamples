from tqdm import tqdm
import time

myList = []
for pr in range(100):
    myList.append(pr)
#  myList = [1,2,3,4,5,6,7,8,9,10]
for i in tqdm(myList):
    time.sleep(0.2)

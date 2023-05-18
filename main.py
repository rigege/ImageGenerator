from PIL import Image
from functions import mergeSort, evolveGen, shapeGen
import time

starttime = time.perf_counter()

target, img = Image.open("ImageGenerator/img.jpg").convert("RGB"), Image.new("RGB", (100,100))  # opening target image, and setting placeholder "img" variable

best, height, width = 256, target.height, target.width    # int values used - "best" is placeholder vairable

for iteration in range(2500):   #loop that repeatedly places objects 
    objarray = []   # array that stores the objects as dictionaries
   
    for x in shapeGen(target, img, iteration, height, width, starttime):    # generator for initial 500 objects
        objarray.append(x)
     
    #print("initial objects generated: " + str(time.perf_counter() - starttime))

    mergeSort(objarray)
    
    #print("sorting/evolving: " + str(time.perf_counter() - starttime))
    
    for evolved in range(200):  # loop for repeated evolution
        del objarray[30:]   # keeping first 50 objs in sorted array and deleting the rest
        for y in evolveGen(objarray, target, img, iteration,  height, width):   # generator for evolution of objects
            objarray.append(y)  
        mergeSort(objarray)
    
    #print("done sort/evolve: " + str(time.perf_counter() - starttime))
    
    if (objarray[0]["value"] < best):   # checks if new object placed make image closer to target than previous iteration, if not, image is reverted to previous iteration
        img = objarray[0]["image"]
        best = objarray[0]["value"]
    print("Objects Placed: " + str(iteration + 1))
    
img.save("ImageGenerator/result.jpg")
from PIL.ImageStat import Stat
from PIL.ImageChops import difference
from PIL import ImageDraw, Image
from random import randint
import time

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if (L[i]["value"] < M[j]["value"]):
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
                        
def shapeGen(target, img, iteration, height, width, starttime):
    #print("creating inital objects: " + str(time.perf_counter() - starttime))
    
    for objs_created in range(300): # loops for creating 500 objs
        
        x = (randint(0, width) ,randint(0, width))  # generating x and y coordinates
        y = (randint(0, height) ,randint(0, height))
        
        x0, x1, y0, y1 = min(x), max(x), min(y), max(y)
        
        colour = (randint(0, 255), randint(0, 255), randint(0, 255))    # generating colour
        
        if (iteration==0):
            new = Image.new("RGB", (width, height))
        else:
            new = img.copy()
        
        draw = ImageDraw.Draw(new)
        draw.ellipse((x0, y0, x1, y1), colour, colour)  # drawing the object on the image
        
        objects = {}    # empty dictionary that will store the object data
        
        objects["image"] = new
        objects["xy"] = (x0, y0,x1, y1)
        objects["colour"] = colour
        diff = difference(target, new).convert("L") # measuring difference from target
        objects["value"] = Stat(diff).mean[0]
        
        yield objects   

def evolveGen(array, target, img, iteration,  height, width):  
    child = 0   # keeps track of children of each obj in array
    for obj in array:
        while (child<10):
            
            if (iteration==0):
                new = Image.new("RGB", (width, height))
            else:
                new = img.copy()
                
            draw = ImageDraw.Draw(new)
            
            newx = (obj["xy"][0] + randint(-round(width/8), round(width/8)) ,obj["xy"][2] + randint(-round(width/8), round(width/8)))
            newy = (obj["xy"][1] + randint(-round(height/8), round(height/8)) ,obj["xy"][3] + randint(-round(height/8), round(height/8)))
            
            newx0, newx1, newy0, newy1 = min(newx), max(newx), min(newy), max(newy)
            
            newcol = (obj["colour"][0] + randint(-30, 30), obj["colour"][1] + randint(-30, 30), obj["colour"][2] + randint(-30, 30))
            
            draw.ellipse((newx0, newy0, newx1, newy1), newcol, newcol)
            
            objs = {}
            
            objs["image"] = new
            objs["xy"] = (newx0, newy0, newx1, newy1)
            objs["colour"] = newcol
            diff = difference(target, new).convert("L")
            objs["value"] = Stat(diff).mean[0]
            
            child+=1
            
            #print("child yielded: " + str(child))
            
            yield objs          
Image Generator

May 17th, 2023
________________________________________________________________________________

To use the image generator
- Place the target image in the "ImageGenerator" folder
- Name the image "img.jpg", if the img is in PNG format or under a different name, change line 7 of the "main.py" file to open the name of your image
- Run the "main.py" afterwards

Notes
- Various "print()" functions are commented out throughout that will print to console what stage the program is at, and time since starting it in seconds, can be used to troubleshoot
- The generator only uses ellipses at the moment
- Generating one object can take up to 30sec, but usually around 15-12sec
- Certain images may be slower or faster
- By default, 2500 objects are generated onto the image
- Values in the "main.py" and "functions.py" may be changed based on your own preference
- The final image will be saved in the "ImageGenerator" folder as "result.jpg", this may have to be changed to PNG on line 36 of "main.py" if your target image is a PNG

Thoughts
- I know that this can be more efficient, and am open to hearing ways to improve it 
- There are ways to improve it that I do not currently have the skills to implement, but it is something I can come back to in the future 
- This will likely be updated to include other shapes, and custom textures as well
# ASCII-Art-Generator
# ASCII-Art-Generator-
This python script is use to convert photos and video into ascii art.
## TABLE OF CONTENTS-
 * How to run the project with all dependencies
 * The Internal working of project
 * Learning takeaways from this project
 * References used while working on the project
 
## HOW TO RUN THE PROJECT WITH ALL DEPENDENCIES-
We need to install some python packages for the working of this project:
* Numpy
* Pillow
* Open CV
* Glob
This project requires image file/video file along with font file in the same folder.
## THE INTERNAL WORKING OF THE PROJECT
To convert video to ASCII art,capture each and every frame of the video after that add up the number of frames in the video.
```
video=cv2.VideoCapture("sample_video2.mp4")
add=0;
f=1;
while f:
  f,image=video.read()
  try:
     cv2.imwrite("image/frame%d.jpg"%add,image)
     expect:
       break
       add=add+1
 ```
 Now lets change all the captured frames to ASCII Art
 Firstly,set the background colour
 ```
 background="white"
 if background=="white":
     background_code=(255,255,255)
     elif background=="black":
      background_code=(0,0,0)
 ```
 Now resize all the images for that take the height and width of each image , to calculate height and width of each image and to make a new image using PIL
 after that map the characters to generate ASCII art,then check for the background colour and upturn as well as crop the output image respectively finally save this   
 output image.
 consecutively accumulate each image to image array and reserve this in an result video file.
 ```
 image_array=[]
 for filename in glob.glob('outputImage/*.jpg'):
   my_image=cv2.imread(filename)
   height,width,layers=my_image.shape
   size=(width,height)
   image_array.append(my_image)
   
   result=cv2.VideoWriter('OutputVideo.av1',cv2.VideoWriter_fourcc(*"DIVX"),25,size)
   
   for k in range(len(image_array)):
       result.write(image_array[k])
   ```
   Our ASCII Art video is ready.
   
   ## LEARNINGS TAKEAWAYS FROM THIS PROJECT
   * We have learned to work with numerous python packages such as pillow and open cv.
   * we have learned to read an image file and video file.
   * we have learned to transform an image as well as video to ASCII Art.
    
   ## REFERENCES USED WHILE WORKING ON THE PROJECT
   * https://medium.com/analytics-vidhya/the-ultimate-handbook-for-opencv-pillow-72b7eff77cd7
   * https://docs.opencv.org/4.x/d7/dbd/group_imgproc.html
   * https://learnopencv.com
   * https://betterprogramming.pub

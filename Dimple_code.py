import cv2
import numpy as np
import glob
from PIL import Image, ImageDraw, ImageOps, ImageFont


Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

video=cv2.VideoCapture("sample_video2.mp4")
add=0
f=1
while f:
    f,image=video.read()
    try:
        cv2.imwrite("images/frame%d.jpg"%add,image)
    except:
        break
    add+=1


def get_data(mode):
    font=ImageFont.truetype("arial.ttf",size=20)
    scale=2
    char_list=Character[mode]
    return char_list, font, scale


background = "white"
if background == "white":
    background_code = (255,255,255)
elif background == "black":
    background_code = (0,0,0)


char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300


for l in range(add):
    image=cv2.imread("images/frame%d.jpg"%l)
    height, width, _ =image.shape
    cell_w=width / num_cols
    cell_h=scale * cell_w
    num_rows=int(height / cell_h)
    char_width, char_height=font.getsize("A")
    out_width=char_width * num_cols
    out_height=scale * char_height * num_rows
    out_image=Image.new("RGB", (out_width, out_height), background_code)
    draw=ImageDraw.Draw(out_image)
    for i in range(num_rows):
        for j in range(num_cols):
            partial_image=image[int(i*cell_h) :min(int((i+1)*cell_h),height),int(j*cell_w) :min(int((j+1)*cell_w),width),]
            partial_avg_color=np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
            partial_avg_color=tuple(partial_avg_color.astype(np.int32).tolist())
            c=char_list[min(int(np.mean(partial_image)*num_chars/255), num_chars-1)]
            draw.text((j*char_width, i*char_height),c,fill=partial_avg_color, font=font)
    if background=="white":
        cropped_image=ImageOps.invert(out_image).getbbox()
    elif background=="black":
        cropped_image=out_image.getbbox()
    out_image=out_image.crop(cropped_image)
    out_image.save("outputImage/out%d.jpg"%l)
    

image_array=[]
for filename in glob.glob('outputImage/*.jpg'):
    my_image=cv2.imread(filename)
    height,width,layers=my_image.shape
    size=(width,height)
    image_array.append(my_image)


result=cv2.VideoWriter('OutputVideo.avi',cv2.VideoWriter_fourcc(*"DIVX"),25,size)
 
for k in range(len(image_array)):
    result.write(image_array[i])


result.release()

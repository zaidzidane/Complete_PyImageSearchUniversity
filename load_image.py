import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="input file path")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
print(image.shape)
(h,w,c)=image.shape[:3]

print(f"width:{w} pixels")
print(f"height:{h} pixels")
print(f"channels:{c} pixels")


cv2.imshow("Image",image)
cv2.waitKey(10) 
cv2.imwrite("newimage.jpg",image)



import pixellib
import numpy as np
import cv2
import os
import keyboard
import time
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
from pixellib.semantic import semantic_segmentation

# Initialize video capture instance
cap = cv2.VideoCapture(0)

# Initialize image segmentation model
segment_image = semantic_segmentation()
segment_image.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

while(True):
    #Capture frame by frame
    ret, frame = cap.read()

    if keyboard.is_pressed('c'):
        start = time.time()
        cv2.imwrite("raw.jpg", frame)
        segmap, segoverlay = segment_image.segmentAsPascalvoc("raw.jpg" , overlay= True)
        cv2.imshow('Segmented', segoverlay)
        end = time.time()
        print(f"Inference Time: {end-start:.2f} seconds")

    #Display the webcame frame
    cv2.imshow('Raw', frame)

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
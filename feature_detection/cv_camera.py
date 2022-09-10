import cv2
import numpy as np


def shi_tomasi(image):
    #Converting to grayscale
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #Specifying maximum number of corners as 1000
    # 0.01 is the minimum quality level below which the corners are rejected
    # 10 is the minimum euclidean distance between two corners
    corners_img = cv2.goodFeaturesToTrack(gray_img,1000,0.01,50)
    corners_img = np.int0(corners_img)
    out_img=image.copy()
    for corners in corners_img:
       
        x,y = corners.ravel()
        #Circling the corners in green
        cv2.circle(out_img,(x,y),3,(0,255,0),-1)

    return out_img

def main():
    vid = cv2.VideoCapture(0)
  
    while(True):
      
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
 
        out_shi=shi_tomasi(frame)
         # Display the resulting frame
        cv2.imshow('frame',out_shi)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
        # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
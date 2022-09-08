from cgitb import grey
import cv2
import numpy as np 

def main(): 
    vid = cv2.VideoCapture(0)
    
    while(True):
        
        ret, frame = vid.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert to HSV 
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale color representation
        
        mask_greensoft = cv2.inRange(hsv, (90, 10, 100), (105, 255, 255)) # Given a range of values from HSV min and max values divided 2
        #mask_pink = cv2.inRange(hsv, (150, 10, 100), (165, 255, 255))
        
        target = cv2.bitwise_and(frame, frame, mask=mask_greensoft) 
        #target2 = cv2.bitwise_and(frame, frame, mask=mask_pink)
        
        edges = cv2.Canny(grey, 50, 100) # edges detection 
        output = np.hstack((grey, edges)) # Sort arrays grey and edges 
        
        #*Display the resulting frame
        cv2.imshow('frame', target)  # Display the outpur variable
        
        #cv2.imshow('frame2', target2)    
             
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    vid.release()
    
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
# software-practicing-python

Here i put codes that i wrote in the past as practice
either for online courses or for platforms like hackerrank or something

Here are some notable learnings

### non library specific
1) getattr(arr,command)(*n) --> from practice number 6.                    
the *n operator is iterating operator.                      
getattr will retrieve the type of the input and allow you to work on it like a variable                       
eg here, arr is a list, and command can be "append" or "pop".                   
getattr gets the variable type of arr, which is list.


### opencv
1) img = cv2.imread(imgfile)
2) img.shape     -- this is actually a numpy command, img.shape[0] --> height, img.shape[1] --> width
3) img.dtype     -- returns type of varialbe
4) cv2.imshow('name of window', img_variable)
5) cv2.waitKey(0)     -- imshow() should be followed by function waitKey(), which specifies how long the image should be specified in milliseconds
6) cv2.destroyAllWindows()      -- you need to do this else cv2.imshow won't work again in the same run
7) For a colour image, imread() gives a 3D numpy array in BGR format
     - img[:,:,0] --> Blue channel
     - img[:,:,1] --> Green channel
     - img[:,:,2] --> Red channel
8) cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)      -- many conversion codes, see their docs
9) cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)      -- convert grayscale back to BGR, but actually just copies the vals to 3 channels, you wont get back your colour information
10) cv2.merge(imgc1, imgc2, imgc3)      -- stack the channels together
11) cv2.copyMakeBorder(img, top, btm, left, right, borderType)      --  cv2.BORDER_REPLICATE, cv2.BORDER_REFLECT, cv2.BORDER_WRAP,  cv2.BORDER_CONSTANT
12) cv2.line
13) cv2.circle
14) cv2.rectangle
15) cv2.ellipse
16) cv2.putText
17) cv2.resize      -- common methods cv2.INTER_AREA, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_NEAREST
18) cv2.affine(img, transform_matrix, (output height,output width))
19) cv2.getRotationMatrix2D
20) cv2.equalizeHist      -- histogram equalisation, gives less confusing edges when doing edge detection
21) cv2.createCLAHE()      -- CLAHE Contrast limited adapative histogram equalisation, visually clearer
     clahe.apply(img)
22) cv2.threshold          -- remember Otsu thresholding too
23) cv2.filter(img, intensity, kernel)      -- for filtering using self defined kernel... convolutions
24) cv2.blur(img, (kernelsize,kernelsize))      -- mean filtering
25) cv2.GaussianBlur(img, (kernelsize,kernelsize), val)      -- val is sigma value, set to 0 to let opencv decide
26) cv2.medianBlur
27) To sharpen image...where nuc is image file. Values are not fixed, just an example
> krn = np.ones((11,11),np.float32)/121
> mnuc = cv2.filter2D(nuc,-1,krn)
> sharpen = (np.float32(nuc)*2 - np.float32(mnuc))/255
> Note: sharpening introduces noise into image
28) canny_edges = cv2.Canny(img, minval, maxval, 3)      -- last argument is kernel size, usually defaults to 3, can use 5 or 7 too
> contours = cv2.findContours     -- find contours
> cv2.drawContours     -- draw contours

29) Haar Cascade classifier/Viola Jones algorithm
> fce = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #or whatever xml file
> face= fce.detectMultiScale(img, scaleFactor, minNeighbours)
> sml = cv2.CascadeClassifier('haarcascade_smile.xml')      # or whatever your xml file name is
> smle= sml.detectMultiScale(fcb, scaleFactor=1.3, minNeighbors=10) # or whatever numbers

30) CaffeModel/GoogLeNet
> prototxt = 'bvlc_googlenet.prototxt'
> caffemodel= 'bvlc_googlenet.caffemodel'
> net = cv2.dnn.readNetFromCaffe(prototxt,caffemodel)
> blob = cv2.dnn.blobFromImage(image=img, scalefactor, outputsize, mean, swapRB, crop)
> net.setInput(blob)
> preds = net.forward()

31) cv2.dilate     -- grow everything    
32) cv2.erode     -- shave off from everything

33) yolov3 in opencv
> yoloconfig = 'yolov3.cfg'
> yoloweights= 'yolov3.weights'
> net = cv2.dnn.readNet(yoloweights,yoloconfig)
> blob = cv2.dnn.blobFromImage(image=img, scalefactor, outputsize, mean, swapRB, crop)
> net.setInput(blob)
> outLyrs = getOutputLayers(net)  #get output layers
> preds = net.forward(outLyrs)      #Run the actual object detection.
> cv2.dnn.NMSBoxes(bboxes=boxes, scores=confidences, score_threshold=scoreThres, nms_threshold=nmsThres) #do non max suppression

34) cv2.morphologyEx

### For Morphological snake 
### morphsnakes as ms
1) ms.inverse_gaussian_gradient(img, alpha, sigma)
2) ms.circle_level_set(img.shape, (centerx, centery), radius)
3) ms.visual2d      -- visualisation callback
4) ms.morphological_geodesic_active_contour(inversegauss, iterations, init, smoothing, threshold, balloon, iter_callback=back)

### matplotlib.pylot as plt
1) plt.axis('on') or plt.axis('off')
2) plt.imshow
3) plt.show
4) plt.hist.img.ravel()

### numpy
1) np_array = numpy.array(arr, float)  --> converts a list called arr into a numpy array, you can specify the value type. Eg float int double 
2) np.transpose 
3) np.matmul --> to do matrix multiplication on 2 matrices (max is 2 for this function)
4) np.array --> to convert a list into an array 
5) np.linalg.inv --> to calculate the inverse of a matrix
6)  @ operator --> usin the @ operator lets you do multiple matrix multiplcations in 1 line in that specified order                         
     eg   Pmatrix = np.linalg.inv( np.matmul(np.matmul(H_trans, R_inv), Hmatrix))              
          Pmatrix = np.linalg.inv( H_trans @ R_inv @ Hmatrix)              
          These 2 lines are equivalent in their operation             

### Reading input from stdin
1) a = int(input())  ---> this reads the input and convert into a int. Else it is a string.         
2) rooms = input().split() ----> splits a long input in a list. For eg,  1 4 5 a b c  becomes '1', '4', '5', 'a', 'b', 'c'   

### strings
1) string.isalnum() 
2) str.isalpha()
3) str.islower()
4) str.isupper()
5) str.ljust(width, padding_chars)
6) str.rjust(width, padding_chars)
7) str.center(width, padding_chars)
8) str.join() --> see #https://www.w3schools.com/python/ref_string_join.asp 

### numbers (int, octa, hexadecimal, binary) 
normal = str(i)               
octal = format(i,'o')                   
hexa = format(i, 'X')              
binary = format(i, 'b')                 

        
### dictionary
1)  dictonary_name.items()  gives you key (key, value) tuples:

### collections  
import collections       
from collections import Counter   #https://www.geeksforgeeks.org/python-collections-module/    
> print(Counter(['B','B','A','B','C','A','B','B','A','C']))   #Counter gives you a dictionary                    
> {'B': 5, 'A': 3, 'C': 2}         

### sets vs list
sets only retain unique values, list retains whatever you put in        
scores_set = set(scores)  #set only retains unique values, you can convert a list into a set like that 

### itertools
itertools.product() 


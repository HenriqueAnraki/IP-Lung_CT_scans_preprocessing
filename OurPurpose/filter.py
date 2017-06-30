#Marcus Araujo, Nusp 9005871
#Henrique Caetano Anraki, Nusp 8643412
#Ítalo Tobler Silva, Nusp 8551910

#Image Processing - image generator 

import sys
import string
import cv2
import numpy as np
import math
import random
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



def showHistogram (vector):


    n, bins, patches = plt.hist(vector);

    plt.grid(True);
    plt.show();
    return 0;


def imLog (img):

    img_log = np.float32(img);
    (pixel_min, pixel_max, tmp1, tmp2) = cv2.minMaxLoc(img_log);
    R= pixel_max;
    c= 255/np.log(1+R);
    img_log = cv2.log(1+img_log);
    img_log = cv2.multiply(img_log, c);
    img_log = cv2.convertScaleAbs(img_log)

    return img_log;

def imHistogram (img):
    img_hist = np.int32(img);
    m,n = img.shape;
    vector = np.zeros(256);
    for i in range (0,m):
        for j in range (0,n):
            vector[int( img[i][j] ) ] = vector[int( img[i][j] ) ]  +1;


    return vector;

def DoesItBelongToPeriod(value, a, b):
    if (a <= value and b>=value ):
        return True;
    else:
        return False;


def BoardHistogram(img):

    img_hist = np.int32(img);
    lin, col = img.shape;
   
    countOut = countIn = 0;

    delta = np.std(img)/2;
   
    vector = np.zeros(256*2);
    for i in range(0,lin):
        
        for j in range (0,col):
            n=s=w=o=0;
            
            #check north 
            if (j-1>=0):
                if(DoesItBelongToPeriod((int (img[i][j])), (int (img[i][j-1])) - delta, (int (img[i][j-1])) + delta)):
                    n =1;
            else:
                n =1;
            
            #check east 
            if (j+1< col):
                if(DoesItBelongToPeriod((int (img[i][j])), (int (img[i][j+1])) - delta, (int (img[i][j+1])) + delta)):
                    s =1;
            else:
                s =1;
            #check west
            if (i+1<lin):
                if(DoesItBelongToPeriod((int (img[i][j])), (int (img[i+1][j])) - delta, (int (img[i+1][j])) + delta)):
                    w =1;
            else:
                w =1;

            #check inferior 
            if (i-1>=0):
                if(DoesItBelongToPeriod((int (img[i][j])), (int (img[i-1][j])) - delta, (int (img[i-1][j])) + delta)):
                    o =1;
            else:
                o =1;

            if((n==1) and (s ==1) and (w == 1) and  (o == 1)):
                countIn = countIn +1; 
                vector[(int( img[i][j] )) ] = vector[(int( img[i][j] )) ]  +1;

            else:
                countOut = countOut +1;
                vector[(int( img[i][j] )) + 256 ] = vector[(int( img[i][j] )) + 256 ]  +1;
    
    return vector;
# ------ main ----- 



if (sys.argv[1] == "--help"):
    print("run with : [class file] [images directory] [output path] [filer type] ");
else:
    #input
    
    #file containing images' path 
    indexPath = open( sys.argv[1] ); 
    features = open (sys.argv[3] + "features.csv", "w");


    # while index path is not done: 
    while( True ):
        filename = str (indexPath.readline() );
        
    # break when end of file
        if (filename == ""):  
            break;

        # line format : image name, class
        filename = (filename.split(","))[0];
        # image path generator
        aux_open = sys.argv[2] + filename;
        if(sys.argv[5] =="status"):
            print("current image: "+ aux_open);

        
        #open image 
        img = cv2.imread( aux_open, cv2.IMREAD_GRAYSCALE);
        
        #apply filter
            
	if (sys.argv[4] == "Histogram"): #simple histogram 
            
            
	    histogram = imHistogram(img);
	            	       
            features.write("0");           
            for i in range (len(histogram)):
                features.write("," + str(histogram[i]));
            
            features.write(","+ ((filename.split("_"))[1]).replace(".jpg", ""));
            
 	    features.write("\n");   
	
	elif(sys.argv[4] == "log"): # logarithm function applied to pixels 
            
	    img_log = imLog(img);
        
	    histogram = imHistogram(img_log);
	            	       
            features.write("0");           
            for i in range (len(histogram)):
                features.write("," + str(histogram[i]));
            
            features.write(","+ ((filename.split("_"))[1]).replace(".jpg", ""));
            
 	    features.write("\n"); 

                       
            features.write("0");           

            for i in range (len(histogram)):

                features.write("," + str(histogram[i]));

            features.write(","+ ((filename.split("_"))[1]).replace(".jpg", ""));

            features.write("\n");    
	
	elif (sys.argv[4] == "boardHistogram"): # histogram of intern and extern pixels 

            img_log = imLog(img);

            histogram = BoardHistogram(img_log);
	            	       
            features.write("0");           
            for i in range (len(histogram)):
                features.write("," + str(histogram[i]));
            
            features.write(","+ ((filename.split("_"))[1]).replace(".jpg", ""));
            
 	    features.write("\n"); 

                       
            features.write("0");           

            for i in range (len(histogram)):

                features.write("," + str(histogram[i]));

            features.write(","+ ((filename.split("_"))[1]).replace(".jpg", ""));

            features.write("\n");

        else:
            print("no filter applied");
            break;



       
    indexPath.close();
    features.close();


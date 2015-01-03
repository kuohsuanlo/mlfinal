# resize(path,outpath):
# Function parameter 
#	1. path : absolute path of the original image,  like '/Home/projects/final/image/21.jpg'
#	2. path : absolute intented path of the output image 
#	3. sizeOfW, integer, the size of the output image's width
#	4. sizeOfH, integer, the size of the output image's height
#

def resize(path,outpath,sizeOfW,sizeOfH):
	from PIL import Image
	import numpy
	im = Image.open(path)
	imarray = numpy.array(im)

	TopFirstI=0
	TopFirstJ=0
	LeftFirstI=0
	LeftFirstJ=0
	DownFirstI=0
	DownFirstJ=0
	RightFirstI=0
	RightFirstJ=0

	RGBThreshold = 25;

	for i in range(0,im.size[0]-1,1):
		for j in range(0,im.size[1]-1,1):
			rgbAdded = 0;
			rgbAdded = rgbAdded + imarray[j][i]
			if(rgbAdded>=RGBThreshold):
				TopFirstI=i
				TopFirstJ=j



	for j in range(0,im.size[1]-1,1):
		for i in range(0,im.size[0]-1,1):
			rgbAdded = 0;
			rgbAdded = rgbAdded + imarray[j][i]
			if(rgbAdded>=RGBThreshold):
				LeftFirstI=i
				LeftFirstJ=j



	for i in xrange(im.size[0]-1,0,-1):
		for j in xrange(im.size[1]-1,0,-1):
			rgbAdded = 0;
			rgbAdded = rgbAdded + imarray[j][i]
			if(rgbAdded>=RGBThreshold):
				DownFirstI=i
				DownFirstJ=j



	for j in xrange(im.size[1]-1,0,-1):
		for i in xrange(im.size[0]-1,0,-1):
			rgbAdded = 0;
			rgbAdded = rgbAdded + imarray[j][i]
			if(rgbAdded>=RGBThreshold):
				RightFirstI=i
				RightFirstJ=j

	if(TopFirstI>LeftFirstI):
		RightDownI = TopFirstI
	else :
		RightDownI = LeftFirstI

	if(TopFirstJ>LeftFirstJ):
		RightDownJ = TopFirstJ
	else:
		RightDownJ = LeftFirstJ

	if(DownFirstI<RightFirstI):
		LeftTopI = DownFirstI
	else :
		LeftTopI = RightFirstI

	if(DownFirstJ<RightFirstJ):
		LeftTopJ = DownFirstJ
	else:
		LeftTopJ = RightFirstJ

	#print 'TF i,j : (',LeftTopI,',',LeftTopJ,')'
	#print 'RD i,j : (',RightDownI,',',RightDownJ,')'



	miniW = 50
	miniH = 50	
	if(RightDownI - LeftTopI <= miniW):
		diffW = miniW- (RightDownI - LeftTopI)
		while(diffW>=0):
			if(LeftTopI-1>=0):
				LeftTopI=LeftTopI-1
				diffW=diffW-1
			if(RightDownI+1<im.size[0]):
				RightDownI=RightDownI+1
				diffW=diffW-1

	if(RightDownJ - LeftTopJ <= miniH):
		diffH = miniH- (RightDownJ - LeftTopJ)
		while(diffH>=0):
			if(LeftTopJ-1>=0):
				LeftTopJ=LeftTopJ-1
				diffH=diffH-1
			if(RightDownJ+1<im.size[1]):
				RightDownJ=RightDownJ+1
				diffH=diffH-1

	
	imOut = im.crop((LeftTopI,LeftTopJ, RightDownI,RightDownJ))

	basewidth = sizeOfW
	baseheight = sizeOfH
	#wpercent = (basewidth/float(imOut.size[0]))
	#hsize = int((float(imOut.size[1])*float(wpercent)))
	imOut = imOut.resize((basewidth,baseheight), Image.ANTIALIAS)
	imOut.save(outpath)


import glob
import os

for a in ('train','val'):
	for i in range(0,32,1):	
		print 'Now processing: '+a+' '+`i`+' class'
		os.chdir("/home/logocat/handwrite/images_original_data/images_"+a+"/"+`i`+"/")
		now_path = "/home/logocat/handwrite/images_original_data/images_"+a+"/"+`i`+"/"
		dis_path = "/home/logocat/handwrite/images_original_data/images_"+a+"_cropped/"+`i`+"/"
		if not os.path.exists(dis_path): os.makedirs(dis_path)		
		for file in glob.glob("*.jpg"):
			resize(now_path+file,dis_path+file,105,122)

for a in ('ans',):
	for i in range(100,101,1):	
		print 'Now processing: '+a+' '+`i`+' class'
		os.chdir("/home/logocat/handwrite/images_original_data/images_"+a+"/"+`i`+"/")
		now_path = "/home/logocat/handwrite/images_original_data/images_"+a+"/"+`i`+"/"
		dis_path = "/home/logocat/handwrite/images_original_data/images_"+a+"_cropped/"+`i`+"/"
		if not os.path.exists(dis_path): os.makedirs(dis_path)	
		for file in glob.glob("*.jpg"):
			resize(now_path+file,dis_path+file,105,122)

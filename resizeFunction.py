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

	RGBThreshold = 120*3;

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			rgbAdded = 0;
			for k in range(imarray[i][j].size):
				rgbAdded = rgbAdded + imarray[i][j][k]
			if(rgbAdded>=RGBThreshold):
				TopFirstI=i
				TopFirstJ=j



	for j in range(im.size[1]):
		for i in range(im.size[0]):
			rgbAdded = 0;
			for k in range(imarray[i][j].size):
				rgbAdded = rgbAdded + imarray[i][j][k]
			if(rgbAdded>=RGBThreshold):
				LeftFirstI=i
				LeftFirstJ=j



	for i in xrange(im.size[0]-1,0,-1):
		for j in xrange(im.size[1]-1,0,-1):
			rgbAdded = 0;
			for k in range(imarray[i][j].size):
				rgbAdded = rgbAdded + imarray[i][j][k]
			if(rgbAdded>=RGBThreshold):
				DownFirstI=i
				DownFirstJ=j



	for j in xrange(im.size[1]-1,0,-1):
		for i in xrange(im.size[0]-1,0,-1):
			rgbAdded = 0;
			for k in range(imarray[i][j].size):
				rgbAdded = rgbAdded + imarray[i][j][k]
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

	print 'TF i,j : (',LeftTopI,',',LeftTopJ,')'
	print 'RD i,j : (',RightDownI,',',RightDownJ,')'

	imOut = im.crop((LeftTopJ,LeftTopI, RightDownJ, RightDownI ))


	basewidth = sizeOfW
	baseheight = sizeOfH
	#wpercent = (basewidth/float(imOut.size[0]))
	#hsize = int((float(imOut.size[1])*float(wpercent)))
	imOut = imOut.resize((basewidth,baseheight), Image.ANTIALIAS)
	imOut.save(outpath)





"""
Usage: 
    python runTest.py DEPLOY_PROTOTXT TRAINED_NET IMAGE_MEAN TEST_DIR
"""
import time
import datetime
import numpy as np
import caffe
import sys
from os.path import isfile, isdir
from glob import glob


if __name__ == "__main__":
    assert len(sys.argv) == 4, "Error: Invalid input arguments."
    assert isfile(sys.argv[1]) and isfile(sys.argv[2]) and isdir(sys.argv[3]), "Error: Input files missing."
    DEPLOY_PROTOTXT = sys.argv[1]
    TRAINED_NET = sys.argv[2]

    net = caffe.Classifier(DEPLOY_PROTOTXT,TRAINED_NET)
    net.set_phase_test()
    net.set_channel_swap('data', (2,1,0))
    net.set_input_scale('data', 255)

    # TESTIMG = list()
    fans = open("result.txt", "w")
    for i in range(len(glob(sys.argv[3] + "/100/*.jpg"))):
	t = time.time()
	print(time.strftime('%Y-%m-%d %H:%M:%S   ', time.localtime(t))+`i`+'/'+str(len(glob(sys.argv[3] + "/100/*.jpg"))))
        # TESTIMG.append(glob(sys.argv[3] + "/100/" + str(i + 1) + ".jpg"))

        img_path = glob(sys.argv[3] + "/100/" + str(i + 1) + ".jpg")[0]
        fans.write(str(np.nan_to_num(net.predict([caffe.io.load_image(img_path)])[0]).argmax(axis=0)) + "\n")
        # scores = self.net.predict([caffe.io.load_image(img_path)])
    fans.close()

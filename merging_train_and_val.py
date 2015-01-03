import glob
import os

for i in range(0,32,1):	
	now_id=1
	train_file_name = "/home/logocat/handwrite/images_train/"+`i`+"/"+`now_id`+".jpg"
	while(os.path.isfile(train_file_name)):
		now_id=now_id+1
		train_file_name = "/home/logocat/handwrite/images_train/"+`i`+"/"+`now_id`+".jpg"
	
	print(train_file_name) 

	os.chdir("/home/logocat/handwrite/images_val/"+`i`+"/")
	for file in glob.glob("*.jpg"):
		if(now_id<=430):
			print(file)
			os.rename(file, train_file_name)
			now_id=now_id+1
			train_file_name = "/home/logocat/handwrite/images_train/"+`i`+"/"+`now_id`+".jpg"

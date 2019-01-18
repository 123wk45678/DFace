import os

print("************************************************")

bbox = 'list_bbox_celeba.txt'
print("bbox file : %s" %bbox)

landmark = 'list_landmarks_celeba.txt'
print("landmark file : %s" %landmark)

fr_bbox = open(bbox, 'rb')

fr_landmark = open(landmark, 'rb')

fw_unify = open('testImageList.txt', 'w')

print("************************************************")


list_bbox = []
for each_bbox in fr_bbox:
    list_bbox.append(each_bbox)
    #print each_result

list_landmark = []
for each_landmark in fr_landmark:
    list_landmark.append(each_landmark)
    #print each_label

assert(len(list_bbox) == len(list_landmark))

print("sample number = %d" %len(list_bbox))

for i in range(len(list_landmark)):
    landmarks = list_landmark[i].split(' ', 1)
    if(len(landmarks) > 1):
	temp = list_bbox[i].replace("\r\n", "")
        fw_unify.writelines((temp + " " + landmarks[1]))

fr_bbox.close()
fr_landmark.close()
fw_unify.close()

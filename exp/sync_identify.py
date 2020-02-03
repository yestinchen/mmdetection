from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os
import numpy as np
import reader
import time

CONFIG_FILE = '../configs/faster_rcnn_r50_fpn_1x.py'
CHECKPOINT_FILE = '../models/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'

OUTPUT_FOLDER="../expout/"

def identify_videoseq(folder, model, name, score_thr=0.3):
  identify_folder(folder, model, os.path.join(OUTPUT_FOLDER, name), score_thr)


def identify_folder(folder, model, ofolder, score_thr):
  for fname in reader.list_frame_images_inorder(folder):
    fpath = os.path.join(folder, fname)
    if (not os.path.isdir(ofolder)):
      os.makedirs(ofolder)
    identify_img(fpath, model, ofolder, score_thr)

def identify_img(img, model, ofolder, score_thr):
  print("processing:"+img)
  result = inference_detector(model, img)
  bboxes = np.vstack(result)
  labels = [
    np.full(bbox.shape[0], i, dtype=np.int32)
    for i, bbox in enumerate(result)
  ]
  labels = np.concatenate(labels)
  scores = bboxes[:, -1]
  inds = scores > score_thr
  bboxes = bboxes[inds, :]
  labels = labels[inds]

  outputFile = os.path.join(ofolder, os.path.basename(img))
  with open(outputFile+".txt", 'w') as the_file:
    for bbox, label in zip(bboxes, labels):
      # print(bbox)
      left_top = (bbox[0], bbox[1])
      right_bottom = (bbox[2], bbox[3])
      # print("{}, {}".format(left_top, right_bottom))
      # print(model.CLASSES[label])
      # print("prob:{:.02f}".format(bbox[-1]))
      class_id = label
      class_name = model.CLASSES[label]
      score = bbox[-1]
      the_file.write("{}; {}; [{}, {}, {}, {}]; {}\n".format(class_name, class_id, bbox[0], bbox[1], bbox[2], bbox[3], score))

  


if __name__=="__main__":
  model = init_detector(CONFIG_FILE, CHECKPOINT_FILE, device='cuda:0')
  # identify_videoseq("../testroot/t1/",model, 0.3)
  
  start = time.time()
  # identify_videoseq("../../beindexing/python/images/visualroad1",, "visualroad1" model, 0.3) #263.5951690673828s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad2/img1/",  model,"visualroad2", 0.3) #253.76282954216003s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad3/img1/",  model, "visualroad3",0.3) #250.58333253860474s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad4/img1/",  model, "visualroad4",0.3) #249.09775495529175s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MOT16-03/img1/",  model,"MOT16-03", 0.3) #225.03858494758606s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MOT16-04/img1/",  model,"MOT16-04", 0.3) #157.41504430770874s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MOT16-13/img1/",  model,"MOT16-13", 0.3) #110.76021575927734s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/sherbrooke/img1/",  model,"sherbrooke", 0.3) #571.6836140155792s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/stmarc/img1/",  model,"stmarc", 0.3) #328.5447025299072s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_20034/img1/",  model,"MVI_20034", 0.3) #123.00305151939392s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40131/img1/",  model,"MVI_40131", 0.3) #253.31823444366455s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40171/img1/",  model,"MVI_40171", 0.3) #176.5968005657196s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40172/img1/",  model,"MVI_40172", 0.3) #404.6470127105713s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40181/img1/",  model,"MVI_40181", 0.3) #261.79537773132324s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40732/img1/",  model,"MVI_40732", 0.3) #329.40419340133667s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40751/img1/",  model,"MVI_40751", 0.3) #176.08973908424377s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_40871/img1/",  model,"MVI_40871", 0.3) #267.8949992656708s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_63544/img1/",  model,"MVI_63544", 0.3) #178.1296842098236s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/MVI_63553/img1/",  model,"MVI_63553", 0.3) # 218.65589427947998s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad1xt2/img1/",  model,"visualroad1xt2", 0.3) # 137.17280411720276s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad2xt2/img1/",  model,"visualroad2xt2", 0.3) #  136.32257533073425s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad3xt2/img1/",  model,"visualroad3xt2", 0.3) # 131.2922236919403s
  # identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad4xt2/img1/",  model,"visualroad4xt2", 0.3) # 137.0745804309845s
  identify_videoseq("/media/ytchen/hdd/working/beindex/visualroad5xt2/img1/",  model,"visualroad5xt2", 0.3) # 139.09989166259766s
  end = time.time()
  print("total time: {}s".format(end - start))

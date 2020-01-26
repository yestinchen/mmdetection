from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import os
import numpy as np

CONFIG_FILE = '../configs/faster_rcnn_r50_fpn_1x.py'
CHECKPOINT_FILE = '../models/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'

OUTPUT_FOLDER="../expout/"

def identify_videoseq(folder, model, score_thr=0.3):
  identify_folder(folder, model, os.path.join(OUTPUT_FOLDER, os.path.basename(folder)), score_thr)


def identify_folder(folder, model, ofolder, score_thr):
  for fname in os.listdir(folder):
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
      bbox_int = bbox.astype(np.int32)
      left_top = (bbox_int[0], bbox_int[1])
      right_bottom = (bbox_int[2], bbox_int[3])
      # print("{}, {}".format(left_top, right_bottom))
      # print(model.CLASSES[label])
      # print("prob:{:.02f}".format(bbox[-1]))
      class_id = label
      class_name = model.CLASSES[label]
      roi = bbox_int
      score = bbox[-1]
      the_file.write("{}; {}; {}; {}\n".format(class_name, class_id, roi, score))

  


if __name__=="__main__":
  model = init_detector(CONFIG_FILE, CHECKPOINT_FILE, device='cuda:0')
  identify_videoseq("../testroot/t1/",model, 0.3)

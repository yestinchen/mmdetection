from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import numpy as np

config_file = '../configs/faster_rcnn_r50_fpn_1x.py'
# download the checkpoint from model zoo and put it in `checkpoints/`

checkpoint_file = '../models/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'
# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')
# test a single image
img = '../demo/demo.jpg'
result = inference_detector(model, img)
bboxes = np.vstack(result)
labels = [
  np.full(bbox.shape[0], i, dtype=np.int32)
  for i, bbox in enumerate(result)
]
labels = np.concatenate(labels)

score_thr = 0.3
scores = bboxes[:, -1]
inds = scores > score_thr
bboxes = bboxes[inds, :]
labels = labels[inds]

for bbox, label in zip(bboxes, labels):
  print(bbox)
  bbox_int = bbox.astype(np.int32)
  left_top = (bbox_int[0], bbox_int[1])
  right_bottom = (bbox_int[2], bbox_int[3])
  print("{}, {}".format(left_top, right_bottom))
  print(model.CLASSES[label])
  print("prob:{:.02f}".format(bbox[-1]))
show_result_pyplot(img, result, model.CLASSES)
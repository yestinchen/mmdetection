from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv

CONFIG_FILE="../configs/faster_rcnn_r50_fpn_1x.py"
CHECKPOINT_FILE="../checkpoints/faster_rcnn_r50_fpn_1x_.pth"

OUTPUT_FOLDER="../expout/"

def identify_folder(folder, model):
  pass


def identify_img(img, model):
  result = inference_detector(model, img)


if __name__=="__main__":
  model = init_detector(CONFIG_FILE, CHECKPOINT_FILE, device='cuda:0')
  identify_folder(model)

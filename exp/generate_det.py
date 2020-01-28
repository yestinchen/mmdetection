import reader
import os

def generate_det(folder, ofolder):
  if (not os.path.isdir(ofolder)):
    os.makedirs(ofolder)
  ofile = os.path.join(ofolder, 'det.txt')
  with open(ofile, 'w') as wf:
    fid = 0
    for fname in reader.list_detected_files_inorder(folder):
      fid = fid + 1
      fpath = os.path.join(folder, fname)
      with open(fpath, 'r') as rf:
        lines = rf.readlines()
        objs = [reader.DetectedResult.from_str('0; {}'.format(i)) for i in lines]
        # append frame id.
        for s in objs:
          # width, height;
          wf.write("{},-1,{},{},{},{},{},-1,-1,-1".format(fid, s.roi[0], s.roi[1], s.roi[2]-s.roi[0], s.roi[3]-s.roi[1], s.score))
          wf.write('\n')



if __name__ == "__main__":
  # generate_det("../expout/visualroad1", "/media/ytchen/hdd/working/beindex/visualroad1/det")
  # generate_det("../expout/visualroad2", "/media/ytchen/hdd/working/beindex/visualroad2/det")
  # generate_det("../expout/visualroad3", "/media/ytchen/hdd/working/beindex/visualroad3/det")
  # generate_det("../expout/visualroad4", "/media/ytchen/hdd/working/beindex/visualroad4/det")
  # generate_det("../expout/MOT16-13", "/media/ytchen/hdd/working/beindex/MOT16-13/det")
  # generate_det("../expout/MOT16-03", "/media/ytchen/hdd/working/beindex/MOT16-03/det")
  # generate_det("../expout/MOT16-04", "/media/ytchen/hdd/working/beindex/MOT16-04/det")
  generate_det("../expout/stmarc", "/media/ytchen/hdd/working/beindex/stmarc/det")
  generate_det("../expout/sherbrooke", "/media/ytchen/hdd/working/beindex/sherbrooke/det")
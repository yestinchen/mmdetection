# generate sequence.
import os
import reader
import math

def generate_seq(ifolder, sortFile, outFile, addMissingObjs):
  if not os.path.isdir(os.path.dirname(outFile)):
    os.makedirs(os.path.dirname(outFile))
  newId = 1
  with open(outFile+"-extra.txt" if addMissingObjs else outFile+".txt", 'w') as wf:
    fid = 0
    fname_list = reader.list_detected_files_inorder(ifolder)
    with open(sortFile, 'r') as sf:
      lines = sf.readlines()
      l_index = 0
      for fname in fname_list:
        fid = fid + 1
        # read all with same fid.
        bbidmap = []
        while l_index < len(lines):
          line = lines[l_index]
          arr = line.split(",")
          sort_fid = int(arr[0])
          if fid == sort_fid:
            # read new file.
            bbidmap.append((int(arr[1]), float(arr[2]), float(arr[3]), float(arr[4]), float(arr[5])))
          else:
            break
          l_index = l_index + 1
        
        with open(os.path.join(ifolder, fname)) as detectf:
          objs = [reader.DetectedResult.from_str('0; {}'.format(i)) for i in detectf.readlines()]
          # assign each
          for obj in objs:
            x1, y1, x2, y2 = obj.roi
            # find the match one.
            max_error = 100
            tmp_id = None
            for item in bbidmap:
              id, ox1, oy1, ow, oh = item
              error = math.fabs(ox1 - x1) + math.fabs(oy1 - y1) + math.fabs(ow - (x2-x1)) + math.fabs(oh - (y2-y1))
              if error < max_error:
                tmp_id = id
                max_error = error
            if (max_error < 10):
              obj.id = tmp_id
          # ids = []
          # for obj in objs:
          #   if obj.id != -1 and not obj.id in ids:
          #     # ids.append(obj.id)
          #     # wf.write('{}\n'.format(obj))
          #   elif addMissingObjs:
          #     print("missing obj, assign a new id")
          #     obj.id="2000{0}".format(newId)
          #     newId = newId + 1
          #     wf.write('{}\n'.format(obj))
          seqset = {}
          count = 0
          for s in objs:
            clist = seqset.get(s.class_name)
            if clist == None:
              seqset[s.class_name]=[]
            clist = seqset[s.class_name]
            if s.id == 0 and addMissingObjs:
              s.id = '2000{0}'.format(newId)
            # append current one.
            if (s.id != 0):
              count = count + 1
              clist.append('{}{}'.format(s.class_name, s.id))
          # output.
          items = []
          for clazz in sorted(seqset.keys()):
            items.append('{}: <{}>'.format(clazz, ','.join(seqset[clazz])))
          if count != 0:
            wf.write(";".join(items))
          wf.write('\n')
  
def generate_seq_all(p1, p2, p3):
  generate_seq(p1, p2, p3, True)
  generate_seq(p1, p2, p3, False)

if __name__ == "__main__":
    # generate_seq('../expout/visualroad1', '../../deep_sort/results/visualroad1.txt', 
      # '../seqout/visualroad1', True)
    # generate_seq_all('../expout/visualroad2', '../../deep_sort/results/visualroad2.txt', 
    # '../seqout/visualroad2')
    # generate_seq_all('../expout/visualroad3', '../../deep_sort/results/visualroad3.txt', 
    # '../seqout/visualroad3')
    # generate_seq_all('../expout/visualroad4', '../../deep_sort/results/visualroad4.txt', 
    # '../seqout/visualroad4')
    # generate_seq_all('../expout/MOT16-03', '../../deep_sort/results/MOT16-03.txt', 
    # '../seqout/MOT16-03')
    # generate_seq_all('../expout/MOT16-04', '../../deep_sort/results/MOT16-04.txt', 
    # '../seqout/MOT16-04')
    # generate_seq_all('../expout/MOT16-13', '../../deep_sort/results/MOT16-13.txt', 
    # '../seqout/MOT16-13')
    # generate_seq_all('../expout/stmarc', '../../deep_sort/results/stmarc.txt', 
    # '../seqout/stmarc')
    # generate_seq_all('../expout/sherbrooke', '../../deep_sort/results/sherbrooke.txt', 
    # '../seqout/sherbrooke')
    generate_seq_all('../expout/MVI_20034', '../../deep_sort/results/MVI_20034.txt', 
    '../seqout/MVI_20034')
    generate_seq_all('../expout/MVI_40131', '../../deep_sort/results/MVI_40131.txt', 
    '../seqout/MVI_40131')
    generate_seq_all('../expout/MVI_40171', '../../deep_sort/results/MVI_40171.txt', 
    '../seqout/MVI_40171')
    generate_seq_all('../expout/MVI_40172', '../../deep_sort/results/MVI_40172.txt', 
    '../seqout/MVI_40172')
    generate_seq_all('../expout/MVI_40181', '../../deep_sort/results/MVI_40181.txt', 
    '../seqout/MVI_40181')
    generate_seq_all('../expout/MVI_40732', '../../deep_sort/results/MVI_40732.txt', 
    '../seqout/MVI_40732')
    generate_seq_all('../expout/MVI_40751', '../../deep_sort/results/MVI_40751.txt', 
    '../seqout/MVI_40751')
    generate_seq_all('../expout/MVI_40871', '../../deep_sort/results/MVI_40871.txt', 
    '../seqout/MVI_40871')
    generate_seq_all('../expout/MVI_63544', '../../deep_sort/results/MVI_63544.txt', 
    '../seqout/MVI_63544')
    generate_seq_all('../expout/MVI_63553', '../../deep_sort/results/MVI_63553.txt', 
    '../seqout/MVI_63553')
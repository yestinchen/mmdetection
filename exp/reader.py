# contain utils to read files.
import os

def read_detected(rfile):
    r = {'class_ids':[], 'rois': [], 'scores': [], 'class_names': []}
    with open(rfile, 'r') as f:
        for l in f.readlines():
            arr = l.split(';')
            r['class_names'].append(arr[0].strip())
            r['class_ids'].append(int(arr[1]))
            roisArr = arr[2].strip()[1:-1].split()
            r['rois'].append([int(i) for i in roisArr])
            r['scores'].append(float(arr[3]))
    return r

class DetectedResult(object):
    id=-1
    roi=None
    class_id=-1
    score=0.0
    class_name=None

    @staticmethod
    def from_str(line):
        r = DetectedResult()
        arr = line.split(';')
        r.id = int(arr[0].strip())
        r.class_name = arr[1]
        r.class_id = int(arr[2])
        roisArr = arr[3].strip()[1:-1].split(', ')
        r.roi = [float(i) for i in roisArr]
        r.score = float(arr[4])
        return r

    def __str__(self):
        return "{}; {}; {}; {}; {}".format(self.id, self.class_name, self.class_id, self.roi, self.score)

def read_detected_as_obj(rfile):
    r = read_detected(rfile)
    objs = []
    for i in range(0, len(r['class_ids'])):
        obj = DetectedResult()
        obj.roi=r['rois'][i]
        obj.class_id=r['class_ids'][i]
        obj.score=r['scores'][i]
        obj.class_name=r['class_names'][i]
        objs.append(obj)
    return objs

def list_frame_images_inorder(imgDir):
    file_names = next(os.walk(imgDir))[2]

    def extract_number(string):
        if ('frame' in string):
            return int(string[len('frame'): -4])
        elif ('img' in string): 
            return int(string[len('img'):-4])
        else:
            return int(string[: -4])


    sortedFiles = sorted(file_names ,key=lambda x: extract_number(x))
    return sortedFiles

    
def list_detected_files_inorder(imgDir):
    file_names = next(os.walk(imgDir))[2]

    def extract_number(string):
        if ('frame' in string):
            return int(string[len('frame'): -8])
        elif ('img' in string): 
            return int(string[len('img'):-8])
        else:
            return int(string[: -8])

    sortedFiles = sorted(file_names ,key=lambda x: extract_number(x))
    return sortedFiles

if __name__ == "__main__":
    # r = read_detected('detected/demo/frame0.jpg.txt')
    # print(r)
    # for f in list_frame_images_inorder('images/demo'):
    #     print(f)
    # r = read_detected_as_obj('detected/visualroad1/frame0.jpg.txt')
    # for i in r:
    #     print(i)
    for f in list_detected_files_inorder('detected/stmarc_frames'):
        print(f)
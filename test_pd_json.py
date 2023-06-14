import json
import os


with open(os.path.join('openpose_json/10th_frame_keypoints.json')) as mon_json:
    print(os.path.join('openpose_json/10th_frame_keypoints.json'))
    data = json.load(mon_json)
    print(data['people'])
    for r in mon_json:
        print(r[0])
        data = json.load(r)
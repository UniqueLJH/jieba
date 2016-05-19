import jieba
from jieba import Tokenizer
import ujson as json
LT = Tokenizer()
LT.load_userdict("/usr/local/lib/python2.7/dist-packages/jieba/location_dict.txt")
location_synonmys_dictynonmys_dict = None
with open("/usr/local/lib/python2.7/dist-packages/jieba/location_synonmys.txt", "rb") as f:
    line = f.readline()
    location_synonmys_dict = json.loads(line)
def get_location(location):
    l = []
    if location:
        l = list(LT.cut(location))
    locationlist = []
    for ll in l:
        if ll in location_synonmys_dict:
            if location_synonmys_dict[ll] not in locationlist:
                locationlist.append(location_synonmys_dict[ll])
    return "|".join(locationlist)
    


import json
import random
import re

if __name__ == '__main__':

    with open("../data/急性腹膜炎.txt", "r", encoding="utf-8") as f:
        read = f.read()
    p = re.findall(r'[a-z]\'[a-z]', read)
    sp = set(p)
    print(sp)
    sp_dict = {}
    for i in sp:
        random_random = random.random()
        print(random_random)
        sp_dict[str(random_random)] = i
        read = read.replace(i, str(random_random))
    read = read.replace("\"", "*78545*")
    read = read.replace("'", "\"")
    read = read.replace("*78545*", "'")
    read = read.replace(": '", ": \"")
    read = read.replace("'}", "\"}")

    for k, v in sp_dict.items():
        read = read.replace(k, v)
    split = read.split("][")
    res = []
    if (len(split) > 1):
        for i, data in enumerate(split):
            if i / 2 == 0:
                res.append(json.loads(data + "]"))
            else:
                res.append(json.loads("[" + data))
    else:
        res.append(json.loads(split[0]))
    print(res)

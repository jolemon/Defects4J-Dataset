import os
import shutil
import re

projs = ['Time', 'Mockito', 'Lang', 'Math', 'Closure']
linked_dir = 'linked-bugMethods-iBug/'
linked_postfix = '_bugId_buggyMethodsName'
bugcode_dir = 'allMethods-iBug'
br_dir = 'bugReport4Vector'

def load_link_dic(path):
    dic = {}
    f = open(path, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            parts = line.split('\t')
            br_id = parts[0]
            dic[br_id] = 1
    return dic


def clear_allMethods():
    for proj in projs:
        link_dic = load_link_dic(linked_dir + proj + linked_postfix)
        for file in os.listdir(os.path.join(bugcode_dir, proj)):
            if file not in link_dic:
                print(os.path.join(bugcode_dir, proj, file))
                file_path = os.path.join(bugcode_dir, proj, file)
                if file == '.DS_Store':
                    os.remove(file_path)
                else:
                    shutil.rmtree(file_path)


def clear_br():
    for proj in projs:
        link_dic = load_link_dic(linked_dir + proj + linked_postfix)
        proj_dir = os.path.join(br_dir, proj)
        for br in os.listdir(proj_dir):
            if br not in link_dic:
                print(os.path.join(proj_dir, br))
                file_path = os.path.join(br_dir, proj, br)
                os.remove(file_path)


if __name__ == '__main__':
    clear_allMethods()
    clear_br()
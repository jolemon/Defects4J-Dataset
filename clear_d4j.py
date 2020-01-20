import os
import shutil
import re

projs = ['Time', 'Mockito', 'Lang', 'Math', 'Closure']
linked_dir = 'linked-bugMethods/'
linked_postfix = '_bugId_buggyMethodsName'
bugcode_dir = 'allMethods'
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
            pm_lists_str = parts[1].rstrip('\n')
            pm_lists = pm_lists_str.split('外')
            for pm_list in pm_lists:
                pm_parts = pm_list.split('内')
                if len(pm_parts) < 2:
                    print(pm_parts, "in this sentence can not find PATH / METHOD_NAME !")
                    continue
                path =  '/'+'/'.join((pm_parts[0].split('/'))[2:])
                method = pm_parts[1]

                path_method = path + '#' + trim_method(trim_comma_in_paras(method))

                if br_id not in dic:
                    dic.setdefault(br_id, []).append(path_method)
                else:
                    dic[br_id].append(path_method)
    return dic


def trim_method(ori_method_str):
    return re.sub(r'(@(\w+) )|(public )|(private )|(final )|(static )|(abstract )|(protected )|(synchronized )|(native )|(transient)|(volatie )|( throws(.*))', "", ori_method_str)


def trim_comma_in_paras(method_str):
    return re.sub(r'(,(\s*))', ',', method_str)


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
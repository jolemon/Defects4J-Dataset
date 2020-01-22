import os


def remove_class(from_file_path, to_file_path):
    with open(from_file_path, 'r') as f:
        lines = f.readlines()

    with open(to_file_path, 'w') as f:
        new_lines = []
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            parts = line.split('\t')
            if len(parts) == 1:
                print('length of parts == 1')
                continue

            if '外' not in parts[1]:
                method = parts[1]
                res_method = handle_method(method)
                new_line = parts[0] + '\t' + res_method
                new_lines.append(new_line)
            else:
                methods = parts[1].split('外')
                new_methods = []
                for method in methods:
                    res_method = handle_method(method)
                    new_methods.append(res_method)
                new_line = parts[0] + '\t' + '外'.join(new_methods)
                new_lines.append(new_line)
            # print(new_line)
        # print(new_lines)
        f.write('\n'.join(new_lines))


def handle_method(method):
    parts = method.split('内')
    path = parts[0]
    method = parts[1].split('#')[1]
    return path+'内'+method


def from_FineLoctor_to_iBug(proj):
    return


defects4j_dataset_path = '/Users/lienming/defects4j-dataset'

linked_buggy_dir_name_for_FineLocator = 'linked-bugMethods'

linked_buggy_dir_name_for_iBug = 'linked-bugMethods-iBug'
linked_buggy_dir_path_for_iBug = os.path.join(defects4j_dataset_path, linked_buggy_dir_name_for_iBug)

postfix = '_bugId_buggyMethodsName'
if not os.path.exists(linked_buggy_dir_path_for_iBug):
    os.mkdir(linked_buggy_dir_path_for_iBug)

for proj in ['Time', 'Mockito', 'Lang', 'Math', 'Closure']:
    linked_buggy_file_for_FineLocator = \
        defects4j_dataset_path + '/' + linked_buggy_dir_name_for_FineLocator + '/' + proj + postfix

    linked_buggy_file_for_iBug = \
        defects4j_dataset_path + '/' + linked_buggy_dir_name_for_iBug + '/' + proj + postfix

    # print(linked_buggy_file_for_FineLocator)
    # print(linked_buggy_file_for_iBug)

    remove_class(linked_buggy_file_for_FineLocator, linked_buggy_file_for_iBug)

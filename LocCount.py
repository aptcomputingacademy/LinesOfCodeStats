'''
count no of lines in .c files found in a directory.
methods:
is_c_file
count_c_code
'''
import os
import re
import time
Log_fd = 0
ROOT_DIR = "/Users/kamalmukiri/Documents/AptComputingAcademy"
remove_dirs = ["/Users/kamalmukiri/Documents/AptComputingAcademy/IoT/Projects/SmartFarming/FinalProject/SmartFarm_v6 copy.1/SmartFarm9_old/SmartFarm9/Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS"]
list_code_formats = [".c", ".py", ".cpp", ".h", ".hpp"]



def is_c_file(file_name):
    '''
    checks if a file is .c file.
    '''
    for file_format in list_code_formats:
        pattern = "\\"+file_format+"$"
        if re.search(pattern,file_name):
#             print("File format: ", file_name)
            return True
    return False


def count_c_code(root_dir):
    '''
    method to count no of lines in .c files found in a directory.
    '''

    if ".git" in root_dir:
        return


    for dir_name, sub_dir_list, file_list in os.walk(root_dir):
        #print('Found directory: %s' % dir_name)
        #print(sub_dir_list)
        #print(file_list)
        #print("\n\n")
        
        #Go through sub dirs...
        if len(sub_dir_list) > 0:
            for sub_dir in sub_dir_list:
                count_c_code(sub_dir)
        
        list_c_files = list(filter(is_c_file, file_list))
        for item in list_c_files:
            if dir_name in remove_dirs:
                return
            path = os.path.join(dir_name, item)
            #print(path)
            try:
                lines_in_file = 0
                with open(path, 'r') as file_name:
                    for line in file_name:
                        line = line.strip()
                        if line == '':
                            continue
                        lines_in_file += 1

            except:
                print("Exception File name = ", path)
            global num_lines
            Log_fd.write(path+":"+str(lines_in_file)+"\n")
            num_lines += lines_in_file
    return
try:
    os.rename("LogPresent.txt", "LogPrev.txt")
except:
    pass
num_lines = 0
with open("LogPresent.txt", 'w') as log_fd:
    Log_fd = log_fd
    start = time.time()
    count_c_code(ROOT_DIR)
    end = time.time()
    print("No of lines of c = {} \nCalculated in {}secs".format(num_lines, end-start))
    
log_present_fd = open("LogPresent.txt", 'r')
log_present_lines = set(log_present_fd.readlines())
log_present_fd.close()
log_prev_fd = open("LogPrev.txt", 'r')
log_prev_lines = set(log_prev_fd.readlines())
log_prev_fd.close()
    
print("Diff = ", log_present_lines - log_prev_lines)

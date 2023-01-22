'''
1. Get information:
    a) Class
    b) HW #
    c) Due Date
    d) number of questions
    e) number of parts per question
2. Generate folder if it does not exist
3. Generate default mathematica with new info
'''
import os
import shutil

path_to_default = r'D:\Documents\UW-Madison\CourseWork\Spring\DefualtMathematica'
path_to_classes = r'D:\Documents\UW-Madison\CourseWork\Spring'
abcs = [0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Prompting for information input
class_title = input("Class: ")
hw_num = input("Hw#: ")
due_date = input("Due date: ")
# num_ques = int(input("Number of questions: "))
# q_parts = {}
# for q in range(1,num_ques+1):
#     q_parts[q] = int(input(f"Parts for question {q}: "))
print("\n")

def zeroFormat(x):
    if int(x)/10 < 1:
        return(''.join(['0','0',x]))
    else:
        return(''.join(['0',x]))

# Finding or creating the directory
os.chdir(path_to_classes)
for dir in os.listdir():
    if class_title.upper() in ['QC',"ADVANCED","QUANTUM","COMPUTING","ADVANCEDQUANTUMCOMPUTING"] and dir == 'AdvancedQuantumComputing':
        dirname = 'AdvancedQuantumComputing'
        dirprefix = 'AQC'
        class_title = 'Advanced Quantum Computing'
        os.chdir(f'{path_to_classes}\\{dir}\\Hw')
        if os.path.isdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}'):
            if os.path.isfile(f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb'):
                print(f'Error: AQC_HW{zeroFormat(hw_num)}.nb already exists')
            else:
                shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb')
                copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb'
        else:
            os.mkdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}')
            shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb')
            copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb'
    elif class_title.upper() in ['ELECTRONICS',"EAM","MEASUREMENT","ELECTRONICAIDSTOMEASUREMENT"] and dir == 'ElectronicAidsToMeasurement':
        dirname = 'ElectronicAidsToMeasurement'
        dirprefix = 'EAM'
        class_title = 'Electronic Aids To Measurement'
        os.chdir(f'{path_to_classes}\\{dir}\\Hw')
        if os.path.isdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}'):
            if os.path.isfile(f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\EAM_HW{zeroFormat(hw_num)}.nb'):
                print(f'Error: EAM_HW{zeroFormat(hw_num)}.nb already exists')
            else:
                shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\EAM_HW{zeroFormat(hw_num)}.nb')
                copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\EAM_HW{zeroFormat(hw_num)}.nb'
        else:
            os.mkdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}')
            shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\EAM_HW{zeroFormat(hw_num)}.nb')
            copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\EAM_HW{zeroFormat(hw_num)}.nb'
    elif class_title.upper() in ['ML',"CS","MACHINE","LEARNING","MACHINELEARNING"] and dir == 'MachineLearning':
        dirname = 'MachineLearning'
        dirprefix = 'ML'
        class_title = 'Machine Learning'
        os.chdir(f'{path_to_classes}\\{dir}\\Hw')
        if os.path.isdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}'):
            if os.path.isfile(f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\ML_HW{zeroFormat(hw_num)}.nb'):
                print(f'Error: ML_HW{zeroFormat(hw_num)}.nb already exists')
            else:
                shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\ML_HW{zeroFormat(hw_num)}.nb')
                copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\ML_HW{zeroFormat(hw_num)}.nb'
        else:
            os.mkdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}')
            shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\ML_HW{zeroFormat(hw_num)}.nb')
            copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\ML_HW{zeroFormat(hw_num)}.nb'
    elif class_title.upper() in ['RESEARCH',"R"] and dir == 'Research':
        dirname = 'Research'
        dirprefix = 'R'
        class_title = 'Research'
        os.chdir(f'{path_to_classes}\\{dir}\\Hw')
        if os.path.isdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}'):
            if os.path.isfile(f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\R_HW{zeroFormat(hw_num)}.nb'):
                print(f'Error: R_HW{zeroFormat(hw_num)}.nb already exists')
            else:
                shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\R_HW{zeroFormat(hw_num)}.nb')
                copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\R_HW{zeroFormat(hw_num)}.nb'
        else:
            os.mkdir(f'{os.getcwd()}\\{zeroFormat(hw_num)}')
            shutil.copyfile(f'{path_to_default}\\DefaultNotebook.nb',f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\R_HW{zeroFormat(hw_num)}.nb')
            copy_path = f'{path_to_classes}\\{dir}\\Hw\\{zeroFormat(hw_num)}\\R_HW{zeroFormat(hw_num)}.nb'


# Getting Default Mathematica Notebook
# os.chdir(path_to_default)
#f'{path_to_classes}\\AdvancedQuantumComputing\\Hw\\{zeroFormat(hw_num)}\\AQC_HW{zeroFormat(hw_num)}.nb'
nbTest = open(f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb')
nbPath = f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb'
lines=[]

with open (f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb', 'r') as nb_reader:
    for line in nb_reader:
        if 'Class HW#' in line:
            lines.append(line.replace("Class HW#", f'{class_title} HW{zeroFormat(hw_num)}'))
        elif '00/00/0000' in line:
            lines.append(line.replace("00/00/0000", due_date))
        else:
            lines.append(line)

with open(f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb', 'w') as nb_writer:
    for line in lines:
        nb_writer.write(line)
  

#print(nbTest.read(1000))

def getQs(path):
    with open(path, 'r') as q_reader:
        q = []
        lines=q_reader.readlines()
        for index in range(len(lines)):
            if r'Cell["Question 001"' in lines[index]:
                start = index-2
                break
        for index2 in range(start, len(lines)):
            if r'}, Open' in lines[index2]:
                stop = index2+1
                break
        for count in range(start,stop+1):
            q.append(lines[count])
        new_list = []
        # for c in range(len(lines)):
        #     if c >= start and c <= stop:
        #         continue
        #     else:
        #         new_list.append(lines[c])
        # return(''.join(sub))
    # with open(path, 'w') as q_writer:
    #     for line in q:
    #         q_writer.write(line)
    return(q)

qFormat = getQs(nbPath)
print(''.join(qFormat))

def insertQ(path, q):
    with open(path, 'r') as q_reader:
        lines=q_reader.readlines()
        for index in range(len(lines)):
            if r'}, Open  ]]' in lines[index]:
                insert_point = index+2
                break
        new_list = lines[0:insert_point] + ['\n'] + q + lines[insert_point:]
        #print(''.join(new_list))
    with open(path, 'w') as q_writer:
        for line in new_list:
            q_writer.write(line)


insertQ(nbPath, qFormat)

# def getSub(path):
#     with open(path, 'r') as sub_reader:
#         sub = []
#         lines=sub_reader.readlines()
#         for index in range(len(lines)):
#             if r'Cell["A:"' in lines[index]:
#                 start = index-2
#                 break
#         for index2 in range(start+1, len(lines)):
#             if r'Cell[CellGroupData[{' in lines[index2]:
#                 stop = index2-2
#                 break
#         for count in range(start,stop+1):
#             sub.append(lines[count])
#         new_list = []
#         for c in range(len(lines)):
#             if c >= start and c <= stop:
#                 continue
#             else:
#                 new_list.append(lines[c])
#         # return(''.join(sub))
#     with open(path, 'w') as sub_writer:
#         for line in new_list:
#             sub_writer.write(line)
#     return(sub)

# subSec = getSub(nbPath)

# def adjust_let(sub, let):
#     new_lis=[]
#     for x in sub:
#         if f'"A:"' in x:
#             new_lis.append(x.replace(f'"A:"', f'"{let}:"'))
#         else:
#             new_lis.append(x)
#     return(new_lis)

# def insertSub(path, sub, let):
#     with open(path, 'r') as sub_reader:
#         lines=sub_reader.readlines()
#         for index in range(len(lines)):
#             if r'"\"\<Global`*\>\""' in lines[index]:
#                 insert_point = index+3
#                 break
#         new_list = lines[0:insert_point] + ['\n'] + adjust_let(sub, let) + lines[insert_point:]
#     with open(path, 'w') as sub_writer:
#         for line in new_list:
#             sub_writer.write(line)

# def nums_to_let(nums):
#     let_lis=[]
#     for num in range(1,nums+1):
#         let_lis.append(abcs[num])
#     return(', '.join(let_lis))

# for key, value in q_parts.items():
#     for let in nums_to_let(value):
#         insertSub(nbPath, subSec, let)

# for key, value in q_parts.items():
#     print(key, ' : ', nums_to_let(value))
# print(q_parts)
# print(def_nb.read())
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
num_ques = int(input("Number of questions: "))
q_parts = {}
for q in range(1,num_ques+1):
    q_parts[q] = int(input(f"Parts for question {q}: "))
print("\n")

def zeroFormat(x):
    if int(x)/10 < 1:
        return(''.join(['0','0',str(x)]))
    elif int(x)/10 < 10:
        return(''.join(['0',str(x)]))
    else:
        return(str(x))

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
nbTest = open(f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb')
nbPath = f'{path_to_classes}\\{dirname}\\Hw\\{zeroFormat(hw_num)}\\{dirprefix}_HW{zeroFormat(hw_num)}.nb'

# Path Information
headerPath = r'D:\Desktop\Programming\Python\MathematicaCreator\Essentials\HeaderInfo.txt'
tailPath = r'D:\Desktop\Programming\Python\MathematicaCreator\Essentials\TailInfo.txt'
ques1nosubs = r'D:\Desktop\Programming\Python\MathematicaCreator\noSubs\Question1NoSubs.txt'
#oneQuestionPath = r'D:\Desktop\Programming\Python\MathematicaCreator\SingleQ.txt'
#ques1 = r'D:\Desktop\Programming\Python\MathematicaCreator\Question1.txt'
#midQues = r'D:\Desktop\Programming\Python\MathematicaCreator\MiddleQuestions.txt'
#finalQ = r'D:\Desktop\Programming\Python\MathematicaCreator\FinalQuestion.txt'
finalQnoSubs = r'D:\Desktop\Programming\Python\MathematicaCreator\noSubs\FinalQNoSubs.txt'
subSec = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subSection.txt'
middleQnoSubs = r'D:\Desktop\Programming\Python\MathematicaCreator\noSubs\middleQnoSubs.txt'
DestinationPath = r'D:\Desktop\Programming\Python\MathematicaCreator\Output2.nb'

subBeginPath = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subBegin.txt'
subPath = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subSection.txt'
subPathMQ = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subSectionMQ.txt'
subFinalPath = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subFinal.txt'
subFqPath = r'D:\Desktop\Programming\Python\MathematicaCreator\subSections\subFQlast.txt'

def q1subs(num):
    with open(subBeginPath, 'r') as sb_read:
        sb = sb_read.readlines()
    with open(subPathMQ, 'r') as spmq_read:
        spmq = spmq_read.readlines()
    with open(subPath, 'r') as sp_read:
        sp = sp_read.readlines()
    with open(subFinalPath, 'r') as sf_read:
        sf = sf_read.readlines()
    full = sb+['\n']
    for c in range(num):
        full+=spmq+['\n']
    return(full+sf)
def mQsubs(num):
    with open(subBeginPath, 'r') as sb_read:
        sb = sb_read.readlines()
    with open(subPath, 'r') as sp_read:
        sp = sp_read.readlines()
    with open(subPathMQ, 'r') as spmq_read:
        spmq = spmq_read.readlines()
    with open(subFinalPath, 'r') as sf_read:
        sf = sf_read.readlines()
    full = sb+['\n']
    for c in range(num-1):
        full+=spmq+['\n']
    return(full+sp+sf)
def fQsubs(num):
    with open(subBeginPath, 'r') as sb_read:
        sb = sb_read.readlines()
    with open(subPath, 'r') as sp_read:
        sp = sp_read.readlines()
    with open(subPathMQ, 'r') as spmq_read:
        spmq = spmq_read.readlines()
    with open(subFinalPath, 'r') as sf_read:
        sf = sf_read.readlines()
    with open(subFqPath, 'r') as fQsubs_read:
        fq = fQsubs_read.readlines()
    full = sb+['\n']
    for c in range(num-1):
        full+=spmq+['\n']
    return(full+sp+fq)

with open(headerPath, 'r') as header_read:
    head = header_read.readlines()
#with open(oneQuestionPath, 'r') as ques_read:
    #ques = ques_read.readlines()
with open(ques1nosubs, 'r') as q1no_read:
    q1no = q1no_read.readlines()
#with open(ques1, 'r') as q1_read:
    #q1 = q1_read.readlines()
#with open(midQues, 'r') as mQ_read:
    #mQ = mQ_read.readlines()
#with open(finalQ, 'r') as fQ_read:
    #fQ = fQ_read.readlines()
with open(subSec, 'r') as subS_read:
    subS = subS_read.readlines()
with open(finalQnoSubs) as fQS_read:
    fQS = fQS_read.readlines()
with open(tailPath, 'r') as tail_read:
    t = tail_read.readlines()
with open(middleQnoSubs, 'r') as mQno_read:
    mQno = mQno_read.readlines()

def editQnum(ques, num):
    lines=[]
    for line in ques:
        if f'Question' in line:
            if f'Question 001' in line:
                lines.append(line.replace("Question 001", f'Question {zeroFormat(num)}'))
            elif f'Question 002' in line:
                lines.append(line.replace("Question 002", f'Question {zeroFormat(num)}'))
        else:
            lines.append(line)
    return(lines)

def to_upper(let_lis):
    new_list =[]
    for let in let_lis:
        new_list.append(let.upper())
    return(new_list)

def nums_to_let(num):
    let_lis=[]
    for num in range(1,num+1):
        let_lis.append(abcs[num])
    return(to_upper(let_lis))

def adjust_let(sub, let_lis):
    new_lis=[]
    c=0
    for x in sub:
        if f'"A:"' in x:
            new_lis.append(x.replace(f'"A:"', f'"{let_lis[c]}:"'))
            c+=1
        else:
            new_lis.append(x)
    return(new_lis)

full_nb=head
for n in range(1,num_ques+1):
    if n == 1:
        if q_parts.get(n) == 1:
            full_nb+=editQnum(q1no, n)
        else:
            full_nb+=adjust_let(editQnum(q1subs(q_parts.get(n)), n), nums_to_let(q_parts.get(n)))
    elif n == num_ques:
        if q_parts.get(n) == 1:
            full_nb+=editQnum(fQS, n)
        else:
            full_nb+=adjust_let(editQnum(fQsubs(q_parts.get(n)), n), nums_to_let(q_parts.get(n)))
    else:
        if q_parts.get(n) == 1:
            full_nb+=editQnum(mQno, n)
        else:
            full_nb+=adjust_let(editQnum(mQsubs(q_parts.get(n)), n), nums_to_let(q_parts.get(n)))
full_nb+=t
with open(nbPath, 'w') as nb_writer:
    for nb in full_nb:
        nb_writer.write(nb)


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

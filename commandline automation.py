# os to handle file paths
# os.path.dirname(path) gets parent of a path
# os.path.join(path, *args)  joins path with arg[1] and so on
import os
# sys and subprocess to handle automating commandline
import subprocess


# cd varible is used everytime the player do stuff. server will cout all the files in cd_varible's directory
cd_variable = os.path.dirname(__file__)
# file paths for .exe
hdl_HardwareSimulatordotbat = "hardwaresimulator.bat"
hdl_path = os.path.join(cd_variable, hdl_HardwareSimulatordotbat)
asm_CPUemulatordotbat = 'cpuemulator.bat'
asm_path = os.path.join(cd_variable, asm_CPUemulatordotbat)
masm_macroassemblydotpy = 'open main.py and type your name right here'
macros_path = os.path.join(cd_variable, masm_macroassemblydotpy)




#prints a command
def printcommand(str_ing):
    global cd_variable
    print("PS ", cd_variable, "> ",str_ing,sep='')
    out = subprocess.Popen(['powershell', '-command', str_ing], stderr=subprocess.STDOUT)
    try:
        print(out.communicate(timeout=5.0))
    except subprocess.TimeoutExpired:
        out.kill()
        print(out.communicate())

#create gui
#const
help_command = 'cd to go somewhere.\n\
                hdl to specify path of hardware emulator\n\
                asm to specify path of cpuemulator\n\
               masm to specify path of macroassembler \n\
                auto to declare that the bats are here\n\
               here to test all the files in here except for hack files\n\
               hack to test all the hack files \n\
               macro to assemble all the masm \n\
               ctrl+c to exit'
#array of array pointers to sort data into 2d array
your_files = [[],[],[],[]]
your_files_hdl_int=0
your_files_asm_int=1
your_files_masm_int=2
your_files_hack_int=3
your_files_tst_int=4
# put files where they need to go
def initailize_your_files():
    global your_files
    global your_files_hack_int
    global your_files_asm_int
    global your_files_masm_int
    global your_files_hdl_int
    global cd_variable
    your_files = [[], [], [], [], []]
    for potentialfile in os.listdir(cd_variable):
        file_ext = potentialfile.split('.')[-1]
        if (file_ext=='hack'):
            your_files[your_files_hack_int].append(os.path.join(cd_variable,potentialfile))

        elif (file_ext=='masm'):
            your_files[your_files_masm_int].append(os.path.join(cd_variable, potentialfile))

        elif (file_ext=='asm'):
            your_files[your_files_asm_int].append(os.path.join(cd_variable, potentialfile))

        elif (file_ext=='hdl'):
            your_files[your_files_hdl_int].append(os.path.join(cd_variable, potentialfile))
        elif (file_ext=="tst"):
            your_files[your_files_tst_int].append(os.path.join(cd_variable, potentialfile))

        else:
            pass

# use paths in powershell
def cd_variable_call():
    global cd_variable
    return ''.join(["'",cd_variable,"'"])
def asm_path_call():
    global asm_path
    return ''.join(["'",asm_path,"'"])
def hdl_path_call():
    global hdl_path
    return ''.join(["'",hdl_path,"'"])
def macros_path_call():
    global macros_path
    return ''.join(["'",macros_path,"'"])


# prints main menue
def print_main_menue():
    global cd_variable
    global hdl_path
    global macros_path
    global asm_path
    printcommand(' '.join(['ls',cd_variable_call()]))
    print('\t asm file tester is',asm_path,'\t\
            hdl file tester is',hdl_path,'\t\
            macroassembler tester is',macros_path,'\t\
            ')


while True:
    print_main_menue()
    userinpt=input("type help").strip()
    user_cmd=userinpt.split(' ')[0]
    if (user_cmd=='cd'):
        user_path=userinpt.split(' ')[1].strip()
        #compute family tree of path
        if(user_path[0]=='.'):
            #it is relative path
            user_path = user_path[1:]
            while (user_path[0] == '.'):
                cd_variable =os.path.dirname(cd_variable)

                # pop the dot
                user_path = user_path[1:]
            cd_variable=os.path.join(cd_variable,user_path)
        else:
            #it is absolute path
            cd_variable=user_path


    elif (user_cmd=='here'):
        initailize_your_files()

        #print results from asm
        for x in your_files[your_files_asm_int]:
            findme=os.path.basename(x.split(".")[0])
            for y in your_files[your_files_tst_int]:
                if findme.lower() in os.path.basename(y).lower():
                    printcommand(' '.join([asm_path,y]))

        # print results from hdl
        for x in your_files[your_files_hdl_int]:
            findme=os.path.basename(x.split(".")[0])
            for y in your_files[your_files_tst_int]:
                if findme.lower() in os.path.basename(y).lower():
                    printcommand(' '.join([hdl_path, y]))

    elif (user_cmd=='hack'):
        initailize_your_files()

        # print results from hack
        for x in your_files[your_files_hack_int]:
            findme=os.path.basename(x.split(".")[0])
            for y in your_files[your_files_tst_int]:
                if findme.lower() in os.path.basename(y).lower():
                    printcommand(' '.join([asm_path, y]))


    elif (user_cmd=="macro"):
        initailize_your_files()

        # print results from macroassembly
        for x in your_files[your_files_masm_int]:
            findme=os.path.basename(x.split(".")[0])
            for y in your_files[your_files_tst_int]:
                if findme.lower() in os.path.basename(y).lower():
                    printcommand(' '.join([macros_path, y]))


    elif (user_cmd=='auto'):
        hdl_path = os.path.join(cd_variable, hdl_HardwareSimulatordotbat)
        asm_path = os.path.join(cd_variable, asm_CPUemulatordotbat)
    elif (user_cmd=='asm'):
        if len(userinpt.split(' ')) == 1:
            # it is put over here
            asm_path = os.path.join(cd_variable, asm_CPUemulatordotbat)
            continue


        cd_variable_temp=cd_variable
        user_path = userinpt.split(' ')[1].strip()
        # compute family tree of path
        if (user_path[0] == '.'):
            # it is relative path
            user_path = user_path[1:]
            while (user_path[0] == '.'):
                cd_variable_temp = os.path.dirname(cd_variable_temp)

                # pop the dot
                user_path = user_path[1:]
            asm_path = os.path.join(cd_variable_temp, user_path)
        else:
            # it is absolute path
            asm_path = user_path

    elif (user_cmd=='hdl'):
        if len(userinpt.split(' ')) == 1:
            # it is put over here
            hdl_path = os.path.join(cd_variable, hdl_HardwareSimulatordotbat)
            continue

        cd_variable_temp = cd_variable
        user_path = userinpt.split(' ')[1].strip()
        # compute family tree of path
        if (user_path[0] == '.'):
            # it is relative path
            user_path = user_path[1:]
            while (user_path[0] == '.'):
                cd_variable_temp = os.path.dirname(cd_variable_temp)

                # pop the dot
                user_path = user_path[1:]
            hdl_path = os.path.join(cd_variable_temp, user_path)
        else:
            # it is absolute path
            hdl_path = user_path

    elif (user_cmd=='masm'):
        if len(userinpt.split(' ')) == 1:
            # it is put over here
            macros_path = os.path.join(cd_variable, masm_macroassemblydotpy)
            continue

        cd_variable_temp = cd_variable
        user_path = userinpt.split(' ')[1].strip()
        # compute family tree of path
        if (user_path[0] == '.'):
            # it is relative path
            user_path = user_path[1:]
            while (user_path[0] == '.'):
                cd_variable_temp = os.path.dirname(cd_variable_temp)

                # pop the dot
                user_path = user_path[1:]
            macros_path = os.path.join(cd_variable_temp, user_path)
        else:
            # it is absolute path
            macros_path = user_path

    elif (user_cmd=="help"):
        print(help_command)

    else:
        print("type help!")

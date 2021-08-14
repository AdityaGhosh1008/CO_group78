import sys
from sys import stdin
complete_input = sys.stdin.read()
def errorgen(array):
    error= False
    if len(array)>256:
            print("Instruction Number Exceeded limit")
            error=True
    if error==False:
        error=checksyntax(array)
    if error==False:
        error=checkundefvariables(array)
    if error==False:
        error=errorchecklabels(array)
    if error==False:
        error=checkflags(array)
    if error==False:
        error=checkimm(array)
    if error==False:
        error=checklabelsandvar(array)
    if error==False:
        error=checkvar(array)
    if error==False:
        error= checkforhlt(array)
    if error==False:
        error=checktypos(array)
    return error
def checkbin(str):
    check="01"
    for i in range(len(str)):
        if str not in check:
            return False
    return True
def checktypos(array):
    for i in range(len(array)):
        line=array[i].split(" ")
        if len(line)==0:
                continue
        if line[0][len(line[0])-1]!=":":
            if len(line)==1:
                if line[0]!="hlt" :
                    print("Error typo in halting function at line"+ str(i+1))
                    return True
            if len(line)==2:
                if line[0]!="jmp"and line[0]!="jlt"and line[0]!="jgt"and line[0]!="je":
                    print("Error typo in "+line[0]+ " at line " +str(i+1))
                    return True   
            if len(line)==3:
                if line[0]!="mov" and line[0]!="ld" and line[0]!="st" and line[0]!="div"and line[0]!="rs" and line[0]!="ls" and line[0]!="not"and line[0]!="cmp":
                    print("Error typo in "+line[0]+ " at line " +str(i+1))
                    return True
                if line[1] !="R0" and line[1]!="R1" and line[1]!="R2"and line[1]!="R3" and line[1]!="R4" and line[1]!="R5"and line[1]!="R6":
                    print("Error typo in "+line[1]+ " at line " +str(i+1))
                    return True
                if line[2][0]!="$":
                    if line[2] !="R0" and line[2]!="R1" and line[2]!="R2"and line[2]!="R3" and line[2]!="R4" and line[2]!="R5"and line[1]!="R6":
                        print("Error typo in "+line[2]+ " at line " +str(i+1))
                        return True
            if len(line)==4:
                    if line[0]!="add" and line[0]!="sub" and line[0]!="mul"and line[0]!="xor" and line[0]!="or"and line[0]!="and":
                        print("Error typo in "+line[0]+ " at line " +str(i+1))
                        return True
                    if line[1] !="R0" and line[1]!="R1" and line[1]!="R2"and line[1]!="R3" and line[1]!="R4" and line[1]!="R5"and line[1]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
                    if line[2] !="R0" and line[2]!="R1" and line[2]!="R2"and line[2]!="R3" and line[2]!="R4" and line[2]!="R5"and line[2]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
                    if line[3] !="R0" and line[3]!="R1" and line[3]!="R2"and line[3]!="R3" and line[3]!="R4" and line[3]!="R5"and line[3]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
        else:
            line.pop(0)
            if len(line)==0:
                continue
            if len(line)==1:
                if line[0]!="hlt" :
                    print("Error typo in halting function at line"+ str(i+1))
                    return True
            if len(line)==2:
                if line[0]!="jmp"and line[0]!="jlt"and line[0]!="jgt"and line[0]!="je" and line[0]!="var":
                    print("Error typo in "+line[0]+ " at line " +str(i+1))
                    return True   
            if len(line)==3:
                if line[0]!="mov" and line[0]!="ld" and line[0]!="st" and line[0]!="div"and line[0]!="rs" and line[0]!="ls" and line[0]!="not"and line[0]!="cmp":
                    print("Error typo in "+line[0]+ " at line " +str(i+1))
                    return True
                if line[1] !="R0" and line[1]!="R1" and line[1]!="R2"and line[1]!="R3" and line[1]!="R4" and line[1]!="R5"and line[1]!="R6" and line!="FLAGS":
                    print("Error typo in "+line[1]+ " at line " +str(i+1))
                    return True
                if line[2][0]!="$":
                    if line[2] !="R0" and line[2]!="R1" and line[2]!="R2"and line[2]!="R3" and line[2]!="R4" and line[2]!="R5"and line[1]!="R6":
                        print("Error typo in "+line[2]+ " at line " +str(i+1))
                        return True
            if len(line)==4:
                    if line[0]!="add" and line[0]!="sub" and line[0]!="mul"and line[0]!="xor" and line[0]!="or"and line[0]!="and":
                        print("Error typo in "+line[0]+ " at line " +str(i+1))
                        return True
                    if line[1] !="R0" and line[1]!="R1" and line[1]!="R2"and line[1]!="R3" and line[1]!="R4" and line[1]!="R5"and line[1]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
                    if line[2] !="R0" and line[2]!="R1" and line[2]!="R2"and line[2]!="R3" and line[2]!="R4" and line[2]!="R5"and line[2]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
                    if line[3] !="R0" and line[3]!="R1" and line[3]!="R2"and line[3]!="R3" and line[3]!="R4" and line[3]!="R5"and line[3]!="R6":
                        print("Error typo in "+line[1]+ " at line " +str(i+1))
                        return True
    return False
def checkalphanum(str):
    for i in range(len(str)):
        if str[i] not in "abcdefghijklmnopqrstuvwxyz1234567890_":
            return False
    return True
def checkundefvariables(array):
    line=[]
    var=[]
    for i in range(len(array)):
        line=array[i].split()
        if line[0]=="var":
            if (checkalphanum(line[1])):
                var.append(line[1])
            else:
                print("Variable not valid in line :"+ str(i+1))
                return True
        if line[0]=="ld"or line[0]=="st":
            if line[1] not in var:
                print("Variable not valid in line :"+ str(i+1))
                return True
        return False
def errorchecklabels(array):
    line=[]
    labels=[]
    for i in range(len(array)):
        line=array[i].split()
        if line[0][len(line[0]-1)]==":":
            if(checkalphanum(line[0][0:len(line[0]-1)])):
                labels.append(line[0][0:len(line[0]-1)])
            else:
                print("Label not valid in line :"+ str(i+1))
                return True
        if line[0]=="jmp"or line[0]=="jlt" or line[0]=="jgt"or line[0]=="je" :
            if line[1] not in labels:
                print("Label not valid in line :"+ str(i+1))
                return True
        return False
def checksyntax(input_array):
    instr_array = ["add", "sub", "mov", "ld", "st", "mul", "div", "rs", "ls",
               "xor", "or", "and", "not", "cmp", "jmp", "jlt", "jgt", "je",
               "hlt", "var"]
    
    for i in range(len(input_array)):
        line = input_array[i].split()
        length = len(line)
        if line[0] not in instr_array:
            print("SyntaxError: NO SUCH INSTRUCTION FOUND")
            print("Error found at line " + str(i+1))
            return True
        else:
            if length == 1:
                if line[0] != "hlt":
                    print("SyntaxError: INVALID INSTRUCTION TYPE")
                    print("Error found at line " + str(i + 1))
                    return True
            elif length == 2:
                find = search(instr_array, line[0])
                if find not in ["var", "jmp", "jlt", "jgt", "je"]:
                    print("SyntaxError: INVALID INSTRUCTION TYPE")
                    print("Error found at line " + str(i + 1))
                    return True
            elif length == 3:
                find = search(instr_array, line[0])
                if find not in ["mov", "ld", "st", "div", "rs", "ls", "not", "cmp"]:
                    print("SyntaxError: INVALID INSTRUCTION TYPE")
                    print("Error found at line " + str(i + 1))
                    return True
            elif length == 4:
                find = search(instr_array, line[0])
                if find not in ["add", "sub", "mul", "xor", "or", "and"]:
                    print("SyntaxError: INVALID INSTRUCTION TYPE")
                    print("Error found at line " + str(i + 1))
                    return True
            else:
                print("SyntaxError: TOO LONG INSTRUCTION")
                print("Error found at line " + str(i + 1))
                return True
    return False
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return arr[i]
    return -1
def checkforhlt(input_array):
    for i in range(len(input_array)):
        line = input_array[i].split()
        if line[0] == "hlt":
            if i!=len(input_array)-1:
                print("HaltErr0r: NO LINE SHOULD BE TAKEN AFTER HALT INSTRUCTION")
                print("Error at line " + str(i+1))
                return True
        if i == len(input_array) - 1:
            if line[0]!="hlt":
                print("HaltError: INSTRUCTION FOR ENDING PROGRAM ABSENT")
                print("Error at line " + str(i+1))
                return True
    return False           
def checkimm(array):
    for i in range(len(array)):
        line=array[i].split(" ")
        for j in range(len(line)):
            if line[j][0]=="$":
                if int(line[j][1:-1])<0 or int(line[j][1:-1])>255:
                    print("IMM Value not valid in line no: " + str(i+1))
                    return True
    return False
def checklabelsandvar(array):
    line=[]
    labels=[]
    for i in range(len(array)):
        line=array[i].split()
        if line[0][len(line[0]-1)]==":":
            labels.append(line[0][0:len(line[0]-1)])
    newline=[]
    for i in range(len(array)):
        newline=array[i].split()
        if newline[0]=="var":
            if newline[1] in labels:
                print("Label/variable aldready exists Error in line "+ str(i+1));
                return True
    return False
def checkvar(input_array):
    arr = []
    count = 0
    for i in range(len(input_array)):
        line = input_array[i].split(" ")
        if line[0] == "var":
            count += 1
            arr.append("t")
        else:
            arr.append("f")
    for i in range(count):
        if arr[i] != "t":
            print("VarError: VARIABLE INSTRUCTION SHOULD BE BEFORE ALL SYSTEM INSTRUCTIONS")
            print("Error at line " + str(i+1))
            return True
    return False
def checkflags(input_array):
    arr = []
    for i in range(len(input_array)):
        line = input_array[i].split(" ")
        arr.append(line)
    for i in range(len(input_array)):
        if len(arr[i]) > 2:
            if arr[i][2] == "FLAGS":
                if arr[i][0] != "mov":
                    print("FlagError: INCORRECT USE OF FLAGS")
                    print("Error at line "+ str(i+1))
                    return True
    return False
def gin(a):
    ut = ""
    for i in range(7, -1, -1):
        if 2 ** i <= a:
            a = a % (2 ** i)
            ut += "1"
        else:
            ut += "0"
    return ut
def convert_to_binary(array):
    lop = []
    for i in range(0, len(array)):
        arrk = array[i].split(" ")
        lop.append(arrk)
    o = []
    p = []
    j = []
    u = ["hlt"]
    for i in range(0, len(array)):
        if lop[i][0] != "var" and lop[i][0] != "hlt":
            o.append(lop[i])
        elif lop[i] == u:
            p.append(lop[i])
        else:
            j.append(lop[i])
    o = o + p + j
    k = []
    for i in range(0, len(o)):
        if o[i][0] == "add":
            k.append("0000000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "sub":
            k.append("0000100")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "mov":
            if o[i][2][0] == "$":
                k.append("00010")
                r = 1
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
                ben = ""
                for v in range(1, len(o[i][2])):
                    ben += o[i][2][v]
                ben = int(ben)
                k[i] += gin(ben)

            else:
                k.append("0001100000")
                for r in range(1, len(o[i])):
                    if o[i][r] == "R0":
                        k[i] = k[i] + "000"
                    elif o[i][r] == "R1":
                        k[i] = k[i] + "001"
                    elif o[i][r] == "R2":
                        k[i] += "010"
                    elif o[i][r] == "R3":
                        k[i] += "011"
                    elif o[i][r] == "R4":
                        k[i] += "100"
                    elif o[i][r] == "R5":
                        k[i] += "101"
                    elif o[i][r] == "R6":
                        k[i] += "110"
                    elif o[i][r] == "FLAGS":
                        k[i] += "111"
        elif o[i][0] == "ld":
            k.append("00100")
            r = 1
            if o[i][r] == "R0":
                k[i] = k[i] + "000"
            elif o[i][r] == "R1":
                k[i] = k[i] + "001"
            elif o[i][r] == "R2":
                k[i] += "010"
            elif o[i][r] == "R3":
                k[i] += "011"
            elif o[i][r] == "R4":
                k[i] += "100"
            elif o[i][r] == "R5":
                k[i] += "101"
            elif o[i][r] == "R6":
                k[i] += "110"
            elif o[i][r] == "FLAGS":
                k[i] += "111"
            una = o[i][2]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)

        elif o[i][0] == "st":
            k.append("00101")
            r = 1
            if o[i][r] == "R0":
                k[i] = k[i] + "000"
            elif o[i][r] == "R1":
                k[i] = k[i] + "001"
            elif o[i][r] == "R2":
                k[i] += "010"
            elif o[i][r] == "R3":
                k[i] += "011"
            elif o[i][r] == "R4":
                k[i] += "100"
            elif o[i][r] == "R5":
                k[i] += "101"
            elif o[i][r] == "R6":
                k[i] += "110"
            elif o[i][r] == "FLAGS":
                k[i] += "111"
            una = o[i][2]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)

        elif o[i][0] == "mul":
            k.append("0011000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "div":
            k.append("0011100000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "rs":
            k.append("01000")
            r = 1
            if o[i][r] == "R0":
                k[i] = k[i] + "000"
            elif o[i][r] == "R1":
                k[i] = k[i] + "001"
            elif o[i][r] == "R2":
                k[i] += "010"
            elif o[i][r] == "R3":
                k[i] += "011"
            elif o[i][r] == "R4":
                k[i] += "100"
            elif o[i][r] == "R5":
                k[i] += "101"
            elif o[i][r] == "R6":
                k[i] += "110"
            elif o[i][r] == "FLAGS":
                k[i] += "111"
            ben = ""
            for v in range(1, len(o[i][2])):
                ben += o[i][2][v]
            ben = int(ben)
            k[i] += gin(ben)
        elif o[i][0] == "ls":
            k.append("01001")
            r = 1
            if o[i][r] == "R0":
                k[i] = k[i] + "000"
            elif o[i][r] == "R1":
                k[i] = k[i] + "001"
            elif o[i][r] == "R2":
                k[i] += "010"
            elif o[i][r] == "R3":
                k[i] += "011"
            elif o[i][r] == "R4":
                k[i] += "100"
            elif o[i][r] == "R5":
                k[i] += "101"
            elif o[i][r] == "R6":
                k[i] += "110"
            elif o[i][r] == "FLAGS":
                k[i] += "111"
            ben = ""
            for v in range(1, len(o[i][2])):
                ben += o[i][2][v]
            ben = int(ben)
            k[i] += gin(ben)
        elif o[i][0] == "xor":
            k.append("0101000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "or":
            k.append("0101100")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "and":
            k.append("0110000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "not":
            k.append("0110100000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] += "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "cmp":
            k.append("0111000000")
            for r in range(1, len(o[i])):
                if o[i][r] == "R0":
                    k[i] = k[i] + "000"
                elif o[i][r] == "R1":
                    k[i] = k[i] + "001"
                elif o[i][r] == "R2":
                    k[i] += "010"
                elif o[i][r] == "R3":
                    k[i] += "011"
                elif o[i][r] == "R4":
                    k[i] += "100"
                elif o[i][r] == "R5":
                    k[i] += "101"
                elif o[i][r] == "R6":
                    k[i] = "110"
                elif o[i][r] == "FLAGS":
                    k[i] += "111"
        elif o[i][0] == "jmp":
            k.append("01111000")
            una = o[i][1]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)
        elif o[i][0] == "jlt":
            k.append("10000000")
            una = o[i][1]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)

        elif o[i][0] == "jgt":
            k.append('10001000')
            una = o[i][1]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)

        elif o[i][0] == "je":
            k.append("10010000")
            una = o[i][1]
            for u in range(i, len(o)):
                if o[u][0] == "var" and o[u][1] == una:
                    jam = u
            k[i] += gin(jam)

        elif o[i][0] == "hlt":
            k.append("1001100000000000")
    for t in k:
        print(t)
arr = []
for line in stdin:
    if line == '':
        break
    arr.append(line)
truth=errorgen(arr)
if (truth==False):
    convert_to_binary(arr)
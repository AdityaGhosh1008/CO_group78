R0="0000000000000000"
R1="0000000000000000"
R2="0000000000000000"
R3="0000000000000000"
R4="0000000000000000"
R5="0000000000000000"
R6="0000000000000000"
FLAGS="0000000000000000"
RF=[R0,R1,R2,R3,R4,R5,R6,FLAGS]
arr = []

def mem_dump(array):
    arr = []
    for i in range(256):
        arr.append("0000000000000000")

    for i in range(len(array)):
        arr[i] = array[i]

    for i in arr:
        print(i)
def bin_to_int(inp):
    k = 0
    l = 7
    for i in inp:
        i = int(i)
        if i == 1:
            k += 2**l
        l-=1
    return k
def int_to_bin(inp):
    ut = ""
    for i in range(7, -1, -1):
        if 2 ** i <= inp:
            inp = inp % (2 ** i)
            ut += "1"
        else:
            ut += "0"
    return ut
def indexval(inp):
    if inp == '000':
        return 0   
    elif inp == '001':
        return 1
    elif inp =='010':
        return 2
    elif inp =='011':
        return 3
    elif inp =='100':
        return 4
    elif inp =='101':
        return 5
    elif inp=='110':
        return 6
def execute(line,RF):
    opcode_bin = line[0:5]
    if(opcode_bin == "00000"):
        RF=add(line,RF)
    elif(opcode_bin=="00001"):
        RF=sub(line,RF)
    elif(opcode_bin=="00010"):
        RF=movimm(line,RF)
    elif(opcode_bin=="00011"):
        RF=mov(line,RF)
    elif(opcode_bin=="00100"):
        RF=load(line,RF)
    elif (opcode_bin=="00101"):
        RF=st(line,RF)
    elif (opcode_bin=="00110"):
        RF=mul(line,RF)
    elif (opcode_bin=="00111"):
        RF=div(line,RF)
    elif (opcode_bin=="01000"):
        RF=rs(line,RF)
    elif (opcode_bin=="01001"):
        RF=ls(line,RF)
    elif (opcode_bin=="01010"):
        RF=xor(line,RF)
    elif (opcode_bin=="01011"):
        RF=OR(line,RF)
    elif (opcode_bin=="01100"):
        RF=AND(line,RF)
    elif (opcode_bin=="01101"):
        RF=inv(line,RF)
    elif (opcode_bin=="01110"):
        RF=comp(line,RF)
    elif (opcode_bin=="01111"):
        RF=unc_jump(line,RF)
    elif (opcode_bin=="10000"):
        RF=jump_less(line,RF)
    elif (opcode_bin=="10001"):
        RF=jump_great(line,RF)
    elif (opcode_bin=="10010"):
        RF=jump_equal(line,RF)
    return RF
def PC_dump(pc):
    print((bin(pc)[2:]).zfill(8),end=" ")
def RF_dump(RF):
    print(*RF)
def PC_update(line,pc):
    if line[0:5]=="01111":
        return bin_to_int(line[8:])
    elif line[0:5]=="10000" and RF[7][13]=="1":
        RF[7] = "0000000000000000"
        return bin_to_int(line[8:])
    elif line[0:5]=="10001"and RF[7][14]=="1":
        RF[7] = "0000000000000000"
        return bin_to_int(line[8:])
    elif line[0:5]=="10010"and RF[7][15]=="1":
        RF[7] = "0000000000000000"
        return bin_to_int(line[8:])
    else:
        return pc+1
def main(array):
    pc=0
    while array[pc]!="1001100000000000" :
        RF=execute(array[pc],RF)
        PC_dump(pc)
        RF_dump(RF)
        PC_update(array[pc],pc)
    mem_dump(array)
for q in stdin:
    if q == '': # If empty string is read then stop the loop
        break
    q = q.replace("\n", "")
    arr.append(q)
main(arr)




R0="0000000000000000"
R1="0000000000000000"
R2="0000000000000000"
R3="0000000000000000"
R4="0000000000000000"
R5="0000000000000000"
R6="0000000000000000"
FLAGS="0000000000000000"
RF=[R0,R1,R2,R3,R4,R5,R6,FLAGS]
def execute(line,RF):
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




from sys import stdin
R0="0000000000000000"
R1="0000000000000000"
R2="0000000000000000"
R3="0000000000000000"
R4="0000000000000000"
R5="0000000000000000"
R6="0000000000000000"
FLAGS="0000000000000000"
global RF 
RF=[R0,R1,R2,R3,R4,R5,R6,FLAGS]
arr=[]
def add(line,RF):
    r0=line[7:10]
    r1=line[10:13]
    r2=line[13:]
    k1=RF[indexval(r1)]
    k2=RF[indexval(r2)]
    k=bin_to_int(k1)+bin_to_int(k2)
    if k<65536:
        RF[indexval(r0)] = int_to_bin(k)
    else:
        k = k - 65535
        RF[indexval(r0)] = int_to_bin(k)
        res = []
        for i in range(16):
            if i != 12:
                res.append('0')
            else:
                res.append('1')
        k3 = ''
        for i in range(16):
            k3 += res[i]
        RF[7] = k3
    return RF
def sub(line,RF):
    r0=line[7:10]
    r1=line[10:13]
    r2=line[13:]
    k1=RF[indexval(r1)]
    k2=RF[indexval(r2)]
    over = ''
    k=bin_to_int(k1)-bin_to_int(k2)
    if k>=0:
        RF[indexval(r0)] = int_to_bin(k)
    else:
        for i in range(16):
            over += '0'
        RF[indexval(r0)] = over
        res = []
        for i in range(16):
            if i!=12:
                res.append('0')
            else:
                res.append('1')
        k3 = ''
        for i in range(16):
            k3+=res[i]
        RF[7] = k3
    return RF
def movimm(line,RF):
    r0=line[5:8]
    val=line[8:]
    RF[indexval(r0)]="00000000"+val
    return RF
def mov(line,RF):
    r0=line[10:13]
    r1=line[13:]
    RF[indexval(r0)]=RF[indexval(r1)]
    return RF
def mul(line,RF):
    r0=line[7:10]
    r1=line[10:13]
    r2=line[13:]
    over=""
    k0=RF[indexval(r0)]
    k1=RF[indexval(r1)]
    k2=RF[indexval(r2)]
    k=bin_to_int(k1)*bin_to_int(k2)
    if k < 65536:
        RF[indexval(r0)] = int_to_bin(k)
    else:
        k = k - 65535
        RF[indexval(r0)] = int_to_bin(k)
        for i in range(16):
            over += '0'
        RF[indexval(r0)] = over
        res = []
        for i in range(16):
            if i!=12:
                res.append('0')
            else:
                res.append('1')
        k3 = ''
        for i in range(16):
            k3+=res[i]
        RF[7] = k3
    return RF
def div(line,RF):
    r0=line[10:13]
    r1=line[13:]
    k0=RF[indexval(r0)]
    k1=RF[indexval(r1)]
    j0=int(bin_to_int(k0)//bin_to_int(k1))
    j1=int(bin_to_int(k0)%bin_to_int(k1))
    RF[0]=int_to_bin(j0)
    RF[1]=int_to_bin(j1)
    return RF
def ls(line,RF):
    imm = line[8:]
    r0 = line[5:8]
    shift_val = bin_to_int(imm)
    res1 = []
    final_res = ''
    if shift_val > 16:
        for i in range(16):
            res1.append('0')
        for i in res1:
            final_res+= i
    else:
        res2 = list(r0)
        while shift_val!=0:
            res2.pop(0)
            res2.append('0')
            shift_val-=1
        for j in res2:
            final_res += j
    RF[indexval(r0)] = final_res
    return RF
def rs(line,RF):
    imm = line[8:]
    r0 = line[5:8]
    shift_val = bin_to_int(imm)
    res1 = []
    final_res = ''
    if shift_val > 16:
        for i in range(16):
            res1.append('0')
        for i in res1:
            final_res += i
    else:
        g = ''
        for i in range(shift_val):
            g+='0'
        k = RF[indexval(r0)]
        f = k[shift_val:]
        final_res = g+f
    RF[indexval(r0)] = final_res
    return RF
def OR(line, RF):
    r0 = line[7:10]
    r1 = line[10:13]
    r2 = line[13:]
    k0 = RF[indexval(r0)]
    k1 = RF[indexval(r1)]
    k2 = RF[indexval(r2)]
    A = list(k1)
    B = list(k2)
    i = 0
    while i<16:
        if A[i]=='0' and B[i]=='0':
            k0[i] = '0'
        else:
            k0[i] = '1'
        i+=1
    RF[indexval(r0)] = k0
    return RF
def AND(line, RF):
    r0 = line[7:10]
    r1 = line[10:13]
    r2 = line[13:]
    k0 = RF[indexval(r0)]
    k1 = RF[indexval(r1)]
    k2 = RF[indexval(r2)]
    A = list(k1)
    B = list(k2)
    i = 0
    while i<16:
        if A[i]=='1' and B[i]=='1':
            k0[i] = '1'
        else:
            k0[i] = '0'
        i+=1
    RF[indexval(r0)] = k0
    return RF
def XOR(line, RF):
    r0 = line[7:10]
    r1 = line[10:13]
    r2 = line[13:]
    k0 = RF[indexval(r0)]
    k1 = RF[indexval(r1)]
    k2 = RF[indexval(r2)]
    A = list(k1)
    B = list(k2)
    i = 0
    while i<16:
        if A[i]!=B[i]:
            k0[i] = '1'
        else:
            k0[i] = '0'
        i+=1
    RF[indexval(r0)] = k0
    return RF
def NOT(line, RF):
    r0 = line[10:13]
    r1 = line[13:]
    k1 = RF[indexval(r1)]
    res1 = list(k1)
    res2 = []
    for i in res1:
        if i == '0':
            res2.append('1')
        else:
            res2.append('0')
    final_res = ''
    for i in res2:
        final_res += i
    RF[indexval(r0)] = final_res
    return RF
def cmp(line, RF):
    r0 = line[10:13]
    r1 = line[13:]
    k0 = RF[indexval(r0)]
    k1 = RF[indexval(r1)]
    k2 = ''
    x = bin_to_int(k0)
    y = bin_to_int(k1)
    res = []
    if x<y:
        for i in range(16):
            if i!=13:
                res.append('0')
            else:
                res.append('1')
    elif x>y:
        for i in range(16):
            if i!=14:
                res.append('0')
            else:
                res.append('1')
    elif x==y:
        for i in range(16):
            if i!=15:
                res.append('0')
            else:
                res.append('1')
    for j in res:
        k2 += j
    RF[7] = k2
    return RF
def mem_dump(array):
    for i in array:
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
    for i in range(15, -1, -1):
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
    elif inp=='111':
        return 7
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
        RF=XOR(line,RF)
    elif (opcode_bin=="01011"):
        RF=OR(line,RF)
    elif (opcode_bin=="01100"):
        RF=AND(line,RF)
    elif (opcode_bin=="01101"):
        RF=NOT(line,RF)
    elif (opcode_bin=="01110"):
        RF=cmp(line,RF)
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
def load(line,RF):
    mem_add=line[8:]
    RF[indexval(line[5:8])]=mem_state[int_to_bin(mem_add)]
    return RF
def st(line,RF):
    mem_add=line[8:]
    mem_state[bin_to_int(mem_add)]=RF[indexval(line[5:8])]
    return RF
def main(array,RF):
    pc=0
    while array[pc]!="1001100000000000" :
        RF=execute(array[pc],RF)
        PC_dump(pc)
        RF_dump(RF)
        pc=PC_update(array[pc],pc)
    PC_dump(pc)
    RF_dump(RF)
    mem_dump(array)
for q in stdin:
    if q == '': # If empty string is read then stop the loop
        break
    q = q.replace("\n", "")
    arr.append(q)
mem_state=[]
for i in range(256):
    mem_state.append("0000000000000000")
for i in range(len(arr)):
    mem_state[i]=arr[i]
main(mem_state,RF)




import urllib2
import math

def get_data2():
    mem = "3,9,8,9,10,9,4,9,99,-1,8"
    mem = map(lambda x: int(x), mem.split(',') )
   
    return mem

def get_data3():
    mem = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
    mem = map(lambda x: int(x), mem.split(',') )
   
    return mem

def get_data():
    mem = "3,225,1,225,6,6,1100,1,238,225,104,0,1,192,154,224,101,-161,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,157,48,224,1001,224,-61,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,15,28,225,1002,162,75,224,1001,224,-600,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,102,32,57,224,1001,224,-480,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,6,23,225,1102,15,70,224,1001,224,-1050,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,101,53,196,224,1001,224,-63,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,64,94,225,1102,13,23,225,1101,41,8,225,2,105,187,224,1001,224,-60,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,10,23,225,1101,16,67,225,1101,58,10,225,1101,25,34,224,1001,224,-59,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1108,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,404,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,419,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,464,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,659,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"
    mem = map(lambda x: int(x), mem.split(',') )
    return mem

def run_comp():
    memory = get_data()

    inst_ptr = 0 # Instruction pointer
    while True:
        d = "0000" + str(memory[inst_ptr])
        code = int(d[-2:])
        p1 = int(d[-3])
        p2 = int(d[-4])
        p3 = int(d[-5])

       # print(memory)
        #print(d[-5:])
       # print("InstPtr:" + str(inst_ptr))
        if code == 1:
            # 2, 50, 50, 60 - Add the first two numbers and store in the third number memory
            op1 = memory[inst_ptr+1] # Immediate mode
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            op3 = memory[inst_ptr+3]
            
            memory[op3] = op1 + op2
            inst_ptr += 4
        elif code == 2:
            # 2, 50, 50, 60 - Multiply the first two numbers and store in the third number memory
            op1 = memory[inst_ptr+1]
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            op3 = memory[inst_ptr+3]

            memory[op3] = op1 * op2
            inst_ptr += 4  
        elif code == 3:
            # 3, 50 - read input and put in address denoted
            x = int(input("Input:"))
            op1 = memory[inst_ptr+1]
            memory[op1] = x
            inst_ptr += 2
        elif code == 4:
            # 4, 50 - output value at address denoted
            op1 = memory[inst_ptr+1]
            print(memory[op1])
            inst_ptr += 2
        elif code == 5:
            # Jump-if-true - Set instruction pointer if op1 is nonzero
            op1 = memory[inst_ptr+1]
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            
            if op1 > 0:
                inst_ptr = op2
            else:
                inst_ptr += 3
        elif code == 6:
            # Jump-if-false - Set instruction pointer if op1 is zero
            op1 = memory[inst_ptr+1]
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            
            if op1 == 0:
                inst_ptr = op2
            else:
                inst_ptr += 3
        elif code == 7:
            # less than - if first param is less than second param, store 1 in position given by third param, else store 0
            op1 = memory[inst_ptr+1]
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            op3 = memory[inst_ptr+3]

            if op1 < op2:
                memory[op3] = 1
            else:
                memory[op3] = 0
            inst_ptr += 4  
        elif code == 8:
            # less than - if first param is less than second param, store 1 in position given by third param, else store 0
            op1 = memory[inst_ptr+1]
            if not p1: # position mode, get reference
                op1 = memory[op1]
            op2 = memory[inst_ptr+2]
            if not p2: # position mode, get reference
                op2 = memory[op2]
            op3 = memory[inst_ptr+3]
           
            if op1 == op2:
                memory[op3] = 1
            else:
                memory[op3] = 0
            inst_ptr += 4  
        elif code == 99:
            break 
        

    return memory[0]

def main():
    out = run_comp()
	#print(fn())

if __name__=="__main__":
	main()
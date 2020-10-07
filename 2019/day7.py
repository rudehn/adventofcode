import urllib2
import math
import time
import threading
import Queue
from itertools import permutations

class IntcodeComp:

    def __init__(self, memory):
        self.memory = memory
        self.inst_ptr = 0 # Instruction pointer
        self.rel_base = 0 # Relative base of instruction pointer offset

    def execute(self, inputs, outputs):
        self.rel_base = 0
        while True:
            d = "0000" + str(self.memory[self.inst_ptr])
            code = int(d[-2:])
            p1_mode = int(d[-3])
            p2_mode = int(d[-4])
            p3_mode = int(d[-5])

            #print(d)
            #print("Inst:" + str(self.inst_ptr) + " Rel:" + str(self.rel_base))

            if code == 1:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
                op3 = self.get_op(self.inst_ptr + 3, self.rel_base, 1)
              
                # 2, 50, 50, 60 - Add the first two numbers and store in the third number self.memory
                self.write_mem(op3, self.rel_base, op1 + op2, p3_mode)
                self.inst_ptr += 4
            elif code == 2:
                # 2, 50, 50, 60 - Multiply the first two numbers and store in the third number memory
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
                op3 = self.get_op(self.inst_ptr + 3, self.rel_base, 1)
              
                self.write_mem(op3, self.rel_base, op1 * op2, p3_mode)
                self.inst_ptr += 4  
            elif code == 3:
                # 3, 50 - read input and put in address denoted
                # while inputs.empty():
                #     print("Here")
                #     time.sleep(.05)

                x = inputs.get()
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, 1)
                self.write_mem(op1, self.rel_base, x, p1_mode)
               
                self.inst_ptr += 2
            elif code == 4:
                # 4, 50 - output value at address denoted
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                outputs.put(op1)
                self.inst_ptr += 2
            elif code == 5:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
               
                if op1 > 0:
                    self.inst_ptr = op2
                else:
                    self.inst_ptr += 3
            elif code == 6:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
                         
                if op1 == 0:
                    self.inst_ptr = op2
                else:
                    self.inst_ptr += 3
            elif code == 7:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
                op3 = self.get_op(self.inst_ptr + 3, self.rel_base, 1)
              
                if op1 < op2:
                    self.write_mem(op3, self.rel_base, 1, p3_mode)
                else:
                    self.write_mem(op3, self.rel_base, 0, p3_mode)
                self.inst_ptr += 4  
            elif code == 8:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                op2 = self.get_op(self.inst_ptr + 2, self.rel_base, p2_mode)
                op3 = self.get_op(self.inst_ptr + 3, self.rel_base, 1)
                
                if op1 == op2:
                    self.write_mem(op3, self.rel_base, 1, p3_mode)
                else:
                    self.write_mem(op3, self.rel_base, 0, p3_mode)
                self.inst_ptr += 4  
            elif code == 9:
                op1 = self.get_op(self.inst_ptr + 1, self.rel_base, p1_mode)
                self.rel_base += op1
                self.inst_ptr += 2
            elif code == 99:
                break 
            
        return outputs


    def write_mem(self, write_addr, rel_ptr, val, w_mode):
        if w_mode == 2:
            self.memory[rel_ptr + write_addr] = val
        else:
            self.memory[write_addr] = val

    def get_op(self, inst_ptr, rel_ptr, mode):
        op = self.memory.get(inst_ptr, 0) # Immediate mode
        
        if mode == 0:
            op = self.memory.get(op, 0) # Position mode
        elif mode == 1:
            pass
        elif mode == 2:
            op = self.memory.get(rel_ptr + op, 0) # Relative mode
        else:
            raise Exception("Invalid mode:" + str(mode))

        return op


def get_data2():
    mem = "3,9,8,9,10,9,4,9,99,-1,8"
    mem = {i:int(x) for i, x in enumerate(mem.split(','))}
    return mem

def get_data3():
    mem = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    mem = {i:int(x) for i, x in enumerate(mem.split(','))}
    return mem

def get_data4():
    mem = "1102,34915192,34915192,7,4,7,99,0"
    mem = {i:int(x) for i, x in enumerate(mem.split(','))}
    return mem

def get_data5():
    mem = "104,1125899906842624,99"
    mem = {i:int(x) for i, x in enumerate(mem.split(','))}
    return mem

def get_data():
    mem = "3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99"
    mem = {i:int(x) for i, x in enumerate(mem.split(','))}
    return mem


def main():

    global_signals = []


    for i in permutations([5,6,7,8,9]):

        threads = []

        signals = []
        p1,p2,p3,p4,p5 = i

        comp1 = IntcodeComp(get_data())
        comp2 = IntcodeComp(get_data())
        comp3 = IntcodeComp(get_data())
        comp4 = IntcodeComp(get_data())
        comp5 = IntcodeComp(get_data())

        c1_out = Queue.Queue()
        c1_out.put(p2)
        c2_out = Queue.Queue()
        c2_out.put(p3)
        c3_out = Queue.Queue()
        c3_out.put(p4)
        c4_out = Queue.Queue()
        c4_out.put(p5)
        c5_out = Queue.Queue()
        c5_out.put(p1)
        c5_out.put(0)

        t = threading.Thread(target=comp1.execute, args=(c5_out, c1_out))
        t2 = threading.Thread(target=comp2.execute, args=(c1_out, c2_out))
        t3 = threading.Thread(target=comp3.execute, args=(c2_out, c3_out))
        t4 = threading.Thread(target=comp4.execute, args=(c3_out, c4_out))
        t5 = threading.Thread(target=comp5.execute, args=(c4_out, c5_out))

        threads.extend([t,t2,t3,t4,t5])
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        global_signals.append(c5_out.get())

        # co1 = comp1.execute([p1, 0])
        # co2 = comp2.execute([p2, co1[0]])
        # co3 = comp3.execute([p3, co2[0]])
        # co4 = comp4.execute([p4, co3[0]])
        # co5 = comp5.execute([p5, co4[0]])

        # old_output = -1
        # curr_output = co5[0]
        # while curr_output != old_output:
        #     co1 = comp1.execute([co5[0]])
        #     co2 = comp2.execute([co1[0]])
        #     co3 = comp3.execute([co2[0]])
        #     co4 = comp4.execute([co3[0]])
        #     co5 = comp5.execute([co4[0]])
        #     signals.append(co5[0])
        #     old_output = curr_output
        #     curr_output = co5[0]
        #     print(old_output)

    print(max(global_signals))
	#print(fn())

if __name__=="__main__":
	main()
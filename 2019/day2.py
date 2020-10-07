import urllib2
import math

def read_input(url):
    for line in urllib2.urlopen(url):
        yield line

def get_data2():
    mem = "1,1,1,4,99,5,6,0,99"
    mem = map(lambda x: int(x), mem.split(',') )
    return mem

def get_data():
    mem = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0"
    mem = map(lambda x: int(x), mem.split(',') )
    return mem

def run_comp(noun, verb):
    memory = get_data()
    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory)-4, 4):
        code = memory[i]
        ops = memory[i+1:i+4]

        if code == 1:
            memory[ops[2]] = memory[ops[0]] + memory[ops[1]]
        elif code == 2:
            memory[ops[2]] = memory[ops[0]] * memory[ops[1]]
        elif code == 99:
            break   

    return memory[0]

def main():
    for noun in range(100):
        for verb in range(100):
            out = run_comp(noun, verb)
            if out == 19690720:
                print(noun)
                print(verb)
                print(100 * noun + verb)
	#print(fn())

if __name__=="__main__":
	main()
import getkey as gk

class Runner:
    def __init__(self, code):
        self.pos = 0
        self.code = code
        self.mem = [0]
        self.pointer = 0
        self.usedmem = []
        for i in range(29999):
            self.mem.append(0)

    def advance(self):
        self.pos += 1
        if self.pos == len(self.code):
            return False
        return True

    def readvance(self):
        self.pos -= 1
        if self.pos == -1:
            self.pos += 1
            
    def run(self):
        loopP = 0
        isloop = False
        opnloop = False
        clP = 0
        loopCL = False
        while self.pos < len(self.code):

            if self.code[self.pos] == ">": self.pointer += 1
            elif self.code[self.pos] == "<": self.pointer -= 1
            elif self.code[self.pos] == "+": 
                self.mem[self.pointer] += 1
                self.usedmem.append(self.pointer)
            elif self.code[self.pos] == "-": 
                self.mem[self.pointer] -= 1
                self.usedmem.append(self.pointer)

            elif self.code[self.pos] == ".": print(chr(self.mem[self.pointer]), end="")
            elif self.code[self.pos] == ",": 
                try:
                    self.mem[self.pointer] = ord(gk.getkey())
                    self.usedmem.append(self.pointer)
                except (EOFError, KeyboardInterrupt):
                    isloop = False
                    self.pos = clP
                    loopCL = True
                    
            elif self.code[self.pos] == "[":
                loopP = self.pointer
                loopPOS = self.pos
                opnloop = True
                loopCL = False
            elif self.code[self.pos] == "]":
                if opnloop == False:
                    if isloop == False:
                        if loopCL == False:
                            print("""error: closing brackets outside loop""")
                            exit(1)
                else:
                    clP = self.pos
                    isloop = True
                    opnloop = False
                
                if isloop == True:
                    self.pos = loopPOS

                if isloop == True:
                    if self.mem[self.pointer] == 0:
                        isloop = False
                        self.pos = clP
                        loopCL = True

            if self.pointer == -1:
                print("""error: invaild position of pointer in memory (underrun)""")
                exit(1)
            elif self.pointer == len(self.mem):
                print(f"""error: invaild position of pointer in memory (overrun) {len(self.mem)}""")
                exit(1)

            a = self.advance()
            if a == False: break

    def viewmem(self):
        p = 0
        for loc in self.mem:
            if p in self.usedmem:
                print(str(loc)+"|", end="")
            p += 1

        print()

runner = Runner(f"""
Your code here...


""")
runner.run()
# Uncomment this line to see memory after executing
#runner.viewmem()

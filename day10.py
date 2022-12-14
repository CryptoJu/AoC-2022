class krankerCPU():

    cycle = 0
    pointer = 0
    signal = 0
    crt = ""
    crt_index = 0
    x = 1
    _return_at = [20, 60, 100, 140, 180, 220]

    def step(self):

        self.cycle += 1

        if self.getCycle() in self._return_at:
            self.signal += self.cycle * self.x

        if self.x -1 <= self.crt_index and self.crt_index <= self.x + 1:
            self.crt += "😂"
        else:
            self.crt += "💥"
        self.crt_index += 1 if self.crt_index < 39 else -39

        if self.crt_index == 0:
            self.crt += "\n"
    
        
    def getSignal(self):
        print(self.signal)
    
    def getCycle(self):
        return(self.cycle)
    
    def draw(self):
        print(self.crt)
    
    


if __name__ == "__main__":
    with open('input/d10_input.txt', 'r') as f:
        data = f.readlines()

    cpu = krankerCPU()

    for line in data:
        cpu.step()
        if "addx" in line:
            cpu.step()
            amt = line.split()[1]
            cpu.x += int(amt)

    cpu.getSignal()
    cpu.draw()



import sys
from collections import deque

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

class Module:
    def __init__(self, name, outputs, q):
        self.name = name
        self.outputs = outputs
        self.q = q
        self.lowN, self.highN = 0, 0

    def addInput(self, input):
        pass

    def outPulse(self, pulse):
        for output in self.outputs:
            self.q.append((output, pulse, self.name))

    def low(self, origin):
        self.lowN += 1
        self.outPulse("low")

    def high(self, origin):
        self.highN += 1


class FlipFlop(Module):
    def __init__(self, name, outputs, q):
        super().__init__(name, outputs, q)
        self.on = False


    def low(self, origin):
        self.lowN += 1
        pulse = "low" if self.on else "high"
        super().outPulse(pulse)
        self.on = not self.on

    def high(self, origin):
        self.highN += 1


class Conjunction(Module):
    def __init__(self, name, outputs, q):
        super().__init__(name, outputs, q)
        self.inputs = {}

    def addInput(self, input):
        self.inputs[input] = "low"

    def low(self, origin):
        self.lowN += 1
        self.inputs[origin] = "low"
        super().outPulse("high")

    def high(self, origin):
        self.highN += 1
        self.inputs[origin] = "high"
        pulse = "low" if all(state=="high" for state in self.inputs.values()) else "high"
        super().outPulse(pulse)
        

q = deque()
modules = {}
for line in open(f):
    line = line.strip()
    if line[0] == "b":
        outputs = line[15:].split(', ')
        modules["broadcaster"] = Module("broadcaster", outputs, q)
        continue
    name = line[1:3]
    outputs = line[7:].split(', ')
    if line[0] == '%':
        modules[name] = FlipFlop(name, outputs, q)
    elif line[0] == '&':
        modules[name] = Conjunction(name, outputs, q)


outputOnly = []
modules["rx"] = Module("rx", [], q)
for module in modules.values():
    for output in module.outputs:
        modules[output].addInput(module.name)

for i in range(1):
    q.append(("broadcaster", "low", "button"))
    while q:
        name, pulse, origin = q.popleft()
        print("%s -%s-> %s" % (origin, pulse, name))
        send = getattr(modules[name], pulse)
        send(origin)
    if rxLow := modules["rx"].lowN >= 1:
        print("found %d at %d" % (rxLow, i))

totalLow, totalHigh = 0, 0
for module in modules.values():
    totalLow += module.lowN
    totalHigh += module.highN

print(totalLow, totalHigh)
print(totalLow * totalHigh)

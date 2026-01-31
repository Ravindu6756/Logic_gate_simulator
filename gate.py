class Nand:
    def __init__(self):
        self.a = False
        self.b = False
        self.f = True
        self.name = None
    
    def __repr__(self):
        return self.name
    
    def run(self):
        try:
            self.f = not(self.a * self.b)

        except:
            print("Empty Inputs")

class Wire:
    def __init__(self):
        self.x = None
        self.y = None
        self.name = None
        self.y = self.x
    
    def __repr__(self):
        return self.name

class In:
    def __init__(self):
        self.state = False
        self.name = None
    
    def __repr__(self):
        return self.name

    def toggle(self, signal):
        self.signal = signal
        self.state = self.signal

class Out:
    def __init__(self):
        self.stateO = False
        self.name = None
    
    def __repr__(self):
        return self.name

    def show(self, x):
        self.x = x
        self.stateO = self.x

    
class Platform:
    def __init__(self):
        self.button = []
        self.button_names = []
        self.gate = []
        self.gate_names = []
        self.show = []
        self.show_names = []
        self.wire = []
        self.wire_names = []
    

    def add(self, item, name):
        self.item = item
        self.name = name

        if item == "g":
            self.component = Nand()
            self.gate.append(self.component)
            self.gate_names.append(self.name)
            self.component.name = self.name
            print(f"Gate '{self.name}' created!")
        
        elif item == "b":
            self.component = In()
            self.button.append(self.component)
            self.button_names.append(self.name)
            self.component.name = self.name
            print(f"Input '{self.name}' created!")

        elif item == "w":
            self.component = Wire()
            self.wire.append(self.component)
            self.wire_names.append(self.name)
            self.component.name = self.name
            print(f"Wire '{self.name}' created!")

        elif item == "s":
            self.component = Out()
            self.show.append(self.component)
            self.show_names.append(self.name)
            self.component.name = self.name
            print(f"Output '{self.name}' created!")

    def search(self, item, name):
        self.item = item
        self.name = name
        item_id = None

        if self.item == "g":
            for i in range(len(self.gate_names)):
                if self.name == self.gate_names[i]:
                    item_id = i
                

            return self.gate[item_id]
        
        elif self.item == "b":
            for i in range(len(self.button_names)):
                if self.name == self.button_names[i]:
                    item_id = i
                

            return self.button[item_id]
        
        elif self.item == "w":
            for i in range(len(self.wire_names)):
                if self.name == self.wire_names[i]:
                    item_id = i
                

            return self.wire[item_id]
        
        elif self.item == "s":
            for i in range(len(self.show_names)):
                if self.name == self.show_names[i]:
                    item_id = i
                
            return self.show[item_id]


        

    def connect(self, itemA, termA, typeA, itemB, termB, typeB):
        self.itemA = itemA
        self.itemB = itemB
        self.termA = termA
        self.termB = termB
        self.typeA = typeA
        self.typeB = typeB
        self.item_idA = None
        self.item_idB = None

        if self.typeA == "g":
            for i in self.gate:
                if self.itemA == i:
                    self.item_idA = self.gate[i]
        elif self.typeA == "b":
            for i in self.button:
                if self.itemA == i:
                    self.item_idA = self.button[i]
        elif self.typeA == "w":
            for i in self.wire:
                if self.itemA == i:
                    self.item_idA = self.wire[i]
        elif self.typeA == "s":
            for i in self.show:
                if self.itemA == i:
                    self.item_idA = self.show[i]

        if self.typeB == "g":
            for i in self.gate:
                if self.itemB == i:
                    self.item_idB = self.gate[i]
        elif self.typeB == "b":
            for i in self.button:
                if self.itemB == i:
                    self.item_idB = self.button[i]
        elif self.typeB == "w":
            for i in self.wire:
                if self.itemB== i:
                    self.item_idB = self.wire[i]
        elif self.typeB == "s":
            for i in self.show:
                if self.itemB == i:
                    self.item_idB = self.show[i]

        print(self.item_idA)
        # self.item_idB.self.termB = self.item_idA.self.termA
        

    def list_items(self):
        pass

    def set(self, name, state):
        self.state = state
        self.name = name
        self.item_id = None
        
        for i in range(len(self.button_names)):
            if self.name == self.button_names[i]:
                self.item_id = i

        self.component = self.button[self.item_id]
        self.component.state = self.state

    def refresh(self, item, name):
        self.item = item
        self.name = name
        item_id = None
        component = None

        if self.item == "g":
            for i in range(len(self.gate_names)):
                if self.name == self.gate_names[i]:
                    item_id = i
                

            component = self.gate[item_id]
        
        elif self.item == "b":
            for i in range(len(self.button_names)):
                if self.name == self.button_names[i]:
                    item_id = i
                

            component = self.button[item_id]
        
        elif self.item == "w":
            for i in range(len(self.wire_names)):
                if self.name == self.wire_names[i]:
                    item_id = i
                

            component = self.wire[item_id]
        
        elif self.item == "s":
            for i in range(len(self.show_names)):
                if self.name == self.show_names[i]:
                    item_id = i
                
            component = self.show[item_id]

        component.run()

        



obj1 = Platform()
obj1.add("g", "gate1")
obj1.add("b", "btn1")
obj1.add("b", "btn2")
obj1.add("w", "wire1")
ax = obj1.search("b", "btn1")
print(ax.state)
obj1.set("btn1", True)
ax = obj1.search("b", "btn1")
print(ax.state)
xz = obj1.search("g", "gate1")
xz.a = True
xz.b = True
obj1.refresh("g", "gate1")
print(xz.f)

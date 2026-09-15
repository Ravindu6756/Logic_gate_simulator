import os
import subprocess


class Component:
    def __init__(self, name):
        self.name = name
        self.inputs = {}
        self.output_value = 0
        
    def evaluate(self):
        pass

class InputComponent(Component):
    def toggle(self, state):
        self.output_value = state
        print(f"Toggled {self.name} to :{state}")

class ProcessComponent(Component):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = {"nd1": 0, "nd2": 0}

    def evaluate(self):
        if self.inputs["nd1"] == 1 and self.inputs["nd2"] == 1:
            self.output_value = 0
        else:
            self.output_value = 1

class OutputComponent(Component):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = {"nd": 0}


class LogicSandbox:
    def __init__(self):
        self.memory = {}
        self.wires = []

    def add(self, name, comp_type):
        if comp_type == "IN":
            self.memory[name] = InputComponent(name)
        elif comp_type == "NAND":
            self.memory[name] = ProcessComponent(name)
        elif comp_type == "OUT":
            self.memory[name] = OutputComponent(name)
        else:
            print("\033[31mwrong component type!\033[0m")
            return
        
        print(f"Added \033[34m{comp_type}\033[0m object named '\033[33m{name}\033[0m'")

    def connect(self, x_name, y_name, target_pin):
        source_obj = self.memory[x_name]
        target_obj = self.memory[y_name]
        
        self.wires.append((source_obj, target_obj, target_pin))
        print(f"Connected wire from \033[33m{x_name}\033[0m to \033[33m{y_name}\033[0m (\033[32m{target_pin}\033[0m)")

    def refresh(self):
        for _ in range(2):
            for comp in self.memory.values():
                comp.evaluate()

            for source_obj, target_obj, target_pin in self.wires:
                target_obj.inputs[target_pin] = source_obj.output_value
                
        print("\033[32mSandbox refreshed!\033[0m")

    def output(self, name):
        comp = self.memory[name]
        if isinstance(comp, OutputComponent):
            print(f"OUTPUT SCREEN [\033[33m{name}\033[0m]: \033[35m{comp.inputs['nd']}\033[0m")
        else:
            print(f"NODE [\033[33m{name}\033[0m]: \033[35m{comp.output_value}\033[0m")

    def del_wire(self):
        print(self.wires)

    def save(self, name):
        return

sandbox = LogicSandbox()

def main():
    print("-------Logic gate simulator-------" \
    "\n Version 1.0"
    "\n\ntype 'help' for instructions!"
    "\n\n",end="")

    while True:
        command = input("<Logic gate simulator> ")
        parts = command.strip().split(" ")
        bc = parts[0].upper()

        if bc == "ADD" and len(parts) == 3:
            sandbox.add(parts[1], parts[2].upper())
        elif bc == "CON" and len(parts) == 4:
            sandbox.connect(parts[1], parts[2], parts[3])
        elif bc == "REF" and len(parts) == 1:
            sandbox.refresh()
        elif bc == "OUT" and len(parts) == 2:
            sandbox.output(parts[1])
        elif bc == "TOG" and len(parts) == 3:
            sandbox.memory[parts[1]].toggle(int(parts[2]))
        elif bc == "DEL" and len(parts) == 4:
            sandbox.del_wire(parts[1], parts[2], parts[3])
        elif bc == "SAVE" and len(parts) == 2:
            sandbox.save(parts[1])
        elif bc == "HELP" and len(parts) == 1:
            clear_screen()
            print("\n-------Instrcutions-------\n")
            with open("data/instructions.txt", 'r', encoding='utf-8') as f:
                print(f.read(), end="")
                print()
                input("\nPress any key to continue...")
                clear_screen()
                main()
        elif bc == "QUIT":
            break


    input("Press any key to continue...")

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    

clear_screen()
main()
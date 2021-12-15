from enum import Enum


# interface (Instruction and Atom)
class Instruction:
    def print(self):
        pass


class Atom:
    def print(self):
        pass


class TypeDeclaration(Enum):
    VAR = 1
    LET = 2


class TypeCycleControl(Enum):
    CONTINUE = 1
    BREAK = 2


class TypeSwitchCommand(Enum):
    CASE = 1
    DEFAULT = 2


class Func(Instruction):
    def __init__(self, name, args, locals_var=[], body=[]):
        self.__name = name
        self.__args = args
        self.__locals_var = locals_var
        self.__body = body
        self.__cnt_reference = 0

    @property
    def cnt_reference(self):
        return self.__cnt_reference

    def inc(self):
        self.__cnt_reference += 1

    def print(self):
        print(f'function {self.__name} (', end=' ')
        for cond in self.__args:
            cond.print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}')


class Declaration(Instruction):
    def __init__(self, declaration_type, body=[], var=[]):
        self.__body = body
        self.__var = var
        self.__type = declaration_type

    def print(self):
        if self.__type is TypeDeclaration.VAR:
            print('var ', end='')
        else:
            print('let ', end='')
        for atom in self.__body:
            atom.print()
        print(';')


class CycleControl(Instruction):
    def __init__(self, type_cycle_control):
        self.__type = type_cycle_control

    def print(self):
        if self.__type is TypeCycleControl.CONTINUE:
            print('continue;')
        else:
            print('break;')


class Return(Instruction):
    def __init__(self, return_value=None):
        self.return_value = return_value

    def print(self):
        print('return ', end='')
        if self.return_value is not None:
            print(self.return_value, end='')
        print(';')


class While(Instruction):
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    def print(self):
        print(f'while ({self.__conditions}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class If(Instruction):
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    def print(self):
        print(f'if ({self.__conditions}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class Else(Instruction):
    def __init__(self, body):
        self.__body = body

    def print(self):
        print('else {')
        for instr in self.__body:
            instr.print()
        print('}')


class For(Instruction):
    def __init__(self, start, conditions, step, body):
        self.__start = start
        self.__conditions = conditions
        self.__step = step
        self.__body = body

    def print(self):
        print(f'for ({self.__start};{self.__conditions};{self.__step}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class Switch(Instruction):
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    def print(self):
        print(f'switch ({self.__conditions}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class DoWhile(Instruction):
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    def print(self):
        print('do {')
        for instr in self.__body:
            instr.print()
        print(f'}} while ({self.__conditions});')


class SwitchCommand(Instruction):
    def __init__(self, switch_command_type, conditions, body):
        self.switch_command_type = switch_command_type
        self.__conditions = conditions
        self.__body = body

    def print(self):
        if self.switch_command_type is TypeSwitchCommand.CASE:
            print(f'case ({self.__conditions}):')
        else:
            print('default:')
        for instr in self.__body:
            instr.print()


class OtherInstruction(Instruction):
    def __init__(self, atoms):
        self.atoms = atoms

    def print(self):
        print(self.atoms)
        # for i in self.atoms:
        #    i.print()


class Var:
    def __init__(self, name, namespace='__main'):
        self.__name = name
        self.__namespace = namespace

    @property
    def name(self):
        return self.__name

    @property
    def namespace(self):
        return self.__namespace

    @name.setter
    def name(self, value):
        self.__name = value

    def print(self):
        print(self.__name, end=' ')

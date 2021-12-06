from enum import Enum


class TypeDeclaration(Enum):
    VAR = 1
    LET = 2


class TypeCycleControl(Enum):
    CONTINUE = 1
    BREAK = 2


class Func:
    def __init__(self, name, args, locals_var=[], body=[]):
        self.__name = name
        self.__args = args
        self.__locals_var = locals_var
        self.__body = body
        self.__cnt_reference = 0

    @property
    def name(self):
        return self.__name

    @property
    def args(self):
        return self.__args

    @property
    def locals_var(self):
        return self.__locals_var

    @property
    def body(self):
        return self.__body

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


class Declaration:
    def __init__(self, declaration_type, body=[], var=[]):
        self.__body = body
        self.__var = var
        self.__type = declaration_type

    @property
    def body(self):
        return self.__body

    @property
    def var(self):
        return self.__var

    def print(self):
        if self.__type is TypeDeclaration.VAR:
            print('var ', end='')
        else:
            print('let ', end='')
        for atom in self.__body:
            atom.print()
        print(';')


class CycleControl:
    def __init__(self, type_cycle_control):
        self.__type = type_cycle_control

    def print(self):
        if self.__type is TypeCycleControl.CONTINUE:
            print('continue;')
        else:
            print('break;')


class Return:
    def __init__(self):
        pass

    def print(self):
        print('return ;')


class While:
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    @property
    def conditions(self):
        return self.__conditions

    @property
    def body(self):
        return self.__body

    def print(self):
        print(f'while ({self.__conditions}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class If:
    def __init__(self, conditions, body):
        self.__conditions = conditions
        self.__body = body

    @property
    def conditions(self):
        return self.__conditions

    @property
    def body(self):
        return self.__body

    def print(self):
        print(f'if ({self.__conditions}){{')
        for instr in self.__body:
            instr.print()
        print('}')


class Else:
    def __init__(self, body):
        self.__body = body

    @property
    def body(self):
        return self.__body

    def print(self):
        print('else {')
        for instr in self.__body:
            instr.print()
        print('}')


class For:
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

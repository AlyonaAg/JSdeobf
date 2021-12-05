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


class CycleControl:
    def __init__(self, type_cycle_control):
        self.__type = type_cycle_control


class Return:
    def __init__(self):
        pass


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

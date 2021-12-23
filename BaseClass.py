from enum import Enum


# interface (Instruction and Atom)
class Instruction:
    def print(self):
        pass


class Atom:
    def print(self):
        pass


# base enum
class TypeDeclaration(Enum):
    VAR = 1
    LET = 2


class TypeCycleControl(Enum):
    CONTINUE = 1
    BREAK = 2


class TypeSwitchCommand(Enum):
    CASE = 1
    DEFAULT = 2


class TypeBool(Enum):
    TRUE = 1
    FALSE = 2


class TypeArithmeticOperation(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    DEG = 6
    INC = 7
    DEC = 8
    ASSIGN = 9
    ADD_ASSIGN = 10
    SUB_ASSIGN = 11
    MUL_ASSIGN = 12
    DIV_ASSIGN = 13
    DEG_ASSIGN = 14
    MOD_ASSIGN = 15


class TypeBinaryOperation(Enum):
    LEFT_SHIFT = 1
    RIGHT_SHIFT = 2
    RIGHT_SHIFT_FILL = 3  # >>>
    NOT = 4  # ~
    AND = 5
    OR = 6
    XOR = 7
    LEFT_SHIFT_ASSIGN = 8
    RIGHT_SHIFT_ASSIGN = 9
    RIGHT_SHIFT_FILL_ASSIGN = 10  # >>>=
    NOT_ASSIGN = 11
    AND_ASSIGN = 12
    OR_ASSIGN = 13
    XOR_ASSIGN = 14


class TypeLogicalOperation(Enum):
    EQ = 1  # ==
    NE = 2  # !=
    LESS = 3  # <
    GREATER = 4  # >
    LESS_EQ = 5  # <=
    GREATER_EQ = 6  # >=
    AND = 7
    OR = 8
    AND_ASSIGN = 9
    OR_ASSIGN = 10
    NULLISH = 11  # ??
    NULLISH_ASSIGN = 12  # ??=
    NOT = 13
    TRIPLE_EQ = 14  # ===
    TRIPLE_NE = 15  # !==
    SHORT_IF = 16  # ?
    SHORT_COND = 17  # :


# base instruction
class Func(Instruction):
    def __init__(self, name, args=[], body=[]):
        self.__name = name
        self.__args = args
        self.__body = body
        self.__cnt_reference = 0

    @property
    def cnt_reference(self):
        return self.__cnt_reference

    @property
    def body(self):
        return self.__body

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    def inc(self):
        self.__cnt_reference += 1

    def print(self):
        print(f'function {self.__name}(', end='')
        if len(self.__args):
            for cond in self.__args[:-1]:
                cond.print()
                print(end=', ')
            self.__args[-1].print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}\n')


class Declaration(Instruction):
    def __init__(self, declaration_type, body=[], var=[]):
        self.__body = body
        self.__var = var
        self.__type = declaration_type

    @property
    def body(self):
        return self.__body

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
        self.__return_value = return_value

    @property
    def return_value(self):
        return self.__return_value

    def print(self):
        print('return ', end='')
        for atom in self.__return_value:
            atom.print()
        print(';')


class While(Instruction):
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
        print(f'while (', end='')
        for atom in self.__conditions:
            atom.print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}')


class If(Instruction):
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
        print(f'if (', end='')
        for atom in self.__conditions:
            atom.print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}')


class Else(Instruction):
    def __init__(self, body):
        self.__body = body

    @property
    def body(self):
        return self.__body

    def print(self):
        print('else ')
        if len(self.__body) > 1:
            print('{')
        for instr in self.__body:
            instr.print()
        if len(self.__body) > 1:
            print('}')


class For(Instruction):
    def __init__(self, init, conditions, step, body):
        self.__init = init
        self.__conditions = conditions
        self.__step = step
        self.__body = body

    @property
    def init(self):
        return self.__init

    @property
    def conditions(self):
        return self.__conditions

    @property
    def step(self):
        return self.__step

    @property
    def body(self):
        return self.__body

    def print(self):
        print(f'for (', end='')
        for atom in self.__init:
            atom.print()
        print('; ', end='')
        for atom in self.__conditions:
            atom.print()
        print('; ', end='')
        for atom in self.__step:
            atom.print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}')


class Switch(Instruction):
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
        print(f'switch (', end='')
        for atom in self.__conditions:
            atom.print()
        print('){')
        for instr in self.__body:
            instr.print()
        print('}')


class DoWhile(Instruction):
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
        print('do {')
        for instr in self.__body:
            instr.print()
        print('} while (', end='')
        for atom in self.__conditions:
            atom.print()
        print(');')


class SwitchCommand(Instruction):
    def __init__(self, switch_command_type, conditions, body):
        self.switch_command_type = switch_command_type
        self.__conditions = conditions
        self.__body = body

    @property
    def conditions(self):
        return self.__conditions

    @property
    def body(self):
        return self.__body

    def print(self):
        if self.switch_command_type is TypeSwitchCommand.CASE:
            print('case (', end='')
            for atom in self.__conditions:
                atom.print()
            print('):')
        else:
            print('default:')
        for instr in self.__body:
            instr.print()


class OtherInstruction(Instruction):
    def __init__(self, atoms):
        self.__atoms = atoms

    @property
    def atoms(self):
        return self.__atoms

    def print(self):
        if len(self.__atoms):
            for i in self.__atoms:
                i.print()
        else:
            print(self.__atoms, end='')
        print(';')


# base atom
class Var(Atom):
    def __init__(self, name, namespace='__main'):
        self.__name = name
        self.__namespace = namespace

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def namespace(self):
        return self.__namespace

    @name.setter
    def name(self, value):
        self.__name = value

    def print(self):
        print(self.__name, end='')


class Number(Atom):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def print(self):
        print(self.__value, end='')


class String(Atom):
    def __init__(self, value):
        self.__value = value

    def print(self):
        print(self.__value, end='')


class Array(Atom):
    def __init__(self, atoms):
        self.__atoms = atoms

    @property
    def atoms(self):
        return self.__atoms

    def print(self):
        print('[', end='')
        for atom in self.__atoms:
            atom.print()
        print(']', end='')


class CallFunc(Atom):
    def __init__(self, func, args):
        self.__func = func
        self.__args = args

    @property
    def args(self):
        return self.__args

    def print(self):
        print(f'{self.__func.name}(', end='')
        for atom in self.args:
            atom.print()
        print(')', end='')


class Bool(Atom):
    def __init__(self, bool_type):
        self.__bool_type = bool_type

    def print(self):
        if self.__bool_type == TypeBool.TRUE:
            print('true', end='')
        else:
            print('false', end='')


class ArithmeticOperation(Atom):
    def __init__(self, operation_type):
        self.__operation_type = operation_type

    @property
    def operation_type(self):
        return self.__operation_type

    def print(self):
        if self.__operation_type == TypeArithmeticOperation.ADD:
            print(' + ', end='')
        elif self.__operation_type == TypeArithmeticOperation.SUB:
            print(' - ', end='')
        elif self.__operation_type == TypeArithmeticOperation.MUL:
            print(' * ', end='')
        elif self.__operation_type == TypeArithmeticOperation.DIV:
            print(' / ', end='')
        elif self.__operation_type == TypeArithmeticOperation.MOD:
            print(' % ', end='')
        elif self.__operation_type == TypeArithmeticOperation.DEG:
            print(' ** ', end='')
        elif self.__operation_type == TypeArithmeticOperation.INC:
            print('++ ', end='')
        elif self.__operation_type == TypeArithmeticOperation.DEC:
            print('-- ', end='')
        elif self.__operation_type == TypeArithmeticOperation.ASSIGN:
            print(' = ', end='')
        elif self.__operation_type == TypeArithmeticOperation.ADD_ASSIGN:
            print(' += ', end='')
        elif self.__operation_type == TypeArithmeticOperation.SUB_ASSIGN:
            print(' -= ', end='')
        elif self.__operation_type == TypeArithmeticOperation.MUL_ASSIGN:
            print(' *= ', end='')
        elif self.__operation_type == TypeArithmeticOperation.DIV_ASSIGN:
            print(' /= ', end='')
        elif self.__operation_type == TypeArithmeticOperation.DEG_ASSIGN:
            print(' **= ', end='')
        elif self.__operation_type == TypeArithmeticOperation.MOD_ASSIGN:
            print(' %= ', end='')


class BinaryOperation(Atom):
    def __init__(self, operation_type):
        self.operation_type = operation_type

    def print(self):
        if self.operation_type == TypeBinaryOperation.LEFT_SHIFT:
            print(' << ', end='')
        elif self.operation_type == TypeBinaryOperation.RIGHT_SHIFT:
            print(' >> ', end='')
        elif self.operation_type == TypeBinaryOperation.RIGHT_SHIFT_FILL:
            print(' >>> ', end='')
        elif self.operation_type == TypeBinaryOperation.NOT:
            print(' ~ ', end='')
        elif self.operation_type == TypeBinaryOperation.AND:
            print(' & ', end='')
        elif self.operation_type == TypeBinaryOperation.OR:
            print(' | ', end='')
        elif self.operation_type == TypeBinaryOperation.XOR:
            print(' ^ ', end='')
        elif self.operation_type == TypeBinaryOperation.LEFT_SHIFT_ASSIGN:
            print(' >>= ', end='')
        elif self.operation_type == TypeBinaryOperation.RIGHT_SHIFT_ASSIGN:
            print(' <<= ', end='')
        elif self.operation_type == TypeBinaryOperation.RIGHT_SHIFT_FILL_ASSIGN:
            print(' >>>= ', end='')
        elif self.operation_type == TypeBinaryOperation.NOT_ASSIGN:
            print(' ~= ', end='')
        elif self.operation_type == TypeBinaryOperation.AND_ASSIGN:
            print(' &= ', end='')
        elif self.operation_type == TypeBinaryOperation.OR_ASSIGN:
            print(' |= ', end='')
        elif self.operation_type == TypeBinaryOperation.XOR_ASSIGN:
            print(' ^= ', end='')


class LogicalOperation(Atom):
    def __init__(self, operation_type):
        self.operation_type = operation_type

    def print(self):
        if self.operation_type == TypeLogicalOperation.EQ:
            print(' == ', end='')
        elif self.operation_type == TypeLogicalOperation.NE:
            print(' != ', end='')
        elif self.operation_type == TypeLogicalOperation.LESS:
            print(' < ', end='')
        elif self.operation_type == TypeLogicalOperation.GREATER:
            print(' > ', end='')
        elif self.operation_type == TypeLogicalOperation.LESS_EQ:
            print(' <= ', end='')
        elif self.operation_type == TypeLogicalOperation.GREATER_EQ:
            print(' >= ', end='')
        elif self.operation_type == TypeLogicalOperation.AND:
            print(' && ', end='')
        elif self.operation_type == TypeLogicalOperation.OR:
            print(' || ', end='')
        elif self.operation_type == TypeLogicalOperation.AND_ASSIGN:
            print(' &&= ', end='')
        elif self.operation_type == TypeLogicalOperation.OR_ASSIGN:
            print(' ||= ', end='')
        elif self.operation_type == TypeLogicalOperation.NULLISH:
            print(' ?? ', end='')
        elif self.operation_type == TypeLogicalOperation.NULLISH_ASSIGN:
            print(' ??= ', end='')
        elif self.operation_type == TypeLogicalOperation.NOT:
            print(' ! ', end='')
        elif self.operation_type == TypeLogicalOperation.TRIPLE_EQ:
            print(' === ', end='')
        elif self.operation_type == TypeLogicalOperation.TRIPLE_NE:
            print(' !== ', end='')
        elif self.operation_type == TypeLogicalOperation.SHORT_IF:
            print(' ? ', end='')
        elif self.operation_type == TypeLogicalOperation.SHORT_COND:
            print(' : ', end='')


class Border(Atom):
    def __init__(self):
        pass

    def print(self):
        print(', ', end='')


class Brackets(Atom):
    def __init__(self, atoms):
        self.__atoms = atoms

    @property
    def atoms(self):
        return self.__atoms

    def print(self):
        print('(', end='')
        for atom in self.__atoms:
            atom.print()
        print(')', end='')


class New(Atom):
    def __init__(self):
        pass

    @staticmethod
    def print():
        print('new ', end='')


class InstanceClass(Atom):
    def __init__(self, instance, field):
        self.__instance = instance
        self.__field = field

    @property
    def instance(self):
        return self.__instance

    @property
    def field(self):
        return self.__field

    def print(self):
        self.__instance.print()
        print('.', end='')
        self.__field.print()

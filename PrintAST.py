from enum import Enum
import BaseClass
import AST


# TODO: add 'const'

class PrintAST:
    class __TypeElem(Enum):
        INSTR = 1
        ATOMS = 2

    __shift = 0

    def __init__(self, ast):
        self.__ast = ast

    def print(self):
        self.__printDFS(self.__ast, PrintAST.__TypeElem.INSTR)

    def __printDFS(self, elem, type_elem):
        if type_elem is PrintAST.__TypeElem.INSTR:
            self.__printShift()
            if isinstance(elem, AST.AST):
                for instr in elem.tree:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)

            elif isinstance(elem, BaseClass.For):
                print('for (', end='')
                self.__printDFS(elem.init, PrintAST.__TypeElem.ATOMS)
                print('; ', end='')
                self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                print('; ', end='')
                self.__printDFS(elem.step, PrintAST.__TypeElem.ATOMS)
                print(')')
                if len(elem.body) > 1:
                    self.__printShift()
                    print('{')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                if len(elem.body) > 1:
                    self.__printShift()
                    print('}')

            elif isinstance(elem, BaseClass.While):
                print('while (', end='')
                self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                print(')')
                if len(elem.body) > 1:
                    self.__printShift()
                    print('{')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                if len(elem.body) > 1:
                    self.__printShift()
                    print('}')

            elif isinstance(elem, BaseClass.DoWhile):
                print('{')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                print('} (', end='')
                self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                print(')')

            elif isinstance(elem, BaseClass.SwitchCommand):
                if elem.switch_command_type is BaseClass.TypeSwitchCommand.CASE:
                    print('case (', end='')
                    self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                    print('):')
                else:
                    print('default:')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()

            elif isinstance(elem, BaseClass.If):
                print('if (', end='')
                self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                print(')')
                if len(elem.body) > 1:
                    self.__printShift()
                    print('{')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                if len(elem.body) > 1:
                    self.__printShift()
                    print('}')

            elif isinstance(elem, BaseClass.Switch):
                print('switch (', end='')
                self.__printDFS(elem.conditions, PrintAST.__TypeElem.ATOMS)
                print('){')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                self.__printShift()
                print('}')

            elif isinstance(elem, BaseClass.Else):
                print('else')
                if len(elem.body) > 1:
                    print('{')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                if len(elem.body) > 1:
                    print('}')

            elif isinstance(elem, BaseClass.Func):
                print('function ', end='')
                if elem.name is not None:
                    print(f'{elem.name}', end='')
                print('(', end='')
                if len(elem.args):
                    for arg in elem.args[:-1]:
                        self.__printDFS([arg], PrintAST.__TypeElem.ATOMS)
                        print(end=', ')
                    self.__printDFS([elem.args[-1]], PrintAST.__TypeElem.ATOMS)
                print('){')
                self.__incShift()
                for instr in elem.body:
                    self.__printDFS(instr, PrintAST.__TypeElem.INSTR)
                self.__decShift()
                print('}', end='')
                if elem.name is not None:
                    print('\n')

            elif isinstance(elem, BaseClass.Declaration):
                if elem.type is BaseClass.TypeDeclaration.VAR:
                    print('var ', end='')
                else:
                    print('let ', end='')
                self.__printDFS(elem.body, PrintAST.__TypeElem.ATOMS)
                print(';')

            elif isinstance(elem, BaseClass.Return):
                print('return', end='')
                if len(elem.return_value):
                    print(' ', end='')
                    self.__printDFS(elem.return_value, PrintAST.__TypeElem.ATOMS)
                print(';')

            elif isinstance(elem, BaseClass.OtherInstruction):
                self.__printDFS(elem.atoms, PrintAST.__TypeElem.ATOMS)
                print(';')

            elif isinstance(elem, BaseClass.CycleControl):
                if elem.type is BaseClass.TypeCycleControl.CONTINUE:
                    print('continue;')
                else:
                    print('break;')

        elif type_elem is PrintAST.__TypeElem.ATOMS:
            for atom in elem:
                if isinstance(atom, BaseClass.Func):
                    self.__printDFS(atom, PrintAST.__TypeElem.INSTR)

                elif isinstance(atom, BaseClass.Var):
                    print(atom.name, end='')

                elif isinstance(atom, BaseClass.Number):
                    print(atom.value, end='')

                elif isinstance(atom, BaseClass.String):
                    print(atom.value, end='')

                elif isinstance(atom, BaseClass.Border):
                    print(', ', end='')

                elif isinstance(atom, BaseClass.New):
                    print('new ', end='')

                elif isinstance(atom, BaseClass.Const):
                    print('const ', end='')

                elif isinstance(atom, BaseClass.Infinity):
                    print('Infinity', end='')

                elif isinstance(atom, BaseClass.Bool):
                    if atom.bool_type == BaseClass.TypeBool.TRUE:
                        print('true', end='')
                    else:
                        print('false', end='')

                elif isinstance(atom, BaseClass.Array):
                    print('[', end='')
                    self.__printDFS(atom.atoms, PrintAST.__TypeElem.ATOMS)
                    print(']', end='')

                elif isinstance(atom, BaseClass.CallFunc):
                    print(f'{atom.func.name}(', end='')
                    self.__printDFS(atom.args, PrintAST.__TypeElem.ATOMS)
                    print(')', end='')

                elif isinstance(atom, BaseClass.ArithmeticOperation):
                    if atom.operation_type == BaseClass.TypeArithmeticOperation.ADD:
                        print(' + ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.SUB:
                        print(' - ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.MUL:
                        print(' * ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.DIV:
                        print(' / ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.MOD:
                        print(' % ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.DEG:
                        print(' ** ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.INC:
                        print('++ ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.DEC:
                        print('-- ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.ASSIGN:
                        print(' = ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.ADD_ASSIGN:
                        print(' += ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.SUB_ASSIGN:
                        print(' -= ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.MUL_ASSIGN:
                        print(' *= ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.DIV_ASSIGN:
                        print(' /= ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.DEG_ASSIGN:
                        print(' **= ', end='')
                    elif atom.operation_type == BaseClass.TypeArithmeticOperation.MOD_ASSIGN:
                        print(' %= ', end='')

                elif isinstance(atom, BaseClass.BinaryOperation):
                    if atom.operation_type == BaseClass.TypeBinaryOperation.LEFT_SHIFT:
                        print(' << ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.RIGHT_SHIFT:
                        print(' >> ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.RIGHT_SHIFT_FILL:
                        print(' >>> ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.NOT:
                        print(' ~ ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.AND:
                        print(' & ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.OR:
                        print(' | ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.XOR:
                        print(' ^ ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.LEFT_SHIFT_ASSIGN:
                        print(' >>= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.RIGHT_SHIFT_ASSIGN:
                        print(' <<= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.RIGHT_SHIFT_FILL_ASSIGN:
                        print(' >>>= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.NOT_ASSIGN:
                        print(' ~= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.AND_ASSIGN:
                        print(' &= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.OR_ASSIGN:
                        print(' |= ', end='')
                    elif atom.operation_type == BaseClass.TypeBinaryOperation.XOR_ASSIGN:
                        print(' ^= ', end='')

                elif isinstance(atom, BaseClass.LogicalOperation):
                    if atom.operation_type == BaseClass.TypeLogicalOperation.EQ:
                        print(' == ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.NE:
                        print(' != ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.LESS:
                        print(' < ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.GREATER:
                        print(' > ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.LESS_EQ:
                        print(' <= ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.GREATER_EQ:
                        print(' >= ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.AND:
                        print(' && ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.OR:
                        print(' || ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.AND_ASSIGN:
                        print(' &&= ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.OR_ASSIGN:
                        print(' ||= ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.NULLISH:
                        print(' ?? ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.NULLISH_ASSIGN:
                        print(' ??= ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.NOT:
                        print('!', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.TRIPLE_EQ:
                        print(' === ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.TRIPLE_NE:
                        print(' !== ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.SHORT_IF:
                        print(' ? ', end='')
                    elif atom.operation_type == BaseClass.TypeLogicalOperation.SHORT_COND:
                        print(' : ', end='')

                elif isinstance(atom, BaseClass.Brackets):
                    print('(', end='')
                    self.__printDFS(atom.atoms, PrintAST.__TypeElem.ATOMS)
                    print(')', end='')

                elif isinstance(atom, BaseClass.InstanceClass):
                    self.__printDFS([atom.instance], PrintAST.__TypeElem.ATOMS)
                    print('.', end='')
                    self.__printDFS([atom.field], PrintAST.__TypeElem.ATOMS)

    @staticmethod
    def __printShift():
        print('\t' * PrintAST.__shift, end='')

    @staticmethod
    def __incShift():
        PrintAST.__shift += 1

    @staticmethod
    def __decShift():
        PrintAST.__shift -= 1

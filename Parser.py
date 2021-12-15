import re
import Repository
import BaseClass


class Parser:
    __namespace = '__main'

    def parserAST(self, script):
        instrAST = []
        i = 0
        while i < len(script):
            instr, shift = self.__getInstruction(script[i:])

            if instr is not None:
                instrAST.append(instr)
                i += shift - 1
            i += 1
        return instrAST

    def __parserFunc(self, script):
        start = re.search(r'(\{)', script).start()
        finish = start + self.__searchForBoundaries(script[start + 1:], '[{]', '[}]') + 1
        declaration = re.match(r'function ([a-zA-Z_]\w+)\((.*?)\)', script)

        name = declaration.group(1)
        Parser.__namespace = name

        args = [BaseClass.Var(arg, Parser.__namespace)
                for arg in declaration.group(2).split(sep=',')]
        locals_var = args

        body = []
        i = start
        while i < finish:
            instr, shift = self.__getInstruction(script[i:])
            if instr is not None:
                i += shift - 1
                body.append(instr)
            i += 1

        repo = Repository.Repository()
        repo.append_var(args)

        Parser.__namespace = "__main"

        func = BaseClass.Func(name, args, locals_var, body)
        repo.append_func(func)
        return func, finish

    def __parserDeclaration(self, script):
        declaration_type = BaseClass.TypeDeclaration.VAR if script[:3] == 'var' else BaseClass.TypeDeclaration.LET
        finish = self.__searchEndOfCommand(script) + 1

        body = []
        var = []
        # TODO: parser atom
        return BaseClass.Declaration(declaration_type, body, var), finish

    def __parserCycleControl(self, script):
        cycle_control_type = BaseClass.TypeCycleControl.CONTINUE if script.startswith(
            'continue') else BaseClass.TypeCycleControl.BREAK
        finish = self.__searchEndOfCommand(script) + 1

        # print(script[:finish], cycle_control_type)
        return BaseClass.CycleControl(cycle_control_type), finish

    def __parserReturn(self, script):
        start_return_value = len('return')
        finish_return_value = self.__searchEndOfCommand(script) + 1
        # TODO: возвращаемое значение

        return_value = []
        return BaseClass.Return(return_value), finish_return_value

    def __parserWhile(self, script):
        # TODO: create conditions
        start_conditions = re.search(r'(\()', script).start() + 1
        finish_conditions = start_conditions + self.__searchForBoundaries(script[start_conditions:], '[(]', '[)]')
        condition = []
        body, i = self.__getBody(script, finish_conditions)
        return BaseClass.While(condition, body), i

    def __parserIf(self, script):
        # TODO: условие
        start_conditions = re.search(r'(\()', script).start() + 1
        finish_conditions = start_conditions + self.__searchForBoundaries(script[start_conditions:], '[(]', '[)]')
        condition = []
        body, i = self.__getBody(script, finish_conditions)
        return BaseClass.If(condition, body), i

    def __parserElse(self, script):
        start_else = len('else')
        body, i = self.__getBody(script, start_else)
        return BaseClass.Else(body), i

    def __parserFor(self, script):
        start_common_cond = re.search(r'(\()', script).start() + 1
        end_common_cond = start_common_cond + self.__searchForBoundaries(script[start_common_cond:], '[(]', '[)]')

        finish_start = start_common_cond + re.search(r';', script[start_common_cond:end_common_cond]).start() + 1
        finish_cond = finish_start + re.search(r';', script[finish_start:end_common_cond]).start() + 1
        finish_step = end_common_cond

        body, i = self.__getBody(script, end_common_cond)
        return BaseClass.For([], [], [], body), i

    def __parserSwitch(self, script):
        # TODO: create conditions
        start_conditions = re.search(r'(\()', script).start() + 1
        finish_conditions = start_conditions + self.__searchForBoundaries(script[start_conditions:], '[(]', '[)]')
        condition, body = [], []

        start_body = re.search(r'(\{)', script[finish_conditions:]).start() + finish_conditions
        finish_body = start_body + self.__searchForBoundaries(script[start_body + 1:], '[{]', '[}]') + 1

        i = start_body
        while i < finish_body:
            instr, shift = self.__getSwitchCommand(script[i:finish_body])
            if instr is not None:
                i += shift - 1
                body.append(instr)
            i += 1

        return BaseClass.Switch(condition, body), i

    def __parserDoWhile(self, script):
        start_do = len('do')
        body, i = self.__getBody(script, start_do)

        condition = []
        start_conditions = i + re.search(r'(\()', script[i:]).start() + 1
        finish_conditions = start_conditions + self.__searchForBoundaries(script[start_conditions:], '[(]', '[)]')

        return BaseClass.DoWhile(condition, body), finish_conditions

    def __parserOtherInstruction(self, script):
        finish_instruction = self.__searchEndOfCommand(script)
        atoms = self.__getAtomList(script[:finish_instruction])
        return BaseClass.OtherInstruction(atoms), finish_instruction

    @staticmethod
    def __getNumber(script):
        if script.startswith('0x'):
            value = int(script[:-1], base=16)
        elif script.startswith('0o'):
            value = int(script[:-1], base=8)
        elif script.startswith('0b'):
            value = int(script[:-1], base=2)
        else:
            value = int(script[:-1])
        return BaseClass.Number(value), len(script) - 1

    @staticmethod
    def __getString(script):
        return BaseClass.String(script), len(script)

    def __getArray(self, script):
        start_array = re.search(r'(\[)', script).start() + 1
        finish_array = start_array + self.__searchForBoundaries(script[start_array:], r'\[', r'\]')
        atoms = self.__getAtomList(script[start_array:finish_array - 1])
        return BaseClass.Array(atoms), finish_array - 1

    def __getCallFunc(self, script):
        start_args = re.search(r'(\()', script).start() + 1
        finish_args = start_args + self.__searchForBoundaries(script[start_args:], '[(]', '[)]')

        name = script[:start_args - 1]
        args = self.__getAtomList(script[start_args:finish_args - 1])

        repo = Repository.Repository()
        repo.inc_used(name)

        return BaseClass.CallFunc(name, args), finish_args

    def __getSwitchCommand(self, script):
        # TODO: create conditions

        if re.match(r'case[\W]', script) is not None:
            command_type = BaseClass.TypeSwitchCommand.CASE
        elif re.match(r'default[\W]', script) is not None:
            command_type = BaseClass.TypeSwitchCommand.DEFAULT
        else:
            return None, 0

        condition = []
        start_body = re.search(r':', script).start() + 1

        i, body = start_body, []
        while (i - start_body) < len(script):
            if re.match(r'case[\W]', script[i:]) is not None or\
                    re.match(r'default[\W]', script[i:]) is not None:
                i -= 1
                break
            instr, shift = self.__getInstruction(script[i:])
            if instr is not None:
                i += shift - 1
                body.append(instr)
            i += 1

        return BaseClass.SwitchCommand(command_type, condition, body), i

    def __getInstruction(self, script):
        if re.match(r'function[\W]', script) is not None:
            return self.__parserFunc(script)
        elif re.match(r'var ', script) is not None:
            return self.__parserDeclaration(script)
        elif re.match(r'let ', script) is not None:
            return self.__parserDeclaration(script)
        elif re.match(r'break[\W]', script) is not None:
            return self.__parserCycleControl(script)
        elif re.match(r'continue[\W]', script) is not None:
            return self.__parserCycleControl(script)
        elif re.match(r'return[\W]', script) is not None:
            return self.__parserReturn(script)
        elif re.match(r'while[\W]', script) is not None:
            return self.__parserWhile(script)
        elif re.match(r'if[\W]', script) is not None:
            return self.__parserIf(script)
        elif re.match(r'else[\W]', script) is not None:
            return self.__parserElse(script)
        elif re.match(r'for[\W]', script) is not None:
            return self.__parserFor(script)
        elif re.match(r'switch[\W]', script) is not None:
            return self.__parserSwitch(script)
        elif re.match(r'do[\W]', script) is not None:
            return self.__parserDoWhile(script)
        elif re.match(r'[\w]', script) is not None:
            return self.__parserOtherInstruction(script)
        return None, 0

    def __getAtom(self, script):
        if (match := re.match(r'((0o[0-7]+)|(0x[\dabcdef]+)|(0b[0-1]+)|\d+)[^\w\d]', script)) is not None:
            return self.__getNumber(match.group())
        if (match := re.match(r'(\'(\\\'|.)*?\'|\"(\\\"|.)*?\")', script)) is not None:
            return self.__getString(match.group())
        if re.match(r'\[', script) is not None:
            return self.__getArray(script)
        if re.match(r'((\w+\.)*\w+\s*\()', script) is not None:
            return self.__getCallFunc(script)
        return None, 0

    def __getBody(self, script, start_position):
        body = []
        # checking count of instruction (one or { })
        if re.match(r'\s*{', script[start_position:]) is not None:
            start_body = re.search(r'(\{)', script[start_position:]).start() + start_position
            finish_body = start_body + self.__searchForBoundaries(script[start_body + 1:], '[{]', '[}]') + 1

            i = start_body
            while i < finish_body:
                instr, shift = self.__getInstruction(script[i:])
                if instr is not None:
                    i += shift - 1
                    body.append(instr)
                i += 1
        else:
            i, count_instruction = start_position, 0
            while not count_instruction:
                instr, shift = self.__getInstruction(script[i:])
                if instr is not None:
                    i += shift - 1
                    body.append(instr)
                    count_instruction += 1
                i += 1

        return body, i

    def __getAtomList(self, script):
        i = 0
        atoms = []
        while i < len(script):
            atom, shift = self.__getAtom(script[i:])
            if atom is not None:
                i += shift - 1
                atoms.append(atom)
            i += 1

        return atoms

    @staticmethod
    def __searchForBoundaries(script, start_bound, finish_bound):
        cnt_bracket, shift = 1, 0
        while shift < len(script) and cnt_bracket:
            if (match := re.match(r'(\'(\\\'|.)*?\'|\"(\\\"|.)*?\")|(' + start_bound + ')|(' + finish_bound + ')',
                                  script[shift:])) is not None:
                if match.group() == start_bound[1]:
                    cnt_bracket += 1
                elif match.group() == finish_bound[1]:
                    cnt_bracket -= 1
                else:
                    shift += match.end() - 1
            shift += 1
        return shift

    @staticmethod
    def __searchEndOfCommand(script):
        shift = 0
        while shift < len(script):
            if (match := re.match(r'(\'(\\\'|.)*?\'|\"(\\\"|.)*?\")|(;)', script[shift:])) is not None:
                if match.group() == ';':
                    return shift
                else:
                    shift += match.end() - 1
            shift += 1
        raise ValueError('[search_end_of_command]: symbol \';\' was not found')

# TODO: atom = var, class., operation (+,-, and etc.), (), condition (>, ==, < and etc.),!, true, false

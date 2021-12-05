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
        finish = start + self.__searchForBoundaries(script[start + 1:], ['{', '}']) + 1
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
        return BaseClass.Func(name, args, locals_var, body), finish

    def __parserDeclaration(self, script):
        declaration_type = BaseClass.TypeDeclaration.VAR if script[:3] == 'var' else BaseClass.TypeDeclaration.LET
        finish = self.__searchEndOfCommand(script) + 1

        body = []
        var = []
        # TODO: parser atom
        # print(script[:finish], declaration_type)
        return BaseClass.Declaration(declaration_type, body, var), finish

    def __parserCycleControl(self, script):
        cycle_control_type = BaseClass.TypeCycleControl.CONTINUE if script.startswith('continue') else BaseClass.TypeCycleControl.BREAK
        finish = self.__searchEndOfCommand(script) + 1

        # print(script[:finish], cycle_control_type)
        return BaseClass.CycleControl(cycle_control_type), finish

    def __parserReturn(self, script):
        finish = self.__searchEndOfCommand(script) + 1

        # print(script[:finish])
        return BaseClass.Return(), finish

    def __parserWhile(self, script):
        start_conditions = re.search(r'(\()', script).start()
        finish_conditions = start_conditions + self.__searchForBoundaries(script[start_conditions + 1:],
                                                                          ['(', ')']) + 1
        print('WHILE CONDITIONS:', script[start_conditions:])
        return None, 0

    def __getInstruction(self, script):
        # TODO: учитывать символ, идущий после инструкций (вдруг имена называются с этих слов)
        #  сдвиг вроде не должен измениться

        if re.match(r'function', script) is not None:
            return self.__parserFunc(script)
        elif re.match(r'var ', script) is not None:
            return self.__parserDeclaration(script)
        elif re.match(r'let ', script) is not None:
            return self.__parserDeclaration(script)
        elif re.match(r'break', script) is not None:
            return self.__parserCycleControl(script)
        elif re.match(r'continue', script) is not None:
            return self.__parserCycleControl(script)
        elif re.match(r'return', script) is not None:
            return self.__parserReturn(script)
        elif re.match(r'while', script) is not None:
            return self.__parserWhile(script)
        return None, 0

    def __getAtom(self, script):
        pass

    @staticmethod
    def __searchForBoundaries(script, bracket):
        cnt_bracket, shift = 1, 0
        while shift < len(script) and cnt_bracket:
            if (match := re.match(r'(\'(\\\'|.)*?\'|\"(\\\"|.)*?\")|(' + bracket[0] + ')|(' + bracket[1] + ')',
                                  script[shift:])) is not None:
                if match.group() == bracket[0]:
                    cnt_bracket += 1
                elif match.group() == bracket[1]:
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

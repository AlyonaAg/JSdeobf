import BaseClass
import Repository


class ProcessingAST:
    def __init__(self, ast):
        self.__ast = ast

    @property
    def ast(self):
        return self.__ast

    def processing(self):
        self.__deleteUnusedFunction()
        self.__rename()

    def __deleteUnusedFunction(self):
        del_instr = []
        for instr in self.__ast.tree:
            if isinstance(instr, BaseClass.Func) and not instr.cnt_reference:
                del_instr.append(instr)
        for instr in del_instr:
            self.__ast.tree.remove(instr)

    def __rename(self):
        repo = Repository.Repository
        list_vars = repo.get_vars()
        for var, i in enumerate(list_vars):
            var.name = 'var' + str(i)

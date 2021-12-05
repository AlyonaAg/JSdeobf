import BaseClass
import Parser
import Repository


class AST:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.__script = f.read()
        self.__Tree = []

    def createAST(self):
        parser = Parser.Parser()
        self.__Tree = parser.parserAST(self.__script)

        print('------------ AST ------------')
        print(self.__Tree)
        for AST in self.__Tree:
            if isinstance(AST, BaseClass.Func):
                print(AST.name, ': ', AST.body)
            elif isinstance(AST, BaseClass.Declaration):
                print(AST.body)

        print('------------ USED VAR ------------')
        repo = Repository.Repository()
        for var in repo.get_vars():
            print(var.name, var.namespace)

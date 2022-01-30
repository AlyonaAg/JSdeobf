import Parser


class AST:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.__script = f.read()
        self.__Tree = []

    @property
    def tree(self):
        return self.__Tree

    def createAST(self):
        parser = Parser.Parser()
        self.__Tree = parser.parserAST(self.__script)

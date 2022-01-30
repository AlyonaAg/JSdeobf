from AST import AST
from ProcessingAST import ProcessingAST
from PrintAST import PrintAST

if __name__ == '__main__':
    ast = AST('1.js')
    ast.createAST()
    processing = ProcessingAST(ast)
    processing.processing()

    print_ast = PrintAST(ast)
    print_ast.print()

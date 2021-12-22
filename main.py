from AST import AST
from ProcessingAST import ProcessingAST

if __name__ == '__main__':
    ast = AST('obf_test.js')
    ast.createAST()
    # ast.print()
    processing = ProcessingAST(ast)
    processing.processing()

    ast.print()

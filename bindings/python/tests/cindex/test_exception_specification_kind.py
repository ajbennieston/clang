import clang.cindex
from clang.cindex import ExceptionSpecificationKind
import os

kInputsDir = os.path.join(os.path.dirname(__file__), 'INPUTS')

def find_function_declarations(node, declarations=[]):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
        declarations.append((node.spelling, node.exception_specification_kind))
    for child in node.get_children():
        declarations = find_function_declarations(child, declarations)
    return declarations


def test_exception_specification_kind():
    index = clang.cindex.Index.create()
    input_file = os.path.join(kInputsDir, 'exception_spec.cpp')
    tu = index.parse(input_file, ['-std=c++14'])
    declarations = find_function_declarations(tu.cursor)

    expected = [
        ('square1', ExceptionSpecificationKind.NONE),
        ('square2', ExceptionSpecificationKind.BASIC_NOEXCEPT),
        ('square3', ExceptionSpecificationKind.COMPUTED_NOEXCEPT)
        ]
    assert declarations == expected


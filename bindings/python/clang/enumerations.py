#===- enumerations.py - Python Enumerations ------------------*- python -*--===#
#
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.
#
#===------------------------------------------------------------------------===#

"""
Clang Enumerations
==================

This module provides static definitions of enumerations that exist in libclang.

Enumerations are typically defined as a list of tuples. The exported values are
typically munged into other types or classes at module load time.

All enumerations are centrally defined in this file so they are all grouped
together and easier to audit. And, maybe even one day this file will be
automatically generated by scanning the libclang headers!
"""

# Maps to CXTokenKind. Note that libclang maintains a separate set of token
# enumerations from the C++ API.
TokenKinds = [
    ('PUNCTUATION', 0),
    ('KEYWORD', 1),
    ('IDENTIFIER', 2),
    ('LITERAL', 3),
    ('COMMENT', 4),
]

# Maps to ExceptionSpecificationType.
ExceptionSpecificationType = [
    ('None', 0),
    ('DynamicNone', 1),
    ('Dynamic', 2),
    ('MSAny', 3),
    ('BasicNoexcept', 4),
    ('ComputedNoexcept', 5),
    ('Unevaluated', 6),
    ('Uninstantiated', 7),
    ('Unparsed', 8),
]

__all__ = ['TokenKinds']

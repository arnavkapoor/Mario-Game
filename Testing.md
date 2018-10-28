Pylint Errors :-

https://github.com/PyCQA/pylint/issues/1498 (unsubscriptable object false positive)
https://github.com/PyCQA/pylint/issues/397  (numpy issue , fix using ----extension-pkg-whitelist=numpy)


pep8

pep8 cleared up the whitespace errors 

board.py
    used enumerate(list) in place of range(len(list))
    removed functions from inside classes that don't use a class variable.
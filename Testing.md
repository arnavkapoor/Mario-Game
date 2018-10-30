Pylint Errors :-

https://github.com/PyCQA/pylint/issues/1498 (unsubscriptable object false positive)
https://github.com/PyCQA/pylint/issues/397  (numpy issue , fix using ----extension-pkg-whitelist=numpy)


pep8 and refactoring.

autopep8 cleared up the whitespace errors 

Refactoring changes

1) used enumerate(list) in place of range(len(list))
2) removed methods from inside classes that don't use a class         variable or use self argument and changed them to separate         functions. 
3) Added doctsring to all classes and methods

Code Smells

1) Identified the different code smells and listed the same in the codereview pdf.
2) Resolved the God Line (Line 79) in enemy.py by replacing multiple statements and's in the if statement by a loop.





<<<<<<< HEAD
# IS-601-homework 3 & 4
<<<<<<< HEAD
=======
# IS-601 Homework 3 & 4

# Performed Testing

(myenv) ajaswal@AJ:~/projects/homework3$ pytest --pylint --cov
/home/ajaswal/.local/lib/python3.10/site-packages/pytest_pylint/plugin.py:223: PytestRemovedIn9Warning: The (path: py.path.local) argument is deprecated, please use (file_path: pathlib.Path)
see https://docs.pytest.org/en/latest/deprecations.html#py-path-local-arguments-for-hooks-replaced-with-pathlib-path
  def pytest_collect_file(self, path, parent):
================================================== test session starts ==================================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/ajaswal/projects/homework3
configfile: pytest.iniS
testpaths: tests
plugins: pylint-0.21.0, cov-5.0.0
collected 35 items                                                                                                      
--------------------------------------------------------------------------------
Linting files
.....
--------------------------------------------------------------------------------

tests/__init__.py::PYLINT SKIPPED (file(s) previously passed pylint checks)                                       [  2%]
tests/test_calculation.py::PYLINT SKIPPED (file(s) previously passed pylint checks)                               [  5%]
tests/test_calculation.py::test_calculation_operations[a0-b0-add-expected0] PASSED                                [  8%]
tests/test_calculation.py::test_calculation_operations[a1-b1-subtract-expected1] PASSED                           [ 11%]
tests/test_calculation.py::test_calculation_operations[a2-b2-multiply-expected2] PASSED                           [ 14%]
tests/test_calculation.py::test_calculation_operations[a3-b3-divide-expected3] PASSED                             [ 17%]
tests/test_calculation.py::test_calculation_operations[a4-b4-add-expected4] PASSED                                [ 20%]
tests/test_calculation.py::test_calculation_operations[a5-b5-subtract-expected5] PASSED                           [ 22%]
tests/test_calculation.py::test_calculation_operations[a6-b6-multiply-expected6] PASSED                           [ 25%]
tests/test_calculation.py::test_calculation_operations[a7-b7-divide-expected7] PASSED                             [ 28%]
tests/test_calculation.py::test_calculation_operations[a8-b8-modulus-expected8] PASSED                            [ 31%]
tests/test_calculation.py::test_calculation_operations[a9-b9-exponentiate-expected9] PASSED                       [ 34%]
tests/test_calculation.py::test_calculation_repr PASSED                                                           [ 37%]
tests/test_calculation.py::test_divide_by_zero PASSED                                                             [ 40%]
tests/test_calculations.py::PYLINT PASSED                                                                         [ 42%]
tests/test_calculations.py::test_add_calculation PASSED                                                           [ 45%]
tests/test_calculations.py::test_get_history PASSED                                                               [ 48%]
tests/test_calculations.py::test_clear_history PASSED                                                             [ 51%]
tests/test_calculations.py::test_get_latest PASSED                                                                [ 54%]
tests/test_calculations.py::test_get_latest_with_empty_history PASSED                                             [ 57%]
tests/test_calculator.py::PYLINT SKIPPED (file(s) previously passed pylint checks)                                [ 60%]
tests/test_calculator.py::test_addition PASSED                                                                    [ 62%]
tests/test_calculator.py::test_subtraction PASSED                                                                 [ 65%]
tests/test_calculator.py::test_multiply PASSED                                                                    [ 68%]
tests/test_calculator.py::test_divide PASSED                                                                      [ 71%]
tests/test_calculator.py::test_exponentiation PASSED                                                              [ 74%]
tests/test_calculator.py::test_modulus PASSED                                                                     [ 77%]
tests/test_operations.py::PYLINT SKIPPED (file(s) previously passed pylint checks)                                [ 80%]
tests/test_operations.py::test_operation_add PASSED                                                               [ 82%]
tests/test_operations.py::test_operation_subtract PASSED                                                          [ 85%]
tests/test_operations.py::test_operation_multiply PASSED                                                          [ 88%]
tests/test_operations.py::test_operation_divide PASSED                                                            [ 91%]
tests/test_operations.py::test_divide_by_zero PASSED                                                              [ 94%]
tests/test_operations.py::test_operation_modulus PASSED                                                           [ 97%]
tests/test_operations.py::test_operation_exponentiation PASSED                                                    [100%]

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                         Stmts   Miss  Cover
------------------------------------------------
calculator/__init__.py          29      0   100%
calculator/calculation.py       15      0   100%
calculator/calculations.py      22      1    95%
calculator/operations.py        17      1    94%
tests/__init__.py                0      0   100%
tests/test_calculation.py       16      0   100%
tests/test_calculations.py      28      4    86%
tests/test_calculator.py        13      0   100%
tests/test_operations.py        26      0   100%
------------------------------------------------
TOTAL                          166      6    96%
>>>>>>> part3
=======
# Performed Testing
(myenv) ajaswal@AJ:~/projects/homework3$ pytest --pylint --cov /home/ajaswal/.local/lib/python3.10/site-packages/pytest_pylint/plugin.py:223: PytestRemovedIn9Warning: The (path: py.path.local) argument is deprecated, please use (file_path: pathlib.Path) see https://docs.pytest.org/en/latest/deprecations.html#py-path-local-arguments-for-hooks-replaced-with-pathlib-path def pytest_collect_file(self, path, parent): ================================================== test session starts ================================================== platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0 -- /usr/bin/python3 cachedir: .pytest_cache rootdir: /home/ajaswal/projects/homework3 configfile: pytest.ini testpaths: tests plugins: pylint-0.21.0, cov-5.0.0 collected 35 items
Linting files .....
tests/init.py::PYLINT SKIPPED (file(s) previously passed pylint checks) [ 2%] tests/test_calculation.py::PYLINT SKIPPED (file(s) previously passed pylint checks) [ 5%] tests/test_calculation.py::test_calculation_operations[a0-b0-add-expected0] PASSED [ 8%] tests/test_calculation.py::test_calculation_operations[a1-b1-subtract-expected1] PASSED [ 11%] tests/test_calculation.py::test_calculation_operations[a2-b2-multiply-expected2] PASSED [ 14%] tests/test_calculation.py::test_calculation_operations[a3-b3-divide-expected3] PASSED [ 17%] tests/test_calculation.py::test_calculation_operations[a4-b4-add-expected4] PASSED [ 20%] tests/test_calculation.py::test_calculation_operations[a5-b5-subtract-expected5] PASSED [ 22%] tests/test_calculation.py::test_calculation_operations[a6-b6-multiply-expected6] PASSED [ 25%] tests/test_calculation.py::test_calculation_operations[a7-b7-divide-expected7] PASSED [ 28%] tests/test_calculation.py::test_calculation_operations[a8-b8-modulus-expected8] PASSED [ 31%] tests/test_calculation.py::test_calculation_operations[a9-b9-exponentiate-expected9] PASSED [ 34%] tests/test_calculation.py::test_calculation_repr PASSED [ 37%] tests/test_calculation.py::test_divide_by_zero PASSED [ 40%] tests/test_calculations.py::PYLINT PASSED [ 42%] tests/test_calculations.py::test_add_calculation PASSED [ 45%] tests/test_calculations.py::test_get_history PASSED [ 48%] tests/test_calculations.py::test_clear_history PASSED [ 51%] tests/test_calculations.py::test_get_latest PASSED [ 54%] tests/test_calculations.py::test_get_latest_with_empty_history PASSED [ 57%] tests/test_calculator.py::PYLINT SKIPPED (file(s) previously passed pylint checks) [ 60%] tests/test_calculator.py::test_addition PASSED [ 62%] tests/test_calculator.py::test_subtraction PASSED [ 65%] tests/test_calculator.py::test_multiply PASSED [ 68%] tests/test_calculator.py::test_divide PASSED [ 71%] tests/test_calculator.py::test_exponentiation PASSED [ 74%] tests/test_calculator.py::test_modulus PASSED [ 77%] tests/test_operations.py::PYLINT SKIPPED (file(s) previously passed pylint checks) [ 80%] tests/test_operations.py::test_operation_add PASSED [ 82%] tests/test_operations.py::test_operation_subtract PASSED [ 85%] tests/test_operations.py::test_operation_multiply PASSED [ 88%] tests/test_operations.py::test_operation_divide PASSED [ 91%] tests/test_operations.py::test_divide_by_zero PASSED [ 94%] tests/test_operations.py::test_operation_modulus PASSED [ 97%] tests/test_operations.py::test_operation_exponentiation PASSED [100%]

---------- coverage: platform linux, python 3.10.12-final-0 ---------- Name Stmts Miss Cover
calculator/init.py 29 0 100% calculator/calculation.py 15 0 100% calculator/calculations.py 22 1 95% calculator/operations.py 17 1 94% tests/init.py 0 0 100% tests/test_calculation.py 16 0 100% tests/test_calculations.py 28 4 86% tests/test_calculator.py 13 0 100% tests/test_operations.py 26 0 100%
TOTAL 166 6 96%
>>>>>>> 898423ad8e62069adc1c9982f4b49b3dc7b73722

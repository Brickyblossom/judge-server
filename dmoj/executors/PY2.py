from dmoj.executors.python_executor import PythonExecutor


class Executor(PythonExecutor):
    command = 'python'
    command_paths = ['python2.7', 'python2', 'python']
    pygments_traceback_lexer = 'py2tb'
    test_program = """
import sys
if sys.version_info.major == 2:
    print sys.stdin.read()
"""

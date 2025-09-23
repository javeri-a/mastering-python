# mastering-python

What is __pycache__ and .pyc files?

When you run a Python program, the interpreter does not directly execute the .py source code. Instead, it first converts your code into bytecode, which is a low-level, platform-independent format. This bytecode is then saved into .pyc files inside the __pycache__ folder. These files help Python execute programs faster because the code does not need to be recompiled every time you run it.

Key Points

.py = Your original source code written in Python.

Bytecode = An intermediate representation of your code created by the Python interpreter.

.pyc = Compiled bytecode files that Python stores for faster execution.

__pycache__ = The folder where .pyc files are saved automatically.

File naming format: filename.cpython-313.pyc

313 shows the Python version (e.g., Python 3.13).

Python uses .pyc files automatically, you don’t run them manually.

If environment variable PYTHONDONTWRITEBYTECODE=1 is set, .pyc files will not be created.
<img width="1589" height="1006" alt="f29ef9a6-c410-4fab-a0ec-7ca6806f2617" src="https://github.com/user-attachments/assets/3dc8abad-f17c-4c20-a965-4295b5af2621" />

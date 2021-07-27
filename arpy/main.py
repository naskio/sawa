from arpy.process import Process
from arpy.enum.file_error import FileError
import os
import sys

script_dir = os.path.dirname(__file__)

num_dict = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

keyword_dict = {
    "صحيح": "True",
    "خطأ": "False",
    "لاشيئ": "None",
    "كأن": "as",
    "يجزم": "assert",
    "غيرمتزامن": "async",
    "و": "and",
    "انتظر": "await",
    "كسر": "break",
    "صنف": "class",
    "واصل": "continue",
    "تعريف": "def",
    "حذف": "del",
    "إذا": "if",
    "وإلاإذا": "elif",
    "وإلا": "else",
    "بإستثناء": "except",
    "أخيرا": "finally",
    "من_أجل": "for",
    "من": "from",
    "شامل": "global",
    "استراد": "import",
    "في": "in",
    "هو": "is",
    "لامدا": "lambda",
    "ليس": "not",
    "غيرمحلي": "nonlocal",
    "أو": "or",
    "تجاوز": "pass",
    "ارفع": "raise",
    "ارجاع": "return",
    "حاول": "try",
    "طالما": "while",
    "مع": "with",
    "حصّل": "yield",
    "متغيرمنطقي": "bool",
    "عددصحيح": "int",
    "عددطبيعي": "float",
    "نص": "string",
    "__مرادف__": "__dict__",
}

# TODO: function_dict
function_dict = {
    'اطبع': "print",
    "ꦩꦸꦠ꧀ꦭꦏ꧀": "abs",
    "ꦲꦥꦸꦱ꧀ꦲꦠꦿꦶꦧꦸꦠ꧀": "delattr",
    "ꦕꦩ꧀ꦥꦸꦂ": "hash",
    "ꦱꦏ꧀ꦭꦺꦧꦠ꧀": "memoryview",
    "ꦲꦺꦴꦩ꧀ꦧꦾꦺꦴꦏ꧀": "set",
    "ꦏꦧꦺꦃ": "all",
    "ꦧꦲꦸꦱꦱ꧀ꦠꦿ": "dict",
    "ꦥꦶꦠꦸꦭꦸꦁ": "help",
    "ꦩꦶꦤꦶꦩꦭ꧀": "min",
    "ꦒꦺꦠꦂ": "getattr",
    "ꦱꦺꦠꦂ": "setattr",
    "ꦏꦁ": "any",
    "ꦣꦶꦂ": "dir",
    "ꦲꦺꦏ꦳꧀": "hex",
    "ꦧꦕꦸꦠ꧀": "next",
    "ꦲꦶꦫꦶꦱ꧀ꦱꦤ꧀": "slice",
    "ꦲꦱ꧀ꦏꦶ": "ascii",
    "ꦣꦶꦥ꦳꧀ꦩꦺꦴꦢ꧀": "divmod",
    "ꦲꦶꦣꦶ": "id",
    "ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀": "object",
    "ꦲꦸꦫꦸꦠ꧀": "sorted",
    "ꦧꦶꦤ꧀": "bin",
    "ꦲꦺꦤꦸꦩꦼꦂꦫꦺꦠ꧀": "enumerate",
    "ꦠꦸꦭꦶꦱ꧀": "input",
    "ꦲꦺꦴꦏ꧀ꦠ": "oct",
    "ꦱꦶꦒꦼꦒ꧀": "staticmethod",
    "ꦭꦺꦴꦒꦶꦱ꧀": "bool",
    "ꦲꦺꦥ꦳ꦭ꧀": "eval",
    "ꦲꦁꦏ": "int",
    "ꦧꦸꦏꦏ꧀": "open",
    "ꦱꦼꦫꦠ꧀": "str",
    "ꦊꦏꦱ꧀ꦩꦤꦺꦃ": "breakpoint",
    "ꦲꦗꦂ": "exec",
    "ꦧꦭꦤꦺ": "isinstance",
    "ꦲꦺꦴꦫꦼꦢ꧀": "ord",
    "ꦗꦸꦩ꧀ꦭꦃ": "sum",
    "ꦧꦶꦠꦼꦫꦺ": "bytearray",
    "ꦥ꦳ꦶꦭ꧀ꦠꦼꦂ": "filter",
    "ꦲꦤ꧀ꦣꦃꦲꦤ꧀": "issubclass",
    "ꦏ꧀ꦮꦱ": "pow",
    "ꦲꦸꦠꦩ": "super",
    "ꦧꦪ꧀ꦠ": "bytes",
    "ꦣꦺꦱꦶꦩꦭ꧀": "float",
    "ꦥꦫ": "iter",
    "ꦠꦸꦥꦼꦭ꧀": "tuple",
    "ꦔꦸꦚ꧀ꦢꦁ": "callable",
    "ꦮꦸꦗꦸꦢ꧀": "format",
    "ꦢꦮ": "len",
    "ꦏꦒꦸꦁꦔꦤꦺ": "property",
    "ꦩꦺꦴꦣꦺꦭ꧀": "type",
    "ꦕꦂ": "chr",
    "ꦧꦼꦏꦸꦮꦤ꧀": "frozenset",
    "ꦥꦿꦠꦺꦭꦤ꧀": "list",
    "ꦲꦤ꧀ꦠꦫ": "range",
    "ꦥ꦳ꦉꦱ꧀": "vars",
    "ꦩꦺꦠꦺꦴꦢ꧀ꦏꦼꦭꦱ꧀": "classmethod",
    "ꦗꦸꦥꦸꦏ꧀ꦲꦠꦼꦂ": "getattr",
    "ꦥꦿꦶꦧꦸꦩꦶ": "locals",
    "ꦫꦺꦥꦼꦂ": "repr",
    "ꦗꦶꦥ꧀": "zip",
    "ꦏꦺꦴꦩ꧀ꦥꦺꦭ꧀": "compile",
    "ꦱꦗꦒꦢ꧀": "globals",
    "ꦥꦼꦠ": "map",
    "ꦮꦭꦶꦏ꧀ꦲꦤꦺ": "reversed",
    "__ꦗꦸꦥꦸꦏ꧀__": "__import__",
    "__ꦊꦏꦱ꧀__": "__init__",
    "__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__": "__dict__",
    "ꦩꦤꦺꦏ": "complex",
    "ꦒꦣꦃ": "hasattr",
    "ꦥꦺꦴꦭ꧀": "max",
    "ꦮꦸꦠꦸꦃ": "round",
    "ꦣꦺꦮꦺ": "self",
}


def compile(file_name):
    py_content = ''
    # Reading file to process the text
    with open(file_name, 'r', encoding="utf-8") as file:
        # Process all content of the file
        py_content += Process(file, num_dict, keyword_dict, function_dict).process()
    # Splitting file name to remove existing extension in order to add python extension
    file_split = file_name.split(".")
    # Name of the python file to be created
    py_file = file_split[0] + ".py"
    # Creating the python file
    f = open(py_file, "w", encoding="utf-8")
    # And then writing content to the python file
    f.write(py_content)


def main(file_name):
    if os.path.isdir(file_name):
        # If the file name is directory then it will search all the file with *.بايثون and process all file
        for flnm in os.listdir(file_name):
            if flnm.endswith('.بايثون'):
                compile(flnm)
                print(' \r\n ')
    elif os.path.isfile(file_name):
        compile(file_name)
    else:
        sys.exit("'" + file_name + "'" + " " + FileError.INVALID_FILE.value)

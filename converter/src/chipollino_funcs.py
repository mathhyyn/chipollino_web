# import grpc
# from .generated import converter_pb2 as generated_pb2
# from .generated import converter_pb2_grpc as generated_pb2_grpc

# channel = grpc.insecure_channel('localhost:50051')
# stub = generated_pb2_grpc.GreeterStub(channel)

import os
import subprocess
import re


def getString():
    # request = generated_pb2.StringRequest()
    # request.name = "web client"
    # response = stub.getString(request)
    # return response.text
    return "hello world"

def getRegex():
    # request = generated_pb2.RegexRequest()
    # response = stub.getRegex(request)
    # return response.result
    return "a*b(a|b)"

def getNFA():
    return """NFA
    q1 initial_state
    ...
    q1 q2 a"""


def run_interpreter(text):
    try:
        os.chdir('Chipollino')
        subprocess.run('build/apps/InterpreterApp/Debug/InterpreterApp.exe', check=True)
        os.chdir('../')
    except subprocess.CalledProcessError:
        os.chdir('../')
        return None
    with open("Chipollino/resources/report.tex", 'r', encoding='utf-8') as tex_file:
        return tex_file.read()

def create_svg(text, session_key="0"):
    svg_str = ""
    try:
        tex_str = ""
        with open("Chipollino/resources/template/head.tex", 'r', encoding='utf-8') as head_file:
            tex_str += head_file.read().replace('\\maketitle', '')
        tex_str += '\\begin{preview}'
        tex_str += text
        tex_str += '\\end{preview}\n\\end{document}'

        folder_name = 'tmp'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        os.chdir(folder_name)
        file_name = f'{session_key}_svg'
        with open(f'{file_name}.tex', 'w', encoding='utf-8') as f:
            f.write(tex_str)
        print('rendering graph image..')
        subprocess.run(f'latex {file_name}.tex > {file_name}log.log', check=True)
        subprocess.run(f'dvisvgm --no-fonts {file_name}.dvi {file_name}.svg', check=True)
        with open(f'{file_name}.svg', 'r', encoding='utf-8') as svg_file:
            svg_str = svg_file.read()
            svg_str = re.sub(r"width='[^']*' height='[^']*'" , "", svg_str)
        
        files = os.listdir()
        del_files = [f for f in files if f.startswith(f"{file_name}.")]
        for file in del_files:
            os.remove(file)

        os.chdir('../')
    except subprocess.CalledProcessError:
        os.chdir('../')
        return None
    return svg_str
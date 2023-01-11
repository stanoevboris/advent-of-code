# class Node:
#     def __init__(self, name):
#         self.left = None
#         self.right = None
#         self.name = name
#         self.value = None
#         self.operation = None

def check_int(string):
    if string[0] in ('-', '+'):
        return string[1:].isdigit()
    return string.isdigit()


def calculate(node):
    value = nodes_dict[node]['value']
    if check_int(str(value)):
        return int(value)
    else:
        return int(eval(f"{calculate(nodes_dict[node]['left'])}" +
                        nodes_dict[node]['value'] +
                        f"{calculate(nodes_dict[node]['right'])}"))
def equation(node):
    value = nodes_dict[node]['value']
    if check_int(str(value)):
        return int(value)
    elif value == '-1j':
        return '-1j'
    else:
        return f"({equation(nodes_dict[node]['left'])}" + \
                        f"{nodes_dict[node]['value']}" + \
                        f"{equation(nodes_dict[node]['right'])})"


with open('input', 'r') as file:
    lines = file.read().split("\n")

nodes_dict = {}
for line in lines:
    name, value = line.split(":")

    if check_int(value.strip()):
        nodes_dict[name] = {'value': int(value.strip())}
    else:
        if "+" in value:
            left, right = value.split("+")
            left, right = left.strip(), right.strip()
            operand = "+"
        elif "-" in value:
            left, right = value.split("-")
            left, right = left.strip(), right.strip()
            operand = "-"
        elif "*" in value:
            left, right = value.split("*")
            left, right = left.strip(), right.strip()
            operand = "*"
        else:
            left, right = value.split("/")
            left, right = left.strip(), right.strip()
            operand = "/"
        nodes_dict[name] = {'left': left, 'right': right, 'value': operand}

print(calculate('root'))

nodes_dict['humn']['value'] = '-1j'
nodes_dict['root']['value'] = '-('
equation_var = eval(equation('root') + ")")
print(round(equation_var.real / equation_var.imag))

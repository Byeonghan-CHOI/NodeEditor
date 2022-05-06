import os, sys
from examples.example_calculator_1.calc_conf import register_node, OP_NODE_ADD, OP_NODE_SUB, OP_NODE_MUL, OP_NODE_DIV
from examples.example_calculator_1.calc_node_base import CalcNode

# Pyinstaller add folder with images in exe file
# resource_path from absolute path to relative_path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


@register_node(OP_NODE_ADD)
class CalcNode_Add(CalcNode):
    icon = resource_path("icons/add.png")
    op_code = OP_NODE_ADD
    op_title = "Add"
    content_label = "+"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 + input2


@register_node(OP_NODE_SUB)
class CalcNode_Sub(CalcNode):
    icon = resource_path("icons/sub.png")
    op_code = OP_NODE_SUB
    op_title = "Substract"
    content_label = "-"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 - input2

@register_node(OP_NODE_MUL)
class CalcNode_Mul(CalcNode):
    icon = resource_path("icons/mul.png")
    op_code = OP_NODE_MUL
    op_title = "Multiply"
    content_label = "*"
    content_label_objname = "calc_node_mul"

    def evalOperation(self, input1, input2):
        print('foo')
        return input1 * input2

@register_node(OP_NODE_DIV)
class CalcNode_Div(CalcNode):
    icon = resource_path("icons/divide.png")
    op_code = OP_NODE_DIV
    op_title = "Divide"
    content_label = "/"
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return input1 / input2

# way how to register by function call
# register_node_now(OP_NODE_ADD, CalcNode_Add)
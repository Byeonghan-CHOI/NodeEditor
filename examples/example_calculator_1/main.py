import os, sys, inspect
from qtpy.QtWidgets import QApplication
from examples.example_calculator_1.calc_window import CalculatorWindow

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


if __name__ == '__main__':
    app = QApplication(sys.argv)



    app.setStyle('Fusion')

    wnd = CalculatorWindow()

    wnd.show()

    sys.exit(app.exec_())
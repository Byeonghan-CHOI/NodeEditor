import os
import sys
import inspect

from qtpy.QtWidgets import QApplication

from nodeeditor.utils import loadStylesheet
from nodeeditor.node_editor_window import NodeEditorWindow

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

if __name__ == '__main__':

    app = QApplication(sys.argv)

    wnd = NodeEditorWindow()
    wnd.nodeeditor.addNodes()

    module_path = os.path.dirname(inspect.getfile(wnd.__class__) )
    print(module_path)

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
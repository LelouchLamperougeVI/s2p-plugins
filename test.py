import sys
import pkg_resources
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class test(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 200)
        bar = self.menuBar()
        plugin = bar.addMenu('&Plugins')

        self.plug_actions = {}
        for ep in pkg_resources.iter_entry_points(group='suite2p.plugin', name=None):
            plugin_class = ep.load()
            self.plug_actions[ep.name] = plugin_class(self)
            action = QAction(plugin_class.name, self)
            action.triggered.connect(self.plug_actions[ep.name].trigger)
            plugin.addAction(action)


def main():
    app = QApplication(sys.argv)
    gui = test()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

import sys
import pkg_resources
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)

        bar = self.menuBar()
        plugin = bar.addMenu('&Plugins')

        plug_actions = {}
        self.objects = {}
        for ep in pkg_resources.iter_entry_points(group='suite2p.plugin', name=None):
            cls = ep.load()
            self.objects[ep.name] = cls()
            plug_actions[ep.name] = QAction(self.objects[ep.name].menu, self)
            plug_actions[ep.name].triggered.connect(self.objects[ep.name].window)
            plugin.addAction(plug_actions[ep.name])
        #print("finished iter")
        #temp = plug_actions['smooth_dff']()
        #temp.window()


def main():
    app = QApplication(sys.argv)
    gui = test()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#for ep in iter_entry_points(group='suite2p.plugin', name=None):


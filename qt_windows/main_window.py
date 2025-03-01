from PyQt6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from .upload_tab import UploadTab
from .api_tab import ApiTab

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 Tab 页
        self.tabs = QTabWidget()
        self.tabs.addTab(ApiTab(), "调用接口")
        self.tabs.addTab(UploadTab(), "上传图片")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # 设置窗口属性
        self.setWindowTitle('智能家居监控系统')
        # 设置窗口的几何位置和大小
        # 前两个参数 300, 300 表示窗口左上角在屏幕上的坐标，即距离屏幕左侧 300 像素，距离屏幕顶部 300 像素
        # 后两个参数 800, 600 表示窗口的宽度为 800 像素，高度为 600 像素
        self.setGeometry(250, 250, 1000, 800)  # 增加窗口大小

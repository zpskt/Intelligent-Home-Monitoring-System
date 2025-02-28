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
        self.setGeometry(300, 300, 300, 200)

import logging
import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化 UI
        self.initUI()

    def initUI(self):
        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建按钮
        self.button = QPushButton('调用 Django 接口', self)
        self.button.clicked.connect(self.call_api)
        layout.addWidget(self.button)

        # 创建标签用于显示结果
        self.result_label = QLabel('点击按钮调用接口', self)
        layout.addWidget(self.result_label)

        # 设置布局
        self.setLayout(layout)

        # 设置窗口属性
        self.setWindowTitle('调用 Django 接口')
        self.setGeometry(300, 300, 300, 200)

    def call_api(self):
        try:
            # 替换为你的 Django 接口 URL
            url = 'http://127.0.0.1:8000/spotter/'
            logging.info(f'调用接口: {url}')
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                logging.info(f'接口返回数据: {data}')
                self.result_label.setText(str(data))
            else:
                self.result_label.setText(f'请求失败，状态码: {response.status_code}')
        except requests.RequestException as e:
            self.result_label.setText(f'请求出错: {str(e)}')
# 配置日志输出
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志格式
    handlers=[logging.StreamHandler()]  # 输出到控制台
)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

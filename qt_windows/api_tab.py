from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import requests
import logging
from .utils.logging_config import setup_logging

setup_logging()

class ApiTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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

    def call_api(self):
        try:
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

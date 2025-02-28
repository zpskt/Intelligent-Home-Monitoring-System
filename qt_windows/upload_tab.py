from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
import requests
import logging
from .utils.logging_config import setup_logging

setup_logging()

class UploadTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 创建上传按钮
        self.upload_button = QPushButton('上传图片', self)
        self.upload_button.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_button)

        # 创建标签用于显示结果
        self.result_label = QLabel('点击按钮上传图片', self)
        layout.addWidget(self.result_label)

        # 设置布局
        self.setLayout(layout)

    def upload_image(self):
        try:
            # 打开文件选择对话框
            file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg)")
            if file_path:
                with open(file_path, 'rb') as file:
                    files = {'detect_picture': file}
                    url = 'http://127.0.0.1:8000/spotter/detect_picture'
                    logging.info(url)
                    # 把file放入body中
                    response = requests.post(url, files=files)
                    logging.info(response)
                    if response.status_code == 200:
                        self.result_label.setText(response.text)
                    else:
                        self.result_label.setText(f'上传失败，状态码: {response.status_code}')
        except Exception as e:
            self.result_label.setText(f'上传出错: {str(e)}')

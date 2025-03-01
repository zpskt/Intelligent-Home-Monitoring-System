from PyQt6.QtCore import QFile, QIODeviceBase, Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
import requests
import logging
from .utils.logging_config import setup_logging
import os
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

        # 创建水平布局用于放置两个图片和对应的文字
        images_layout = QHBoxLayout()

        # 创建原图布局
        original_image_layout = QVBoxLayout()
        self.original_image_label = QLabel(self)
        original_image_layout.addWidget(self.original_image_label)
        self.original_result_label = QLabel('点击按钮上传图片', self)
        original_image_layout.addWidget(self.original_result_label)
        images_layout.addLayout(original_image_layout)

        # 创建检测后图片布局
        detected_image_layout = QVBoxLayout()
        self.detected_image_label = QLabel(self)
        detected_image_layout.addWidget(self.detected_image_label)
        self.detected_result_label = QLabel('检测结果将显示在这里', self)
        detected_image_layout.addWidget(self.detected_result_label)
        images_layout.addLayout(detected_image_layout)

        layout.addLayout(images_layout)

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
                    if response.status_code == 200:
                        response_data = response.json()
                        if response_data.get('status') == 'success':
                            # 获取图片 URL
                            image_url = response_data.get('data').get('image_url')
                            logging.info("image_url: " + image_url)
                        if image_url:
                            if os.path.exists(image_url):
                                file = QFile(image_url)
                                if file.open(QIODeviceBase.OpenModeFlag.ReadOnly):
                                    pixmap = QPixmap()
                                    pixmap.loadFromData(file.readAll())
                                    file.close()
                                    self.detected_image_label.setPixmap(pixmap)
                                    self.detected_result_label.setText('检测成功')
                                else:
                                    self.detected_result_label.setText('无法打开检测后的图片文件')
                            else:
                                self.detected_result_label.setText('检测后的图片文件不存在')
                        else:
                            self.detected_result_label.setText('未返回图片 URL')
                    else:
                        self.detected_result_label.setText(f'上传失败，状态码: {response.status_code}')

                # 显示原图
                pixmap = QPixmap(file_path)
                self.original_image_label.setPixmap(pixmap)
                self.original_result_label.setText('原图')

        except Exception as e:
            self.detected_result_label.setText(f'上传出错: {str(e)}')
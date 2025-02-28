import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # 设置日志级别为 INFO
        format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志格式
        handlers=[logging.StreamHandler()]  # 输出到控制台
    )

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QTextEdit
import sys

class DateSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('日期选择器')
        self.setGeometry(300, 300, 400, 300)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建年月选择下拉框
        self.date_label = QLabel('选择月份:')
        self.date_combo = QComboBox()

        # 添加日期选项（2025.01-2027.12）
        date_options = []
        for year in range(2025, 2028):
            for month in range(1, 13):
                date_options.append(f"{year}.{month:02d}")
        self.date_combo.addItems(date_options)

        # 创建输出文本框和提交按钮
        self.output_label = QLabel('输出:')
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.submit_button = QPushButton('计算工作日')

        # 添加部件到布局
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_combo)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.submit_button)

        # 连接信号和槽
        self.submit_button.clicked.connect(self.on_submit)

    def on_submit(self):
        selected_date = self.date_combo.currentText()
        self.output_text.setText(f'选择的日期: {selected_date}')

def main():
    app = QApplication(sys.argv)
    window = DateSelector()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
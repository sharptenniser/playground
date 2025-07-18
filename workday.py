from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QTextEdit
from chinese_calendar import is_workday
from datetime import datetime, timedelta
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
        try:
            # 将选择的年月转换为日期对象
            date_obj = datetime.strptime(selected_date + ".01", "%Y.%m.%d").date()
            
            # 获取该月的最后一天
            if date_obj.month == 12:
                next_month = date_obj.replace(year=date_obj.year + 1, month=1)
            else:
                next_month = date_obj.replace(month=date_obj.month + 1)
            last_day = next_month - timedelta(days=1)

            # 遍历该月的每一天，判断是否为工作日
            workdays = []
            current_date = date_obj
            while current_date <= last_day:
                if is_workday(current_date):
                    workdays.append(current_date.strftime("%Y-%m-%d"))
                current_date += timedelta(days=1)

            # 生成结果文本
            workday_count = len(workdays)
            workday_dates = "\n".join(workdays)
            result = f'该月工作日天数: {workday_count}\n工作日日期:\n{workday_dates}'
            self.output_text.setText(result)
        except Exception as e:
            self.output_text.setText(f'日期解析出错: {str(e)}')

def main():
    app = QApplication(sys.argv)
    window = DateSelector()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import  QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy,QHeaderView,QMessageBox,QListWidgetItem
import os
import shutil
import sys
from PyQt5.QtCore import QObject, pyqtSignal,QSize, Qt

class Patient_Image(QMainWindow):
    goBackSignal = pyqtSignal()
    def __init__(self, patient_name):
        super().__init__()

        # 使用loadUi加载UI文件
        loadUi('ui/patient_image.ui', self)

        # 设置 progress_1 被选中
        self.progress_1.setChecked(True)

        # 为 ListWidget_1 添加信号和槽连接
        self.listWidget_1.itemClicked.connect(self.on_listWidget_1_itemClicked)

        # 为 model_select_1 到 model_select_4 添加信号和槽连接
        self.model_select_1.toggled.connect(self.on_model_select_toggled)
        self.model_select_2.toggled.connect(self.on_model_select_toggled)
        self.model_select_3.toggled.connect(self.on_model_select_toggled)
        self.model_select_4.toggled.connect(self.on_model_select_toggled)

        # 为 split 按钮添加点击事件连接
        self.split.clicked.connect(self.on_split_clicked)

        # 加载病人文件夹内容到 listWidget_1 中
        self.loadPatientFiles(patient_name)

        self.back.clicked.connect(self.goBackToPatientManage)        


     # 加载病人文件夹内容到 listWidget_1 中
    def loadPatientFiles(self, patient_name):
        # 获取病人文件夹路径
        patient_folder_path = os.path.join('patients', patient_name)

        # 检查文件夹是否存在
        if os.path.exists(patient_folder_path) and os.path.isdir(patient_folder_path):
            # 清空 listWidget_1 中的内容
            self.listWidget_1.clear()

            # 获取文件夹中的文件和子文件夹
            files_and_folders = os.listdir(patient_folder_path)

            # 将文件和子文件夹名称添加到 listWidget_1 中
            for item in files_and_folders:
                self.listWidget_1.addItem(item)

    def on_listWidget_1_itemClicked(self, item):
        # 当 ListWidget_1 中的某一行被选中时，progress_2 被选中
        self.progress_2.setChecked(True)

    def on_model_select_toggled(self):
        # 当 model_select_1 到 model_select_4 中的某个被选中时，progress_3 被选中
        if self.model_select_1.isChecked() or self.model_select_2.isChecked() or \
           self.model_select_3.isChecked() or self.model_select_4.isChecked():
            self.progress_3.setChecked(True)
    
    def on_split_clicked(self):
        # 当 split 按钮被点击时，progress_4 被选中
        self.progress_4.setChecked(True)

    def goBackToPatientManage(self):
        # self.progress_1.setChecked(False)
        self.progress_2.setChecked(False)
        self.progress_3.setChecked(False)
        self.progress_4.setChecked(False)
        self.progress_5.setChecked(False)
        self.model_select_1.setChecked(False)
        self.model_select_2.setChecked(False)
        self.model_select_3.setChecked(False)
        self.model_select_4.setChecked(False)
        # 当用户点击返回按钮时发出信号
        self.goBackSignal.emit()
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Patient_Image()
#     window.show()
#     sys.exit(app.exec_())
# import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import  QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy,QHeaderView,QMessageBox
import os
import shutil
from PyQt5.QtCore import QObject, pyqtSignal

class Patient_Manage(QMainWindow):
    navigateSignal = pyqtSignal()#splitWorkflow跳转信号
    def __init__(self):
        super().__init__()

        # 使用loadUi加载UI文件
        loadUi('ui/patient_manage.ui', self)
        

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(1, 380)  # 第二列宽度为430
        self.tableWidget.setColumnWidth(2, 325)  # 第三列宽度为325

        patients_directory = 'patients'
        if os.path.isdir(patients_directory):
            patient_folders = next(os.walk(patients_directory))[1]
            for patient_name in patient_folders:
                self.addRow(patient_name)

        self.addRowButton.clicked.connect(self.addRow)  # 连接新增行按钮的点击事件到添加行函数
        self.deleteRowButton.clicked.connect(self.deleteRow)  # 连接删除行按钮的点击事件到删除行函数
        self.sure.clicked.connect(self.enterButtonClicked)#点击确认按钮，新增文件夹
        self.tableWidget.itemSelectionChanged.connect(self.showPatientFiles)#点击某一行，该文件夹下的文件以及子文件夹展示在listwidget中

    # 添加新行的函数
    def addRow(self, patient_name=None):
        rowPosition = self.tableWidget.rowCount()  # 获取当前表格行数
        self.tableWidget.insertRow(rowPosition)  # 在表格中插入新行

        if patient_name is not None:
        # 在新行中显示病人姓名
            name_item = QTableWidgetItem(patient_name)
            self.tableWidget.setItem(rowPosition, 0, name_item)

        # 设置新增行的高度
        self.tableWidget.setRowHeight(rowPosition, 50)  # 将新增行的高度设置为50像素

        # 添加按钮到第二列
        splitWorkflowButton = QPushButton("splitWorkflow")
        trainWorkflowButton = QPushButton("trainWorkflow")
        splitWorkflowButton.clicked.connect(self.navigateToPatient_Image)

        # 创建水平布局并添加按钮
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(splitWorkflowButton)
        buttonLayout.addWidget(trainWorkflowButton)

        # 创建一个 QWidget 来容纳水平布局
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)

        # 将 QWidget 设置为表格的单元格
        self.tableWidget.setCellWidget(rowPosition, 1, buttonWidget)


        # 添加按钮到第三列
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")

        # 创建水平布局并添加按钮
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)

        # 创建一个 QWidget 来容纳水平布局
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)

        # 将 QWidget 设置为表格的单元格
        self.tableWidget.setCellWidget(rowPosition, 2, buttonWidget)

    # 删除行的函数
    def deleteRow(self):
        currentRow = self.tableWidget.currentRow()  # 获取当前选中行的索引
        if currentRow >= 0:  # 如果有选中行
            # 获取选中行的病人姓名
            patientNameItem = self.tableWidget.item(currentRow, 0)
            if patientNameItem is not None:
                patientName = patientNameItem.text()
                
                # 删除 patients 文件夹中对应的文件夹
                patients_directory = 'patients'
                folder_path = os.path.join(patients_directory, patientName)
                if os.path.exists(folder_path):  # 检查文件夹是否存在
                    try:
                        shutil.rmtree(folder_path)  # 递归删除文件夹及其内容
                    except Exception as e:
                        QMessageBox.warning(self, "Warning", f"Failed to delete folder '{patientName}': {str(e)}")
                        return
                    QMessageBox.information(self, "Info", f"Folder '{patientName}' deleted from 'patients' directory.")
                else:
                    QMessageBox.warning(self, "Warning", f"Folder '{patientName}' does not exist in 'patients' directory.")

            self.tableWidget.removeRow(currentRow)  # 从表格中删除选中行

    #点击确认新建病人信息 
    def enterButtonClicked(self):
        # 获取病人姓名
        patientNameItem = self.tableWidget.item(self.tableWidget.rowCount() - 1, 0)
        if patientNameItem is None:
            QMessageBox.warning(self, "Warning", "Please enter patient name.")
            return
        patientName = patientNameItem.text()

        # 在 patients 目录下创建一个新的文件夹
        patients_directory = 'patients'
        new_folder_path = os.path.join(patients_directory, patientName)
        if not os.path.exists(new_folder_path):  # 检查文件夹是否已存在
            os.makedirs(new_folder_path)
            QMessageBox.information(self, "Info", f"Folder '{patientName}' created in 'patients' directory.")
        else:
            QMessageBox.warning(self, "Warning", f"Folder '{patientName}' already exists in 'patients' directory.")

    # listwidget展示patients内的文件
    def showPatientFiles(self):
        # 清空 listWidget 中的内容
        self.listWidget.clear()

        # 获取选中行的索引
        currentRow = self.tableWidget.currentRow()

        if currentRow >= 0:
            # 获取选中行的病人姓名
            patientNameItem = self.tableWidget.item(currentRow, 0)
            if patientNameItem is not None:
                patientName = patientNameItem.text()

                # 获取病人文件夹路径
                patients_directory = 'patients'
                folder_path = os.path.join(patients_directory, patientName)

                # 检查文件夹是否存在
                if os.path.exists(folder_path) and os.path.isdir(folder_path):
                    # 获取文件夹中的文件和子文件夹
                    files_and_folders = os.listdir(folder_path)

                    # 将文件和子文件夹名称添加到 listWidget 中
                    for item in files_and_folders:
                        self.listWidget.addItem(item)

    # splitWorkflowButton跳转
    def navigateToPatient_Image(self):
            # 当用户点击按钮时发出信号
            self.navigateSignal.emit()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Patient_Manage()
#     window.show()
#     sys.exit(app.exec_())

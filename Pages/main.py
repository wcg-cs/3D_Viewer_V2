import sys
from PyQt5.QtWidgets import QApplication
from Patient_Manage import Patient_Manage
from Patient_Image import Patient_Image

class MainApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.patient_manage_page = Patient_Manage()
        self.patient_info_page = None

        # 连接界面一的信号到页面跳转的槽函数
        self.patient_manage_page.navigateSignal.connect(self.navigateToPatient_Image)

        # 显示界面一
        self.patient_manage_page.show()
        sys.exit(self.app.exec_())

    def navigateToPatient_Image(self):
        # 获取当前选中行的病人姓名
        current_row = self.patient_manage_page.tableWidget.currentRow()
        patient_name_item = self.patient_manage_page.tableWidget.item(current_row, 0)
        if patient_name_item is not None:
            patient_name = patient_name_item.text()
            # print(patient_name+'\n')

            # 如果界面二未被实例化，则实例化并加载病人文件
            if self.patient_info_page is None:
                self.patient_info_page = Patient_Image(patient_name)
                self.patient_info_page.loadPatientFiles(patient_name)
                self.patient_info_page.goBackSignal.connect(self.goBackToPatientManage)
                self.patient_info_page.show()
            else:
                # 如果界面二已经被实例化，则直接加载病人文件
                self.patient_info_page.loadPatientFiles(patient_name)
                self.patient_info_page.show()

            # 隐藏界面一
            self.patient_manage_page.hide()

    def goBackToPatientManage(self):
        # 隐藏界面二
        self.patient_info_page.hide()
        # 显示界面一
        self.patient_manage_page.show()

if __name__ == "__main__":
    main_app = MainApplication()

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Giriş Ekranı')
		self.resize(350, 150)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Kullanıcı adı: </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Lütfen kullanıcı adınızı girin')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Şifre: </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Lütfen şifrenizi girin')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Giriş')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'zeynep' and self.lineEdit_password.text() == '123':
			msg.setText('Hoşgeldin Zeynep')
			msg.exec_()
			app.quit()
		else:
			msg.setText('Yanlış kullanıcı adı veya şifre.')
			msg.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()
	sys.exit(app.exec_())

import re
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence


class formValidate(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("week5/week5.ui", self)
    self.setWindowTitle("Form Validation")

    self.genderCom.addItem("Pilih Gender")
    self.genderCom.addItems(["Pria", "Wanita"])

    self.eduCom.addItem("Pilih Edukasi")
    self.eduCom.addItems(["Dasar","Menengah Pertama","Menengah Atas", "Diploma", "Bachelor", "Master", "Doctoral"])

    self.saveBtn.clicked.connect(self.validate_form)
    self.clearBtn.clicked.connect(self.clear_fields)

    QShortcut(QKeySequence("Q"), self).activated.connect(self.close)

  def validate_form(self):
    nama = self.nama_input.text().strip()
    email = self.email_input.text().strip()
    umur = self.umur_input.text().strip()
    hp = self.hp_input.text().strip().replace(" ", "")
    alamat = self.alamat_input.toPlainText().strip()
    gender = self.genderCom.currentText()
    edu = self.eduCom.currentText()

    if not nama or len(nama) < 3:
      self.show_warning("Nama hasus diisi dan harus setidaknya 3 karakter atau lebih.")
    elif not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
      self.show_warning("Masukkan email yang valid.")
    elif not umur.isdigit():
      self.show_warning("Umur harus angka.")
    elif not len(hp) != 13:
      self.show_warning("Nomor handphone harus setidaknya 13 digit.")
    elif not alamat:
      self.show_warning("Masukkan email.")
    elif gender == "Pilih Gender":
      self.show_warning("Pilih gender anda.")
    elif edu == "Pilih Edukasi":
      self.show_warning("Pilih edukasi anda.")
    else:
      QMessageBox.information(self, "Sukses", "Data Berhasil Tersimpan!!!")
      self.clear_fields()
  
  def show_warning(self, message):
    QMessageBox.warning(self, "Validation Error", message)

  def clear_fields(self):
    self.nama_input.clear()
    self.email_input.clear()
    self.umur_input.clear()
    self.hp_input.clear()
    self.alamat_input.clear()
    self.genderCom.setCurrentIndex(0)
    self.eduCom.setCurrentIndex(0)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = formValidate()
  window.show()
  sys.exit(app.exec_())
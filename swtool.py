from tkinter import font
from PyQt6 import QtCore, QtGui, QtWidgets
import paramiko
import socket
import subprocess
import platform
import os
import time


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1045, 729)

        MainWindow.setStyleSheet("background-color: rgb(35, 114, 150); color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 181, 561))
        self.widget.setObjectName("widget")
        self.IP_gb = QtWidgets.QGroupBox(parent=self.widget)
        self.IP_gb.setGeometry(QtCore.QRect(10, 0, 161, 91))

        self.host_name_gb = QtWidgets.QGroupBox(parent=self.widget)
        self.host_name_gb.setGeometry(QtCore.QRect(10, 100, 161, 91))
        font = QtGui.QFont()

        font.setBold(True)
        font.setItalic(True)
        self.host_name_gb.setFont(font)
        self.host_name_gb.setObjectName("host_name_gb")

        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(190, 10, 841, 71))
        self.widget_5.setObjectName("widget_5")

        self.groupBox_9 = QtWidgets.QGroupBox(self.widget_5)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 0, 841, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("background-color: rgb(153, 158, 158);")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")

        self.show_interface_btn = QtWidgets.QPushButton(self.widget)
        self.show_interface_btn.setGeometry(QtCore.QRect(10, 200, 161, 24))
        self.show_interface_btn.setObjectName("show_interface_btn")
        self.show_interface_btn.setText("Show Interface Status")

        self.connect_vm_btn = QtWidgets.QPushButton("Connect to VM", self.groupBox_9)
        self.connect_vm_btn.setGeometry(QtCore.QRect(600, 20, 140, 24))
        self.connect_vm_btn.clicked.connect(self.connect_to_vm)
        font = QtGui.QFont()

        font.setBold(True)
        font.setItalic(True)
        self.IP_gb.setFont(font)
        self.IP_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                 "")
        self.IP_gb.setObjectName("IP_gb")
        self.add_ip_lbl = QtWidgets.QTextEdit(parent=self.IP_gb)
        self.add_ip_lbl.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.add_ip_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_ip_lbl.setObjectName("add_ip_lbl")
        self.ping_btn = QtWidgets.QPushButton(parent=self.IP_gb)
        self.ping_btn.setGeometry(QtCore.QRect(40, 60, 75, 24))
        self.ping_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.ping_btn.setObjectName("ping_btn")
        self.ping_btn.clicked.connect(self.perform_ping)

        self.host_name_gb = QtWidgets.QGroupBox(parent=self.widget)
        self.host_name_gb.setGeometry(QtCore.QRect(10, 100, 161, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.host_name_gb.setFont(font)
        self.host_name_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                        "")
        self.host_name_gb.setObjectName("host_name_gb")
        self.hostname_lbl = QtWidgets.QTextEdit(parent=self.host_name_gb)
        self.hostname_lbl.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.hostname_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hostname_lbl.setObjectName("hostname_lbl")
        self.set_btn = QtWidgets.QPushButton(parent=self.host_name_gb)
        self.set_btn.setGeometry(QtCore.QRect(40, 60, 75, 24))
        self.set_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.set_btn.setObjectName("set_btn")
        self.set_btn.clicked.connect(self.on_set_click)
        self.Configurevlan_gb = QtWidgets.QGroupBox(parent=self.widget)
        self.Configurevlan_gb.setGeometry(QtCore.QRect(10, 200, 161, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.Configurevlan_gb.setFont(font)
        self.Configurevlan_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                            "")
        self.Configurevlan_gb.setObjectName("Configurevlan_gb")
        self.label = QtWidgets.QLabel(parent=self.Configurevlan_gb)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.Configurevlan_gb)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.vlan_lbl = QtWidgets.QTextEdit(parent=self.Configurevlan_gb)
        self.vlan_lbl.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.vlan_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vlan_lbl.setObjectName("vlan_lbl")
        self.vlanname_lbl = QtWidgets.QTextEdit(parent=self.Configurevlan_gb)
        self.vlanname_lbl.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.vlanname_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vlanname_lbl.setObjectName("vlanname_lbl")
        self.create_btn = QtWidgets.QPushButton(parent=self.Configurevlan_gb)
        self.create_btn.setGeometry(QtCore.QRect(40, 130, 75, 24))
        self.create_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.create_btn.setObjectName("create_btn")
        self.Switchport_gb = QtWidgets.QGroupBox(parent=self.widget)
        self.Switchport_gb.setGeometry(QtCore.QRect(10, 370, 161, 191))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.Switchport_gb.setFont(font)
        self.Switchport_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                         "")
        self.Switchport_gb.setTitle("")
        self.Switchport_gb.setObjectName("Switchport_gb")
        self.label_3 = QtWidgets.QLabel(parent=self.Switchport_gb)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.Switchport_gb)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_4.setObjectName("label_4")
        self.vlan_lbl_2 = QtWidgets.QTextEdit(parent=self.Switchport_gb)
        self.vlan_lbl_2.setGeometry(QtCore.QRect(10, 120, 141, 31))
        self.vlan_lbl_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vlan_lbl_2.setObjectName("vlan_lbl_2")
        self.addport_btn = QtWidgets.QPushButton(parent=self.Switchport_gb)
        self.addport_btn.setGeometry(QtCore.QRect(40, 160, 75, 24))
        self.addport_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.addport_btn.setObjectName("addport_btn")
        self.addport_btn.clicked.connect(self.configure_switch_port)
        self.label_5 = QtWidgets.QLabel(parent=self.Switchport_gb)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.label_5.setObjectName("label_5")
        self.switchport_sbox = QtWidgets.QSpinBox(parent=self.Switchport_gb)
        self.switchport_sbox.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.switchport_sbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.switchport_sbox.setObjectName("switchport_sbox")
        self.port_sbox = QtWidgets.QSpinBox(parent=self.Switchport_gb)
        self.port_sbox.setGeometry(QtCore.QRect(10, 70, 141, 22))
        self.port_sbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.port_sbox.setObjectName("port_sbox")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(190, 90, 851, 481))
        self.widget_2.setObjectName("widget_2")
        self.clitext = QtWidgets.QTextEdit(parent=self.widget_2)
        self.clitext.setGeometry(QtCore.QRect(-10, 0, 851, 481))
        self.clitext.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clitext.setObjectName("clitext")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 580, 1041, 141))
        self.widget_3.setObjectName("widget_3")
        self.banner_gb = QtWidgets.QGroupBox(parent=self.widget_3)
        self.banner_gb.setGeometry(QtCore.QRect(10, 10, 331, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.banner_gb.setFont(font)
        self.banner_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                     "")

        self.banner_gb.setObjectName("banner_gb")
        self.banner_lbl = QtWidgets.QTextEdit(parent=self.banner_gb)
        self.banner_lbl.setGeometry(QtCore.QRect(10, 20, 311, 71))
        self.banner_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.banner_lbl.setObjectName("banner_lbl")
        self.set_btn_2 = QtWidgets.QPushButton(parent=self.banner_gb)
        self.set_btn_2.setGeometry(QtCore.QRect(120, 100, 75, 24))
        self.set_btn_2.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.set_btn_2.setObjectName("set_btn_2")
        self.set_btn_2.clicked.connect(self.on_set_banner_click)
        self.quickcommands_gb = QtWidgets.QGroupBox(parent=self.widget_3)
        self.quickcommands_gb.setGeometry(QtCore.QRect(350, 10, 441, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.quickcommands_gb.setFont(font)
        self.quickcommands_gb.setStyleSheet("background-color: rgb(206, 216, 229);\n"
                                            "")
        self.quickcommands_gb.setObjectName("quickcommands_gb")
        self.refresh_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.refresh_btn.setGeometry(QtCore.QRect(10, 20, 131, 24))
        self.refresh_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.reset)
        self.cli_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.cli_btn.setGeometry(QtCore.QRect(150, 20, 131, 24))
        self.cli_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.cli_btn.setObjectName("cli_btn")
        self.cli_btn.clicked.connect(self.cliOpen)
        self.showarp_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.showarp_btn.setGeometry(QtCore.QRect(290, 20, 131, 24))
        self.showarp_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.showarp_btn.setObjectName("showarp_btn")
        self.showarp_btn.clicked.connect(self.show_arp)
        self.showinterface_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.showinterface_btn.setGeometry(QtCore.QRect(290, 60, 131, 24))
        self.showinterface_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.showinterface_btn.setObjectName("showinterface_btn")
        self.showinterface_btn.clicked.connect(self.show_interface)
        self.showssh_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.showssh_btn.setGeometry(QtCore.QRect(150, 60, 131, 24))
        self.showssh_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.showssh_btn.setObjectName("showssh_btn")
        self.showssh_btn.clicked.connect(self.show_ssh)
        self.showcdp_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.showcdp_btn.setGeometry(QtCore.QRect(10, 60, 131, 24))
        self.showcdp_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.showcdp_btn.setObjectName("showcdp_btn")
        self.showcdp_btn.clicked.connect(self.show_cdp)
        self.showrun_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.showrun_btn.setGeometry(QtCore.QRect(10, 100, 131, 24))
        self.showrun_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.showrun_btn.setObjectName("showrun_btn")
        self.showrun_btn.clicked.connect(self.show_run)
        self.mactable_btn = QtWidgets.QPushButton(parent=self.quickcommands_gb)
        self.mactable_btn.setGeometry(QtCore.QRect(150, 100, 131, 24))
        self.mactable_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.mactable_btn.setObjectName("mactable_btn")
        self.mactable_btn.clicked.connect(self.show_mac_table)
        self.uploadconfi_btn = QtWidgets.QPushButton(parent=self.widget_3)
        self.uploadconfi_btn.setGeometry(QtCore.QRect(820, 10, 211, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.uploadconfi_btn.setFont(font)
        self.uploadconfi_btn.setStyleSheet("background-color: rgb(190, 252, 255);")
        self.uploadconfi_btn.setObjectName("uploadconfi_btn")
        self.uploadconfi_btn.clicked.connect(self.upload_configuration)

        self.save_btn = QtWidgets.QPushButton(parent=self.widget_3)
        self.save_btn.setGeometry(QtCore.QRect(820, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color: rgb(190, 252, 255);")
        self.save_btn.setText("Save Configuration")
        self.save_btn.clicked.connect(self.save_configuration)

        self.widget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(190, 10, 841, 71))
        self.widget_5.setObjectName("widget_5")

        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.widget_5)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 0, 841, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("background-color: rgb(153, 158, 158);")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")

        self.IPadd_tb = QtWidgets.QTextEdit(parent=self.groupBox_9)
        self.IPadd_tb.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.IPadd_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IPadd_tb.setObjectName("IPadd_tb")
        self.ip_add_lbl = QtWidgets.QLabel(parent=self.groupBox_9)
        self.ip_add_lbl.setGeometry(QtCore.QRect(20, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ip_add_lbl.setFont(font)
        self.ip_add_lbl.setObjectName("ip_add_lbl")
        self.uname_tb = QtWidgets.QTextEdit(parent=self.groupBox_9)
        self.uname_tb.setGeometry(QtCore.QRect(250, 20, 201, 31))
        self.uname_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_tb.setObjectName("uname_tb")
        self.uname_lbl = QtWidgets.QLabel(parent=self.groupBox_9)
        self.uname_lbl.setGeometry(QtCore.QRect(250, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.uname_lbl.setFont(font)
        self.uname_lbl.setObjectName("uname_lbl")
        self.password_tb = QtWidgets.QTextEdit(parent=self.groupBox_9)
        self.password_tb.setGeometry(QtCore.QRect(490, 20, 231, 31))
        self.password_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_tb.setObjectName("password_tb")
        self.password_lbl = QtWidgets.QLabel(parent=self.groupBox_9)
        self.password_lbl.setGeometry(QtCore.QRect(490, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.password_lbl.setFont(font)
        self.password_lbl.setObjectName("password_lbl")
        self.connect_btn = QtWidgets.QPushButton(parent=self.groupBox_9)
        self.connect_btn.setGeometry(QtCore.QRect(750, 20, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.connect_btn.setFont(font)
        self.connect_btn.setStyleSheet("background-color: rgb(212, 225, 221);")
        self.connect_btn.setObjectName("connect_btn")
        self.connect_btn.clicked.connect(self.connect_to_vm)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ping_btn.clicked.connect(self.perform_ping)
        self.create_btn.clicked.connect(self.configure_vlan)

        self.show_interface_btn.clicked.connect(self.show_interface_status)

    def show_arp(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show arp\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("ARP table displayed.")

            self.clitext.setText(f"ARP table displayed, output: {output}")





        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def show_cdp(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show cdp\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("CDP table displayed.")

            self.clitext.setText(f"CDP table displayed, output: {output}")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def show_mac_table(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show mac address-table\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("MAC table displayed.")

            self.clitext.setText(f"MAC table displayed, output: {output}")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def show_run(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show running-config\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("Running configuration displayed.")

            self.clitext.setText(f"Running configuration displayed, output: {output}")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def on_set_banner_click(self):

        if self.banner_lbl.toPlainText() == "":
            self.clitext.setText("Please enter the banner text")
        else:

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ip = self.IPadd_tb.toPlainText()
            username = self.uname_tb.toPlainText()
            password = self.password_tb.toPlainText()
            banner_text = self.banner_lbl.toPlainText()

            try:

                ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

                ssh_shell = ssh_client.invoke_shell()

                while not ssh_shell.recv_ready():
                    time.sleep(1)

                ssh_shell.send("enable\n")
                time.sleep(1)

                output = ssh_shell.recv(1000).decode()
                if "Password" in output:
                    ssh_shell.send(password + "\n")
                    time.sleep(1)

                ssh_shell.send("configure terminal\n")
                time.sleep(1)

                ssh_shell.send(f"banner motd {banner_text}\n")
                time.sleep(1)

                ssh_client.close()

                self.clitext.setText(f"Banner set to {banner_text}.")

            except paramiko.AuthenticationException:
                self.clitext.setText("Authentication failed. Please check your credentials.")
            except paramiko.SSHException as ssh_err:
                self.clitext.setText("SSH error")
            except Exception as e:
                self.clitext.setText("An error occurred")

    def show_ssh(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show ssh\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("SSH table displayed.")

            self.clitext.setText(f"SSH table displayed, output: {output}")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def show_interface(self):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("show interface\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText("Interface table displayed.")

            self.clitext.setText(f"Interface table displayed, output: {output}")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")

        pass

    def cliOpen(self):
        try:
            if os.name == 'nt':
                subprocess.Popen("cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(
                    ["gnome-terminal" if os.environ.get("DESKTOP_SESSION") == "gnome" else "x-terminal-emulator"])
        except Exception as e:
            print(f"Error opening command prompt: {e}")

    def reset(self):
        self.clitext.clear()  #cliText
        self.IPadd_tb.clear()  #ip_address_text
        self.uname_tb.clear()  #user_name_text
        self.password_tb.clear()  #password_text
        self.hostname_lbl.clear()  #subgroup2_text
        self.add_ip_lbl.clear()  #subgroup1_text
        self.vlan_lbl.clear()  #subgroup3_text
        self.vlanname_lbl.clear()  #subgroup4_text
        self.switchport_sbox.clear()  #subgroup5_spinner
        self.port_sbox.clear()  #subgroup6_spinner
        self.vlan_lbl_2.clear()  #subgroup7_text
        self.banner_lbl.clear()  #banner_pallet_text

    def save_configuration(self):

        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()
        hostname = self.hostname_lbl.toPlainText()
        add_ip = self.add_ip_lbl.toPlainText()
        vlan_id = self.vlan_lbl.toPlainText()
        vlan_name = self.vlanname_lbl.toPlainText()
        switchport = self.switchport_sbox.value()
        port = self.port_sbox.value()
        vlan_id_2 = self.vlan_lbl_2.toPlainText()
        banner_text = self.banner_lbl.toPlainText()

        config_data = f"{ip}\n{username}\n{password}\n{hostname}\n{add_ip}\n{vlan_id}\n{vlan_name}\n{switchport}\n{port}\n{vlan_id_2}\n{banner_text}"

        try:
            with open("config.txt", "w") as file:
                file.write(config_data)
            self.clitext.setText("Configuration data saved to config.txt.")
        except Exception as e:
            self.clitext.setText(f"An error occurred: {e}")

    def upload_configuration(self):

        try:
            with open("config.txt", "r") as file:
                config_data = file.read().splitlines()
        except FileNotFoundError:
            self.clitext.setText("Configuration file not found.")
            return
        except Exception as e:
            self.clitext.setText(f"An error occurred: {e}")
            return

        self.IPadd_tb.setPlainText(config_data[0])
        self.uname_tb.setPlainText(config_data[1])
        self.password_tb.setPlainText(config_data[2])
        self.hostname_lbl.setPlainText(config_data[3])
        self.add_ip_lbl.setPlainText(config_data[4])
        self.vlan_lbl.setPlainText(config_data[5])
        self.vlanname_lbl.setPlainText(config_data[6])
        self.switchport_sbox.setValue(int(config_data[7]))
        self.port_sbox.setValue(int(config_data[8]))
        self.vlan_lbl_2.setPlainText(config_data[9])
        self.banner_lbl.setPlainText(config_data[10])

    def configure_switch_port(self):
        vlan_id = self.vlan_lbl.toPlainText()
        vlan_name = self.vlanname_lbl.toPlainText()
        switch_port = self.switchport_sbox.value()
        port = self.port_sbox.value()
        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("configure terminal\n")
            time.sleep(1)

            ssh_shell.send(f"interface FastEthernet0/{switch_port}\n")
            time.sleep(1)

            ssh_shell.send(f"switchport access vlan {vlan_id}\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText(f"Successfully configured switch port {switch_port} to VLAN {vlan_id}.")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as ssh_err:
            self.clitext.setText("SSH error")
        except Exception as e:
            self.clitext.setText("An error occurred")

    def perform_ping(self):
        ip_address = self.add_ip_lbl.toPlainText()

        try:

            output = subprocess.check_output(["ping", "-c", "4", ip_address])

            if b"bytes from" in output:
                self.clitext.setText(f"Host {ip_address} is reachable.")
            else:
                self.clitext.setText(f"Host {ip_address} is unreachable.")

        except subprocess.CalledProcessError:
            self.clitext.setText("Error: Failed to execute the ping command.")
        pass

    def configure_vlan(self):
        vlan_id = self.vlan_lbl.toPlainText()
        vlan_name = self.vlanname_lbl.toPlainText()
        ip = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:

            ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")
            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("configure terminal\n")
            time.sleep(1)

            ssh_shell.send(f"vlan {vlan_id}\n")
            time.sleep(1)

            ssh_shell.send(f"name {vlan_name}\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText(f"Successfully created VLAN {vlan_id} with name {vlan_name}.")

        except paramiko.AuthenticationException:

            self.clitext.setText("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as ssh_err:

            self.clitext.setText("SSH error:")
        except Exception as e:

            self.clitext.setText("An error occurred:")

    def show_interface_status(self):

        result = "Interface status ..."
        self.clitext.setText(result)

        pass

    def on_set_click(self):

        if self.hostname_lbl.toPlainText() == "":
            self.clitext.setText("Please enter the hostname")
        else:

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ip = self.IPadd_tb.toPlainText()
            username = self.uname_tb.toPlainText()
            password = self.password_tb.toPlainText()
            hostname = self.hostname_lbl.toPlainText()

            try:

                ssh_client.connect(hostname=ip, username=username, password=password, timeout=5)

                ssh_shell = ssh_client.invoke_shell()

                while not ssh_shell.recv_ready():
                    time.sleep(1)

                ssh_shell.send("enable\n")
                time.sleep(1)

                output = ssh_shell.recv(1000).decode()
                if "Password" in output:
                    ssh_shell.send(password + "\n")
                    time.sleep(1)

                ssh_shell.send("configure terminal\n")
                time.sleep(1)

                ssh_shell.send(f"hostname {hostname}\n")
                time.sleep(1)

                ssh_client.close()

                self.clitext.setText(f"Hostname set to {hostname}.")

            except paramiko.AuthenticationException:

                self.clitext.setText("Authentication failed. Please check your credentials.")
            except paramiko.SSHException as ssh_err:

                self.clitext.setText("SSH error")
            except Exception as e:

                self.clitext.setText("An error occurred")

    def on_ping_click(self):

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.ping_btn.setFont(font)
        self.ping_btn.setStyleSheet("background-color: rgb(100, 150, 100);")
        self.ping_btn.setObjectName("Disconnect")

        if self.add_ip_lbl.toPlainText() == "":
            self.clitext.setText("Please enter the IP address")
        else:

            ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.ping(self.add_ip_lbl.toPlainText())

    def on_click(self):

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.connect_btn.setFont(font)
        self.connect_btn.setStyleSheet("background-color: rgb(100, 150, 100);")
        self.connect_btn.setObjectName("Disconnect")

        if self.IPadd_tb.toPlainText() == "" or self.uname_tb.toPlainText() == "" or self.password_tb.toPlainText() == "":
            self.clitext.setText("Please enter the IP address, username and password")
        else:

            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(self.IPadd_tb.toPlainText(), username=self.uname_tb.toPlainText(),
                        password=self.password_tb.toPlainText())

            stdin, stdout, stderr = ssh.exec_command('conf t')

            output = stdout.read()

            self.clitext.setText(output.decode())

            ssh.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ANSCT"))
        self.IP_gb.setTitle(_translate("MainWindow", "IP Address"))
        self.ping_btn.setText(_translate("MainWindow", "Ping"))
        self.host_name_gb.setTitle(_translate("MainWindow", "Host Name"))
        self.set_btn.setText(_translate("MainWindow", "Set"))
        self.Configurevlan_gb.setTitle(_translate("MainWindow", "Configure Vlan"))
        self.label.setText(_translate("MainWindow", "Vlan "))
        self.label_2.setText(_translate("MainWindow", "Vlan Name"))
        self.create_btn.setText(_translate("MainWindow", "Create"))
        self.label_3.setText(_translate("MainWindow", "Switch Port"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.addport_btn.setText(_translate("MainWindow", "Add Port"))
        self.label_5.setText(_translate("MainWindow", "Vlan"))
        self.banner_gb.setTitle(_translate("MainWindow", "Banner"))
        self.set_btn_2.setText(_translate("MainWindow", "Set"))
        self.quickcommands_gb.setTitle(_translate("MainWindow", "Quick Commands"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.cli_btn.setText(_translate("MainWindow", "CLI"))
        self.showarp_btn.setText(_translate("MainWindow", "Show arp"))
        self.showinterface_btn.setText(_translate("MainWindow", "Show Interface"))
        self.showssh_btn.setText(_translate("MainWindow", "Show SSH"))
        self.showcdp_btn.setText(_translate("MainWindow", "Show CDP"))
        self.showrun_btn.setText(_translate("MainWindow", "Show Run"))
        self.mactable_btn.setText(_translate("MainWindow", "Mac Address Table"))
        self.uploadconfi_btn.setText(_translate("MainWindow", "Upload Configuration"))
        self.ip_add_lbl.setText(_translate("MainWindow", "IP Address"))
        self.uname_lbl.setText(_translate("MainWindow", "User Name"))
        self.password_lbl.setText(_translate("MainWindow", "Password"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))

    def connect_to_vm(self):

        ip_address = self.IPadd_tb.toPlainText()
        username = self.uname_tb.toPlainText()
        password = self.password_tb.toPlainText()

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:

            ssh_client.connect(hostname=ip_address, username=username, password=password, timeout=5)

            ssh_shell = ssh_client.invoke_shell()

            while not ssh_shell.recv_ready():
                time.sleep(1)

            ssh_shell.send("enable\n")

            time.sleep(1)

            output = ssh_shell.recv(1000).decode()
            if "Password" in output:
                ssh_shell.send(password + "\n")
                time.sleep(1)

            ssh_shell.send("configure terminal\n")
            time.sleep(1)

            ssh_client.close()

            self.clitext.setText('Successfully Cnfigured  a switch')
            self.connect_btn.setFont(font)
            self.connect_btn.setStyleSheet("background-color: rgb(100, 150, 100);")  # Changing color for demonstration
            self.connect_btn.setObjectName("Disconnect")

        except paramiko.AuthenticationException:
            self.clitext.setText("Authendication Error")
        except paramiko.SSHException as ssh_err:
            self.clitext.setText("SSH error")
        except Exception as e:
            self.clitext.setText("An error occurred")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

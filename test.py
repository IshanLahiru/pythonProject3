import sys


from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QFormLayout, \
    QHBoxLayout, QLayout, QGridLayout, QSpinBox, QTextEdit
from tkinter import font
import paramiko
import socket
import subprocess
import platform
import  os
import time

from PyQt6.uic.properties import QtGui, QtCore


class GridLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        upperGrid = QGridLayout()
        lowerGrid = QGridLayout()

        vbox1 = QHBoxLayout()

        group1_layout = QVBoxLayout()

        # ip
        ip_parent_box = QGroupBox()
        ip_group_box = QGroupBox("IP Address")
        self.add_ip_lbl = QLineEdit()
        self.add_ip_lbl.setMaximumSize(3000, 60)
        self.add_ip_lbl.setMinimumSize(30, 20)
        subgroup1_button = QPushButton("Ping")
        subgroup1_button.clicked.connect(self.perform_ping)
        ipFlayout = QFormLayout()
        ipFlayout.addRow(self.add_ip_lbl)
        ipFlayout.addRow(subgroup1_button)
        ip_group_box.setLayout(ipFlayout)
        llg = QVBoxLayout()
        llg.addWidget(ip_group_box)
        ip_parent_box.setLayout(llg)
        subgroup1_layout = QVBoxLayout()
        subgroup1_layout.addWidget(ip_parent_box)
        group1_layout.addLayout(subgroup1_layout)

        #host
        host_parent_box = QGroupBox()
        host_group_box = QGroupBox("Host Name")
        self.hostname_lbl = QLineEdit()
        self.hostname_lbl.setMaximumSize(3000, 60)
        self.hostname_lbl.setMinimumSize(30, 20)
        subgroup2_button = QPushButton("Set")
        hostFlayout = QFormLayout()
        hostFlayout.addRow(self.hostname_lbl)
        hostFlayout.addRow(subgroup2_button)
        host_group_box.setLayout(hostFlayout)
        llh = QVBoxLayout()
        llh.addWidget(host_group_box)
        host_parent_box.setLayout(llh)
        subgroup2_layout = QVBoxLayout()
        subgroup2_layout.addWidget(host_parent_box)
        group1_layout.addLayout(subgroup2_layout)

        # vlan
        vlan_parent_box = QGroupBox()
        vlan_group_box = QGroupBox("Configure Vlan")

        vlan_box = QGroupBox("Vlan")
        vlanFL = QFormLayout()
        self.vlan_lbl = QLineEdit()
        self.vlan_lbl.setMaximumSize(3000, 60)
        self.vlan_lbl.setMinimumSize(30, 20)
        vlanFL.addRow(self.vlan_lbl)
        vlan_box.setLayout(vlanFL)

        vlan_name_box = QGroupBox("Vlan Name")
        vlan_nameFL = QFormLayout()
        self.vlanname_lbl = QLineEdit()
        self.vlanname_lbl.setMaximumSize(3000, 60)
        self.vlanname_lbl.setMinimumSize(30, 20)
        vlan_nameFL.addRow(self.vlanname_lbl)
        vlan_name_box.setLayout(vlan_nameFL)

        subgroupc_button = QPushButton("Create")
        subgroupc_button.clicked.connect(self.show_interface_status)

        lli = QVBoxLayout()
        lli.addWidget(vlan_box)
        lli.addWidget(vlan_name_box)
        lli.addWidget(subgroupc_button)

        vlan_group_box.setLayout(lli)

        sgLayout2 = QVBoxLayout()
        sgLayout2.addWidget(vlan_group_box)
        vlan_parent_box.setLayout(sgLayout2)
        sgLayout3 = QVBoxLayout()
        sgLayout3.addWidget(vlan_parent_box)
        group1_layout.addLayout(sgLayout3)

        # configure ports

        port_group_box = QGroupBox()

        #box1 text input
        switch_port_group_box = QGroupBox("Switch Port")
        self.switchport_sbox = QSpinBox()
        self.switchport_sbox.setMaximumSize(3000, 60)
        self.switchport_sbox.setMinimumSize(30, 20)
        self.switchport_sbox.setMinimum(0)  # Set minimum value
        self.switchport_sbox.setMaximum(100)  # Set maximum value
        self.switchport_sbox.setSingleStep(1)  # Set step size
        self.switchport_sbox.setValue(50)
        ll1 = QVBoxLayout()
        ll1.addWidget(self.switchport_sbox)
        switch_port_group_box.setLayout(ll1)

        #box 2 text input
        another_port_group_box = QGroupBox("Port")
        self.port_sbox = QSpinBox()
        self.port_sbox.setMaximumSize(3000, 60)
        self.port_sbox.setMinimumSize(30, 20)
        self.port_sbox.setMinimum(0)  # Set minimum value
        self.port_sbox.setMaximum(100)  # Set maximum value
        self.port_sbox.setSingleStep(1)  # Set step size
        self.port_sbox.setValue(50)
        ll2 = QVBoxLayout()
        ll2.addWidget(self.port_sbox)
        another_port_group_box.setLayout(ll2)

        #box3 text input
        vlan_group_box = QGroupBox("Vlan")
        self.vlan_lbl_2 = QLineEdit()
        self.vlan_lbl_2.setMaximumSize(3000, 60)
        self.vlan_lbl_2.setMinimumSize(30, 20)
        ll3 = QVBoxLayout()
        ll3.addWidget(self.vlan_lbl_2)
        vlan_group_box.setLayout(ll3)

        #create form layout
        portFlayout = QFormLayout()
        switch_groupe_button = QPushButton("Add Port")
        portFlayout.addRow(switch_port_group_box)
        portFlayout.addRow(another_port_group_box)
        portFlayout.addRow(vlan_group_box)
        portFlayout.addRow(switch_groupe_button)

        port_group_box.setLayout(portFlayout)

        #add to the parent box
        switch_Group_Layout = QVBoxLayout()
        switch_Group_Layout.addWidget(port_group_box)

        group1_layout.addLayout(switch_Group_Layout)

        # this is the Groupe 2
        group2_layout = QVBoxLayout()

        center_section_grid = QGridLayout()
        #top bar
        center_top_bar = QVBoxLayout()
        center_container = QVBoxLayout()

        center_top_bar_container = QGroupBox()  #

        ip_address = QGroupBox("IP Address")
        self.IPadd_tb = QLineEdit()
        cont1 = QVBoxLayout()
        cont1.addWidget(self.IPadd_tb)
        ip_address.setLayout(cont1)

        user_name = QGroupBox("User Name")
        self.uname_tb = QLineEdit()
        cont2 = QVBoxLayout()
        cont2.addWidget(self.uname_tb)
        user_name.setLayout(cont2)

        password = QGroupBox("Password")
        self.password_tb = QLineEdit()
        cont3 = QVBoxLayout()
        cont3.addWidget(self.password_tb)
        password.setLayout(cont3)

        btn_grp = QGroupBox()
        btn_gp_basic_ = QPushButton("Connect")
        btn_gp_basic_.clicked.connect(self.connect_to_vm)
        cont4 = QVBoxLayout()
        cont4.addWidget(btn_gp_basic_)
        btn_grp.setLayout(cont4)

        center_top_bar_components_array = QHBoxLayout()

        center_top_bar_components_array.addWidget(ip_address)
        center_top_bar_components_array.addWidget(user_name)
        center_top_bar_components_array.addWidget(password)
        center_top_bar_components_array.addWidget(btn_grp)

        center_top_bar_container.setLayout(center_top_bar_components_array)

        center_stuff_container = QGroupBox()
        self.clitext = QTextEdit()
        mjkl = QGridLayout()
        mjkl.addWidget(self.clitext)
        center_stuff_container.setLayout(mjkl)
        #implement this


        center_top_bar.addWidget(center_top_bar_container)
        center_container.addWidget(center_stuff_container)

        center_section_grid.addLayout(center_top_bar, 0, 0)
        center_section_grid.addLayout(center_container, 1, 0)
        center_section_grid.setRowStretch(0, 1)
        center_section_grid.setRowStretch(1, 8)
        group2_layout.addLayout(center_section_grid)
        vbox1.addLayout(group2_layout)

        upperGrid.addLayout(group1_layout, 0, 0)
        upperGrid.addLayout(vbox1, 0, 1)

        upperGrid.setColumnStretch(0, 1)
        upperGrid.setColumnStretch(1, 3)

        # bottom bar
        bottom_bar_container = QGroupBox("bottom bar")

        bottom_bar_array = QHBoxLayout()

        banner_pallet_parent = QGroupBox()
        banner_Pallet = QGroupBox("Banner")
        self.banner_lbl = QLineEdit()
        banner_pallet_btn = QPushButton("Set")
        contft = QVBoxLayout()
        contft.addWidget(self.banner_lbl)
        contft.addWidget(banner_pallet_btn)
        banner_Pallet.setLayout(contft)
        parantMapper = QHBoxLayout()
        parantMapper.addWidget(banner_Pallet)
        banner_pallet_parent.setLayout(parantMapper)
        banner_pallet_parent.setMaximumSize(400, 200)
        bottom_bar_array.addWidget(banner_pallet_parent)

        #other things
        quick_command_pallet_parent = QGroupBox()
        quick_command_Pallet = QGroupBox("Quick Commands")

        button_container = QGridLayout()

        #button set
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.reset)
        cli_btn = QPushButton("CLI")
        cli_btn.clicked.connect(self.cliOpen)
        show_arp_btn = QPushButton("Show ARP")
        show_arp_btn.clicked.connect(self.show_arp)
        Show_cdp_btn = QPushButton("Show CDP")
        Show_cdp_btn.clicked.connect(self.show_cdp)
        show_ssh_btn = QPushButton("Show SSH")
        show_ssh_btn.clicked.connect(self.show_ssh)
        show_interface_btn = QPushButton("Show Interface")
        show_interface_btn.clicked.connect(self.show_interface)
        show_run_btn = QPushButton("Show Run")
        show_run_btn.clicked.connect(self.show_run)
        mac_address_btn = QPushButton("MAC Address Table")
        mac_address_btn.clicked.connect(self.show_mac_table)

        button_container.addWidget(refresh_btn, 0, 0)
        button_container.addWidget(cli_btn, 0, 1)
        button_container.addWidget(show_arp_btn, 0, 2)
        button_container.addWidget(Show_cdp_btn, 1, 0)
        button_container.addWidget(show_ssh_btn, 1, 1)
        button_container.addWidget(show_interface_btn, 1, 2)
        button_container.addWidget(show_run_btn, 2, 0)
        button_container.addWidget(mac_address_btn, 2, 1)

        quick_command_Pallet.setLayout(button_container)

        ghj = QVBoxLayout()
        ghj.addWidget(quick_command_Pallet)

        quick_command_pallet_parent.setLayout(ghj)
        bottom_bar_array.addWidget(quick_command_pallet_parent)

        # config Buttons
        config_btn_set_parent = QGroupBox()
        config_btn_set = QGroupBox()

        button_container_box = QVBoxLayout()

        # buttons
        upload_config_btn = QPushButton("Upload Configuration")
        upload_config_btn.clicked.connect(self.upload_configuration)
        upload_config_btn.setMinimumSize(50, 60)
        save_config_btn = QPushButton("Save Configuration")
        save_config_btn.clicked.connect(self.save_configuration)
        save_config_btn.setMinimumSize(50, 60)

        button_container_box.addWidget(upload_config_btn)
        button_container_box.addWidget(save_config_btn)

        config_btn_set.setLayout(button_container_box)
        nbm = QHBoxLayout()
        nbm.addWidget(config_btn_set)
        config_btn_set_parent.setLayout(nbm)
        config_btn_set_parent.setMaximumSize(400, 200)
        bottom_bar_array.addWidget(config_btn_set_parent)

        bottom_bar_container.setLayout(bottom_bar_array)

        b_grid = QHBoxLayout()
        b_grid.addWidget(bottom_bar_container)

        lowerGrid.addLayout(b_grid, 0, 0)
        lowerGrid.setColumnStretch(0, 4)

        layout.addLayout(upperGrid, 0, 0)
        layout.addLayout(lowerGrid, 1, 0)
        # layout.addLayout(bottom_grid, 0, 1)

        layout.setRowStretch(0, 2)
        layout.setRowStretch(1, 1)

        self.setWindowTitle('Grid Layout Demo')
        self.setGeometry(100, 100, 1000, 1000)
        self.show()

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
        self.clitext.clear()
        self.IPadd_tb.clear()
        self.uname_tb.clear()
        self.password_tb.clear()
        self.hostname_lbl.clear()
        self.add_ip_lbl.clear()
        self.vlan_lbl.clear()
        self.vlanname_lbl.clear()
        self.switchport_sbox.clear()
        self.port_sbox.clear()
        self.vlan_lbl_2.clear()
        self.banner_lbl.clear()

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
    app = QApplication(sys.argv)
    demo = GridLayoutDemo()
    sys.exit(app.exec())

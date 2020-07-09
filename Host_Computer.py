# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import array
import serial#串口
import threading#多线程
import pyqtgraph as pg #绘图包
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QApplication, QWidget
from PyQt5.QtCore import QTimer,Qt,QPoint
from PyQt5.QtGui import QPainter, QColor, QPen,QPixmap
from designer_Gui  import Ui_Win
No_Display=55#中线边线不显示值
LCDH=60#下位机OLED显示行数
LCDW=94#下位机OLED显示列数
receive_meg=" "#错误信息
temp_data=[]#临时数据缓存
image_buff=[]#图像缓存
mid_buff=[]#中线缓存
ls_buff=[]#左边线缓存
rs_buff=[]#右边线缓存
Speed_p=[]#电机P缓存
Speed_i=[]#电机I缓存
Speed_d=[]#电机D缓存
SD_PWM=[]#舵机PWM缓存
SD_P=[]#舵机P缓存
SD_D=[]#舵机P缓存
PWM_MAX=850#pwm限幅
PWM_MIN=650#pwm限幅
Speed_p.append(0)
Speed_i.append(0)
Speed_d.append(0)
SD_PWM.append(750)
SD_P.append(0)
SD_D.append(0)
for i in range(2):
    mid_buff.append([])
    ls_buff.append([])
    rs_buff.append([])
    for j in range(LCDH):
        if(i==0):
            mid_buff[i].append(LCDW/2+1)
            ls_buff[i].append(0)
            rs_buff[i].append(LCDW-1)
        else:
            mid_buff[i].append(No_Display)
            ls_buff[i].append(No_Display)
            rs_buff[i].append(No_Display)
for i in range(LCDH):
    image_buff.append([])
    for j in range(LCDW):
        image_buff[i].append(0)
#      停车         车启动      单片机复位     上传图像      电机PID          舵机PD
car_cmd={"CAR_STOP":"A","CAR_GO":"B","RESET":"C","IMAGE":"D","MOTOR_PID":"E","SD5_PD":"F"} #上位机指令集
class Pyqt5_Serial(QtWidgets.QMainWindow,Ui_Win,threading.Thread):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("智能车调试助手")
        self.ser = serial.Serial()
        self.port_check()
        self.data_num_received = 0
        self.data_num_sended = 0
        self.pra_pid=pg.PlotWidget()#实例化一个绘图部件
        self.horizontalLayout_2.addWidget(self.pra_pid)#显示在指定层中
        self.pra_pwm=pg.PlotWidget()#实例化一个绘图部件
        self.horizontalLayout_6.addWidget(self.pra_pwm)#显示在指定层中
        self.plot_mp = self.pra_pid.plot()#电机P
        self.plot_mp.setPen((0,0,255))#蓝色
        self.plot_mi = self.pra_pid.plot()#电机I
        self.plot_mi.setPen((0,238,0))#绿色
        self.plot_md = self.pra_pid.plot()#电机D
        self.plot_md.setPen((255,106,106))#红色
        self.plot_sp = self.pra_pid.plot()#舵机P
        self.plot_sp.setPen((255,255,255))#白色
        self.plot_sd = self.pra_pid.plot()#舵机D
        self.plot_sd.setPen((255,255,0))#黄色
        self.plot_pwm=self.pra_pwm.plot()#舵机PWM
        self.plot_pwm.setPen((0,0,255))#白色
        self.graphinit()#数据线图初始化
        self.pix_img=QPixmap(570,366)  # 实例化一个QPixmap()图片对象作为画布
        self.pix_img.fill(Qt.green)  #给图片对象填充颜色
        self.thread_graph()
    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)
        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)
        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)
        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)
        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)
        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)
        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)
        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)
        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)
        #上位机指令按钮
        self.hc_help_button.clicked.connect(self.hc_help_mes)
        #通信协议按钮
        self.am_button.clicked.connect(self.am_help_mes)
    def thread_graph(self):
        th_grap=threading.Thread(target=self.graphdata)#实例化一个画数据线程
        th_grap.start()#开始线程
    def thread_draw(self):
        th_draw=threading.Thread(target=self.update)#实例化一个画图像线程
        th_draw.start()#开始线程
    def graphinit(self):
        self.pra_pid.showGrid(x=True, y=True, alpha=0.5)
        self.pra_pid.setYRange(max=30,min=0)
        self.pra_pid.setXRange(max=30,min=0)
        self.pra_pwm.showGrid(x=True, y=True, alpha=0.5)
        self.pra_pwm.setYRange(max=900,min=600)
        self.pra_pwm.setXRange(max=30,min=0)
    def graph_one_data(self,pw,box,buff):
        len_buff=len(buff)
        if len_buff>30: 
            pw.setXRange(max=len_buff+1,min=len_buff-40)
        box.setData(buff)
    def graphdata(self):
        if self.MP.isChecked():
            self.graph_one_data(self.pra_pid,self.plot_mp,Speed_p)
        if self.MI.isChecked():
            self.graph_one_data(self.pra_pid,self.plot_mi,Speed_i)
        if self.MD.isChecked():
            self.graph_one_data(self.pra_pid,self.plot_md,Speed_d)
        if self.SP.isChecked():
            self.graph_one_data(self.pra_pid,self.plot_sp,SD_P)
        if self.SD.isChecked():
            self.graph_one_data(self.pra_pid,self.plot_sd,SD_D)
        if self.SW.isChecked():
            self.graph_one_data(self.pra_pwm,self.plot_pwm,SD_PWM)
        # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.uart_statusBox.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.uart_statusBox.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            num=0#发送数据计数
            input_s=""#发送数据缓存
            #发送指令  #如需添加指令，按下列格式添加
            if self.MP.isChecked() or self.MI.isChecked() or self.MD.isChecked():
                input_s +=car_cmd["MOTOR_PID"]
                #num = self.ser.write((car_cmd["MOTOR_PID"]+'\r\n').encode('utf-8')) #添加传送电机PID命令
            if self.SW.isChecked() or self.SP.isChecked() or self.SD.isChecked():
                input_s +=car_cmd["SD5_PD"]
                #num = self.ser.write((car_cmd["SD5_PD"]+'\r\n').encode('utf-8')) #添加传送舵机PD命令
            if self.Pixle.isChecked():
                input_s +=car_cmd["IMAGE"]
                #num=self.ser.write((car_cmd["IMAGE"]+'\r\n').encode('utf-8')) #添加传输图像命令
            
            #发送输入框内的数据
            input_s += self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    # ascii发送
                    input_s = (input_s).encode('utf-8')
                    num += self.ser.write(input_s)
                    self.data_num_sended += num
                    self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    def data_am(self,num,data):
        model="{}剩余:{}"
        add_i=0#计数器
        add_j=0#计数器
        #if(len(temp_data)>10000): temp_data.clear()#清除错误缓存
        if 0x0a in data and 0x0d in data:#包含帧尾
            if 0x49 in temp_data:#"I" ①图像部分
                temp=temp_data.index(0x49)
                if(temp_data[temp+1]==0x45):#"E" 图像
                    temp=temp#定位到有效数据
                    end=temp_data.index(0x0d)#定位到"\r"
                    for byte in temp_data[temp+2:end]:
                        if byte==0x01 or byte==0x00:#检验接收内容是否正确
                            image_buff[add_i][add_j]=byte
                        else:
                            receive_meg="error"#接收错误
                            #temp_data.clear()#清空缓存
                            add_i,add_j=0,0
                            break
                        add_j+=1
                        if(add_j==LCDW): 
                            add_i+=1#换行
                            add_j=0#换行
                        if(add_i==LCDH): 
                            add_i,add_j=0,0
                            end+=2
                            del temp_data[temp:end]#删除已经显示图像数据
                            receive_meg="finish"#接收完成
                            #print(model.format("图像",temp_data))#测试
                            self.thread_draw()#更新图像
                            break
                    #接收图像数据
        if 0x0a in temp_data[10:] and 0x0d in temp_data[10:]:#包含帧尾
            if 0x49 in temp_data:#"I" ①图像部分
                temp=temp_data.index(0x49)#重定向
                if(temp_data[temp+1]==0x4D):#"M" 中线
                                                    #有效帧  #有效帧尾
                    self.temp_image_handler(mid_buff,temp+2)#接收中线数据
                    #print(model.format("中线",temp_data))#测试
                    self.thread_draw()#更新图像
        if 0x0a in temp_data[10:] and 0x0d in temp_data[10:]:#包含帧尾
            if 0x49 in temp_data:#"I" ①图像部分
                temp=temp_data.index(0x49)
                if(temp_data[temp+1]==0x4C):#"L"左边线
                                              #有效帧    #有效帧尾
                    self.temp_image_handler(ls_buff,temp+2)#接收左边线数据
                    #print(model.format("左线",temp_data))#测试
                    self.thread_draw()#更新图像
        if 0x0a in temp_data[10:] and 0x0d in temp_data[10:]:#包含帧尾
            if 0x49 in temp_data:#"I" ①图像部分
                temp=temp_data.index(0x49)#重定向
                if(temp_data[temp+1]==0x52):#"R"右边线
                                              #有效帧    #有效帧尾
                    self.temp_image_handler(rs_buff,temp+2)#接收右边线数据
                    #print(model.format("右线",temp_data))#测试
                    self.thread_draw()#更新图像
            if 0X4D in temp_data:#"M" ②电机数据部分
                temp=temp_data.index(0X4D)#重定向
                if(temp_data[temp+1]==0X50):#"P" 
                    Speed_p.append(float((temp_data[temp+2]<<8)+temp_data[temp+3])/1000)#p
                    Speed_i.append(float((temp_data[temp+6]<<8)+temp_data[temp+7])/1000)#i
                    Speed_d.append(float((temp_data[temp+10]<<8)+temp_data[temp+11])/1000)#d
                    end=temp+11+3
                    del temp_data[temp:end]#删除已经显示图像数据
                    self.graphdata()
                    receive_meg="finish"#接收完成
            if 0X53 in temp_data:#"S" ③舵机数据部分
                temp=temp_data.index(0X53)
                if(temp_data[temp+1]==0X57):#"W" PWM
                    SD_PWM.append(float((temp_data[temp+2]<<8)+temp_data[temp+3]))#pwm
                    SD_P.append(float((temp_data[temp+6]<<8)+temp_data[temp+7])/1000)#p
                    SD_D.append(float((temp_data[temp+10]<<8)+temp_data[temp+11])/1000)#d
                    end=temp+11+3
                    del temp_data[temp:end]#删除已经显示图像数据
                    self.graphdata()
                    receive_meg="finish"#接收完成

            return "Object"
        else: return "None"   

    def temp_image_handler(self,buff,star):
        i,j,end=0,0,0
        for byte in temp_data:#定位到有效数据
            end+=1
            if(byte==0X0D):
                if(temp_data[end]==0x0A):#防止出现误判
                    break;
        try:
            read=temp_data[end]#试读判断是否到最后一位，报错说明到最后一位也没找到，不执行操作
            long=int(len(temp_data[star:end-1])/2)
            for byte in temp_data[star:end-1]:#定位到有效数据
                buff[i][j]=byte
                j+=1
                if(j==long):
                    i+=1
                    j=0
            for num in range(long,LCDH):
                buff[1][num]=No_Display #设置剩下的Y值越界值，保证之前的图像不会重复显示
            #print(temp_data[star-2:end+1])#测试
            del temp_data[star-2:end+1]#删除已经显示图像数据
            
            receive_meg="finish"#接收完成
        except:
            
            #del temp_data[star-2:end+1]#删除误帧
            receive_meg="error"#接收错误
        
    def check_box(self):#检查是否有图像数据勾选
        return (self.MP.isChecked() or self.MI.isChecked() or self.MD.isChecked()or self.SW.isChecked() or self.SP.isChecked() or self.SD.isChecked()or self.Pixle.isChecked()or self.midline.isChecked()or self.sideline.isChecked())
    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        ##接收协议数据##
        if (num>0) and self.check_box() :
           try:
               data=self.ser.read(num)#data为bytes
               for b in data:#保存数据为int
                   temp_data.append(b)
               self.data_am(num,data)
           except:
               pass
        ##接收协议数据##
        if num > 0 and not self.check_box():
            data = self.ser.read(num)
            num = len(data)
            # hex显示
            if self.hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                #接收方式选择(中英文不能混合接收，否则会乱码)
                try:
                    self.s2__receive_text.insertPlainText(data.decode('GBK'))
                except:
                    self.s2__receive_text.insertPlainText(data.decode('ISO-8859-1'))
                
                
        if num > 0:
            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))
        if num > 0 and not self.check_box():
            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass
    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")
    def receive_data_clear(self):
        self.s2__receive_text.setText("")
        #指令集按键
    def hc_help_mes(self):
        QMessageBox.information(self, "上位机指令集", "上传图像:D   \n上传电机PID:E\n上传舵机PD:F")
        #通信协议按键
    def am_help_mes(self):
        QMessageBox.information(self, "通信协议", '''\
//---------------------------通信协议------------------------------------//\
//Image:"IE"+Pixle[0[1]+……+Pixle[LCDH-1[LCDW-1]+"\r\n"//图像协议\
//Iamge_MIDdle:"IM"+Iamge_MIDdle[0][1]……+Iamge_MIDdle[1][IMH-1]+"\r\n"//中线协议,发送(x,y)；0为x，1为y\
//Iamge_LIFE_SIDE:"IL"+Iamge_LIFE_SIDE[0][1]+……+Iamge_LIFE_SIDE[1][IL-1]+"\r\n"//左边线协议,发送(x,y)\
//Iamge_RIGHT_SIDE:"IR"+Iamge_RIGHT_SIDE[0][1]+……+Iamge_RIGHT_SIDE[1][IR-1]+"\r\n"//右边线协议,发送(x,y)\
\
//Speed_PID:"MP"+(int16)Speed_P*1000+MI"+(int16)Speed_I*1000+"MD"\
//              +(int16)Speed_D*1000+"\r\n"//电机PID数据协议\

//SD5_PD:"SW"+(int16)SD5_Out+"SP"+(int16)Speed_P*1000+"SD"\
//            +(int16)Speed_D*1000+"\r\n"//舵机PD数据协议\
//---------------------------通信协议------------------------------------//'''
)




    def paintEvent(self, QPaintEvent):
        QP_Win=QPainter(self)              #实例化一个画布。用窗口作为画布
        QP_img=QPainter(self.pix_img)      #实例化一个画布。用图片对象作为画布
                 #勾选图像显示            #勾选中线显示          #勾选边线显示
        if self.Pixle.isChecked()or self.midline.isChecked()or self.sideline.isChecked():
            if self.Pixle.isChecked():   
                self.drawPoints(QP_img)         #画二值化图像
            else:
                self.draw_clear()               #清除图像
                self.drawPoints(QP_img)         
            if self.midline.isChecked(): 
                self.draw_midorsidline(QP_img,mid_buff,Qt.blue,len(mid_buff[0]))         #画中线
            if self.sideline.isChecked():
                self.draw_midorsidline(QP_img,ls_buff,Qt.yellow,len(ls_buff[0]))         #画左边线
                self.draw_midorsidline(QP_img,rs_buff,Qt.yellow,len(rs_buff[0]))         #画右边线
            QP_Win.drawPixmap(20,50, self.pix_img) #在画布上加载图片

    def drawPoints(self,QPainter): #画二值化图像
        pen = QPen(Qt.black, 6, Qt.SolidLine)
        QPainter.setPen(pen)
        if not image_buff==None:#缓存不为空
            for i in range(LCDH):
                for j in range(LCDW):
                    if image_buff[i][j]==0:# 0表示黑，1表示白
                        pen.setColor(Qt.black)
                        QPainter.setPen(pen)
                    else: 
                        pen.setColor(Qt.white)
                        QPainter.setPen(pen)
                    QPainter.drawPoint(j*6+6,i*6+6)
    def draw_midorsidline(self,QPainter,Buff,Color,Len):#画中线或者边线
        pen = QPen(Color, 6, Qt.SolidLine)
        QPainter.setPen(pen)
        if not Buff==None:#缓存不为空
            for i in range(Len):
                    QPainter.drawPoint(Buff[0][i]*6+6,Buff[1][i]*6+6*10)#转化为图像坐标画点
    def draw_clear(self):
        for i in range(LCDH):
            for j in range(LCDW):
                image_buff[i][j]=0







def show_w():
    '显示窗口'
 
    app = QApplication(sys.argv) # 所有的PyQt5应用必须创建一个应用（Application）对象。
    # sys.argv参数是一个来自命令行的参数列表。
    w = Pyqt5_Serial() 
    w.show() # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。

    sys.exit(app.exec_()) # 应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，
    # 并且转发他们到widget应用上处理。如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
if __name__ == '__main__':
 
    show_w()



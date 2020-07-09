# 智能车调试上位机
今年打算参加恩智浦智能车的比赛，为了后续调试的方便，自己写了一个上位机图像显示的程序，主要功能是将智能车采集和处理后的二值化图像、边线数据、中线数据、电机pid数据、舵机pd数据通过串口传输到电脑中，然后将数据以图像或者波形的形式显示出来，方便调试。
# 通信协议
图像协议:"IE"+Pixle[0[1]+……+Pixle[LCDH-1[LCDW-1]+"\r\n"
中线协议,发送(x,y)；0为x，1为y:"IM"+Iamge_MIDdle[0][1]……+Iamge_MIDdle[1][IMH-1]+"\r\n"
左边线协议,发送(x,y):"IL"+Iamge_LIFE_SIDE[0][1]+……+Iamge_LIFE_SIDE[1][IL-1]+"\r\n"
右边线协议,发送(x,y):"IR"+Iamge_RIGHT_SIDE[0][1]+……+Iamge_RIGHT_SIDE[1][IR-1]+"\r\n"
电机PID数据协议:"MP"+(int16)Speed_P*1000+MI"+(int16)Speed_I*1000+"MD"
//              +(int16)Speed_D*1000+"\r\n"//
//舵机PD数据协议:"SW"+(int16)SD5_Out+"SP"+(int16)Speed_P*1000+"SD"
//            +(int16)Speed_D*1000+"\r\n"//

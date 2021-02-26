import time
from machine import Pin, SPI
spi=SPI(1, baudrate=20000000, polarity=0, phase=0)
from st7735_lut import ST7735
#lcd = ILI9341(240, 320, spi,dc=Pin(25),cs=Pin(32),rst=Pin(33))#竖屏初始化
lcd = ST7735(160, 80, spi,dc=Pin(0),cs=Pin(15),rst=Pin(2),rot=1,bgr=0)#横屏初始化参数rot，交换红蓝位置用bgr=1
bl=Pin(4,Pin.OUT)
bl.value(1)
lcd.font_load("GB2312-24.fon")
#加载的字库是中文，可以选12，16，24，32四种中文
   
for count in range(20):
    lcd.cls(lcd.rgb(0,0,0))
    lcd.font_set(0x11,0,1,0)
    #字体(第一位1-4对应标准，方头，不等宽标准，不等宽方头，第二位1-4对应12，16，24，32高度)，旋转，放大倍数，反白显示
    lcd.text("Micropython中文甒甒%d"%count,0,0,lcd.rgb(255,0,0))
    lcd.font_set(0x12,0,1,1)
    lcd.text("micro拷贝甓甓",0,16,lcd.rgb(0,255,0))
    lcd.font_set(0x13,0,1,0)
    lcd.text("字符Mpy%3.3d"%count,0,32,lcd.rgb(255,255,255))
    #lcd.rgb()是方便设置显示颜色的小功能
    lcd.font_set(0x44,0,1,0)
    lcd.text("中文Mpy%3.3d"%count,0,48,lcd.rgb(0,0,255))
    lcd.show()

lcd.font_free()

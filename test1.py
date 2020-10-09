# -*- coding:utf-8 -*-
import qrcode,time
from PIL import Image
import matplotlib.pyplot as plt


# 方法3  生成带有图标的二维码
def qr_code_3():
    # 实例化QRCode生成qr对象
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data("  鑫怡   ")# 添加数据
    qr.make(fit=True)# 填充数据
    # 生成图片
    # img = qr.make_image()
    img = qr.make_image(fill_color="lightgreen", back_color="gray")
    img = img.convert("RGBA")
    # 添加logo，打开logo照片
    icon = Image.open("26c880e35d1ec1c6d6c6d54af9799ecf_t.gif").convert("RGBA")
    # 获取图片的宽和搞
    img_w, img_h = img.size
    # 参数设置logo的大小
    factor = 3
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到画图的x，y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    '''
    img.paste(path,where,mask=None)
    其中，img为image对象；path为所添加图片；where为tuple,如：(x,y)，表示图片所在二维码的横纵坐标
    '''
    # 黏贴logo照
    img.paste(icon, (w, h), icon)
    img.save("我的二维码.png")
    # img.show()# 自动打开图片
    # 终端显示图片
    plt.imshow(img)
    plt.show()

if __name__=='__main__':
    qr_code_3()

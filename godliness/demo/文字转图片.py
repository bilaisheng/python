
#载入必要的模块
import pygame

#pygame初始化
pygame.init()

text = u"文字转图片"

#设置字体和字号
font = pygame.font.SysFont('Microsoft YaHei', 64)

#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))

#保存图片
pygame.image.save(ftext, "image.jpg")#图片保存地址
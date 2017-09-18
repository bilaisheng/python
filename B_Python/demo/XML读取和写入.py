from xml.dom import minidom

# 生成XML文件方式
def generateXml():
    impl = minidom.getDOMImplementation()

    # 创建一个xml dom
    # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
    doc = impl.createDocument(None, None, None)

    # 创建根元素
    rootElement = doc.createElement('Pythons')

    # 为根元素添加10个子元素
    for pythonId in range(10):
        # 创建子元素
        childElement = doc.createElement('python')
        # 为子元素添加id属性
        childElement.setAttribute('id', str(pythonId))

        # 将子元素追加到根元素中
        rootElement.appendChild(childElement)
        print(childElement.firstChild.data)

    # 将拼接好的根元素追加到dom对象
        doc.appendChild(rootElement)

    # 打开test.xml文件 准备写入
    f = open('test.xml', 'a')
    # 写入文件
    doc.writexml(f, addindent='  ', newl='\n')
    # 关闭
    f.close()

# 执行生成xml方法
generateXml()
# -----------------------------------
#
# from xml.dom.minidom import parse
#
# # 获取 python节点下得所有id属性
# def getTagId():
#
#     # 获取test.xml文档对象
#     doc = parse("test.xml")
#
#     for node in doc.getElementsByTagName("python"):
#         # 获取标签ID属性
#         value_str = node.getAttribute("id")
#         # 打印输出
#         print(value_str)
#
# # 获取属性ID
# getTagId()
# Python内置函数exec()可以用来执行Python代码
# 或内置函数compile()编译的代码对象


# exec程序中可写入python语法格式的代码，并直接输出。
exec('print("Hello World!")')

# compile(source, filename, mode[, flags[, dont_inherit]])
# 中文说明：将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
# 参数source：字符串或者AST（Abstract Syntax Trees）对象。
# 参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# 参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
# 参数flag和dont_inherit：这两个参数暂不介绍，可选参数。

code = "for i in range(0, 10): print(i)"

cmpcode = compile(code, '', 'exec')

exec(cmpcode)
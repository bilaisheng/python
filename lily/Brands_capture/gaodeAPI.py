# import win32com.server.util, win32com.client
import execjs
# class win32Doc:
#      _public_methods_ = ['write']
#      def write(self, s):
#              print(s)
#
# doc = win32Doc()
# jsengine = win32com.client.Dispatch('MSScriptControl.ScriptControl')
# jsengine.language = 'JavaScript'
# jsengine.allowUI = False
# jsengine.addObject('document', win32com.server.util.wrap(doc))
# jsengine.eval('document.write("hello, world")')

source ='document.write("hello, world")'
print(execjs.compile(sources).call())
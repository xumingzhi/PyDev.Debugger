import traceback
import sys
try:
    import StringIO
except:
    import io as StringIO #Python 3.0
    
    
class Log:
    
    def __init__(self):
        self._contents = []
        
    def add_content(self, *content):
        self._contents.append(' '.join(content))
        
    def add_exception(self):
        s = StringIO.StringIO()
        exc_info = sys.exc_info()
        traceback.print_exception(exc_info[0], exc_info[1], exc_info[2], limit=None, file=s)
        self._contents.append(s.getvalue())

        
    def GetContents(self):
        return '\n'.join(self._contents)
    
    def clear_log(self):
        del self._contents[:]
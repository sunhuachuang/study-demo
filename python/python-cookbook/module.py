#! /usr/bin/python3
import sys
import imp
import pkgutil
import importlib
import urllib.request

# 15 分发包 setup.py
'''
projectname/
    README.txt
    Doc/
        documentation.txt
    projectname/
        __init__.py
        foo.py
        bar.py
        utils/
            __init__.py
            spam.py
            grok.py
    examples/
        helloworld.py
'''
from distutils.core import setup
setup(name='projectname',
      version='1.0',
      author='Your Name',
      author_email='you@youraddress.com',
      url='http://www.you.com/projectname',
      packages=['projectname', 'projectname.utils'],
      )

# MANIFEST.in
'''
include *.txt
recursive-include examples *
recursive-include Doc *
'''


# 14 创建新的python环境　pyvenv

# 13 安装私有的包 ~/.local/lib/python pip install --user packagename

# 12 导入模块的同时修改模块
from collections import defaultdict

_post_import_hooks = defaultdict(list)


class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self)


class PostImportLoader:
    def __init__(self, finder):
        self._finder = finder

    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        for func in _post_import_hooks[fullname]:
            func(module)
        self._finder._skip.remove(fullname)
        return module


def when_imported(fullname):
    def decorate(func):
        if fullname in sys.modules:
            func(sys.modules[fullname])
        else:
            _post_import_hooks[fullname].append(func)
        return func
    return decorate


sys.meta_path.insert(0, PostImportFinder())

#*11 远程加载模块


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


# 10 通过字符串名导入模块 importlib.import_module()
math = importlib.import_module('math')
print(math.sin(2))

exit(0)
# 9 将python包导入到环境变量中 1. env PYTHONPATH 2. .pth文件

# 8 读取位于包中的数据文件 pkgutil
data = pkgutil.get_data(__package__, 'some.data')

# 7 运行目录或者压缩文件 __main__.py

# 6 重新加载模块 imp.reload()
imp.reload(sys)

exit(0)
# 5 利用命名空间导入目录分离的代码 sys.path.extend() 没有__init__.py文件
sys.path.extend(['tmp/mymodule/package/foo-package',
                 'tmp/mymodule/package/bar-package'])
import spam.bar
import spam.foo

exit(0)
# 4 将模块分割成多个文件 使用逻辑模块方法合并
import tmp.mymodule as mymodule

a = mymodule.A()
a.foo()  # this in a -> A -> foo

b = mymodule.B()
b.foo()  # this in b -> B -> foo

exit(0)
# 3 使用相对路径名导入包中子模块
# from . import test 当前目录
# from ..B import test　../B 上级B目录 必须在该调用者的包中

exit(0)
# 2 控制模块导入的内容 __all__ = [] _开头
from tmp.test import *
from tmp import test

foo()
no()  # NameError: name 'no' is not defined
# _self() #NameError: name '_self' is not defined
# __private() #NameError: name '__private' is not defined
test.no()  # ok
test._self()  # ok
test.__private()  # ok

# 1 构建模块的层次包 __init__.py文件

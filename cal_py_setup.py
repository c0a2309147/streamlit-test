from distutils.core import setup, Extension

setup(name = 'calModule', version = '1.0.0',  \
   ext_modules = [Extension('calModule', ['cal_py.c'])])
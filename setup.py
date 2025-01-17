from setuptools import setup, Extension
import pybind11

module = Extension(
    'Pybind11Module',  # ім'я модуля, яке буде імпортуватися в Python
    sources=['UserFunctional.cpp', 'DatabaseManager.cpp', 'Pybind11Module.cpp', 'BankCard.cpp', 'BankTransaction.cpp'],  # список файлів для компіляції
    include_dirs=[pybind11.get_include(), 'C://Users//Olexandro//source//repos//dbtest//dbtest//SQLite', ],  # шляхи до заголовочних файлів pybind11
    library_dirs=['C://Users//Olexandro//source//repos//dbtest//dbtest//SQLite'],  # Шлях до sqlite3.lib
    libraries=['sqlite3'],
    language='c++',
)

setup(
    name='Pybind11Module',
    version='1.0',
    ext_modules=[module],
)

from setuptools import setup, find_packages
with open("README.md", "r",encoding='utf-8') as fh:
  long_description = fh.read()
setup(
    name = 'lxkjdatacleaner',
    version = '0.0.6',
    keywords='dataclean',
    description = 'a library for data clean',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT License',
    url = 'https://github.com/qihao123/lxdatacleaner',
    author = 'Hao Qi',
    author_email = '1047355811@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)
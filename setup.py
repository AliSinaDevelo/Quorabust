from setuptools import setup, find_packages

setup(
    name='Quorabust',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'xgboost',
        'matplotlib',
        'seaborn',
        'jupyter',
    ],
    author='AliSinaDevelo',
    author_email='alisinakarimi.2003@gmail.com',
    description='A machine learning project to identify similar questions on Quora.',
    url='https://github.com/AliSinaDevelo/Quorabust',
)
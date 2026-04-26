from setuptools import setup

setup(
    name='cryptocrack',
    version=4.0 ,
    description='Decode All Bases - Base Scheme Decoder',
    author='Mufeed VH',
    url='https://github.com/princy0708/cryptocrack',
    license='MIT',
    packages=[
        'src'
    ],
    py_modules=[
        'cryptocrack'
    ],
    install_requires=[
        'argparse',
        'colorama',
        'termcolor',
        'pathlib',
        'anybase32',
        'base36',
        'base58',
        'pybase62',
        'base91',
        'pybase100',
        'exifread',
        'opencv-python',
        'pytesseract'
    ],
    python_requires='>=3.0.0',
    entry_points={
        'console_scripts': [
            'cryptocrack = cryptocrack:main'
        ]
    }
)

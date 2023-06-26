from setuptools import setup

setup(
    name='sublime-plugin-maker',
    version='1.0.0',
    description='An AI-powered Sublime Text Plugin Maker',
    author='P.A. SCHEMBRI',
    author_email='pierrealex@advanced-stack.com',
    url='https://github.com/paschembri/sublime-plugin-maker',
    packages=['sublime_plugin_maker'],
    install_requires=[
        'openai',
        'langchain==0.0.215',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'make-specs = sublime_plugin_maker.specifications:make',
            'make-plugin = sublime_plugin_maker.builder:make',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

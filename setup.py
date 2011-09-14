"""blatter"""

setup_info = dict(
    name="bookmarkdown",
    description="Write books in Markdown.",
    version="0.0.1",

    author='Steve Losh',
    author_email='steve@stevelosh.com',
    license='MIT License',
    url='http://bitbucket.org/sjl/bookmarkdown/',

    packages=['bookmarkdown'],

    scripts = ['bookmarkdown/bookmarkdown'],

    install_requires = [
        'python-markdown',
        'baker',
        'Jinja2',],

     classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities',
        ]
    )

try:
    from setuptools import setup
    del setup_info['scripts']
except ImportError:
    for unsupported in ('entry_points', 'install_requires'):
        del setup_info[unsupported]
    from distutils.core import setup

setup(**setup_info)

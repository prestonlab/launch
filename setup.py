from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ezlaunch',
      version='1.0.3',
      description='Tools to launch slurm jobs',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.7',
      ],
      url='http://github.com/prestonlab/launch',
      author='Neal Morton',
      author_email='mortonne@gmail.com',
      license='GPLv3',
      scripts=['bin/ezlaunch',
               'bin/getjid',
               'bin/jfile',
               'bin/jstatus',
               'bin/launch',
               'bin/rlaunch',
               'bin/slaunch',
               'bin/subjids'],
      include_package_data=True,
      zip_safe=False)

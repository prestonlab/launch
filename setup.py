import setuptools
import glob


scripts = glob.glob('bin/*')
setuptools.setup(scripts=scripts)

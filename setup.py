import distutils
import subprocess
from setuptools import setup

SCRIPT_NAME = 'poker'


class cProfileCommand(distutils.cmd.Command):
    """"""
    description = 'run cProfile on poker script'
    user_options = []

    def initialize_options(self):
        return

    def finalize_options(self):
        return

    def run(self):
        """Run command."""
        command = ['python3', '-m', 'cProfile', 'tests/perf/perf_test.py']
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        subprocess.check_call(command)


setup(
    name=SCRIPT_NAME,
    version='0.1.0',
    py_modules=['poker'],
    install_requires=[
        'Click',
    ],
    setup_requires=[
        'pytest-runner',
        'behave',
    ],
    tests_require=[
        'pytest',
        'behave',
    ],
    entry_points='''
        [console_scripts]
        poker=poker:main
    ''',
    cmdclass={
        'cProfile': cProfileCommand
    }
)

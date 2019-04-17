# -*- coding: utf-8 -*-


"""epita.command: defines the epita installation."""


from setuptools import Command
from .config import Paths
from .utils import Utils


class epita_install(Command):

    description = 'installation for epita pie'

    user_options = [
        ('automate', 'a', 'fully automate installation')
    ]

    def initialize_options(self):
        self.automate = None

    def finalize_options(self):
        pass

    def run(self):
        # Check if patch already installed
        if Utils.patchInstalled():
            return 0
        Utils.initFolders()
        Utils.moveFile('epita/bind.py', Paths.PATCH)
        Utils.setPerms(Paths.PATCH)
        Utils.setAlias(self.automate is not None)
        Utils.addVimToPie()
        print('Installation finished please run:\n')
        print('  source ' + Paths.BASHRC)

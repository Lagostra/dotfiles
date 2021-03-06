#!/usr/bin/env python3

from __future__ import print_function, with_statement
from builtins import input

import os
import platform
home = os.path.expanduser("~")
system = platform.system()

yes_answers = ('yes', 'YES', 'y', 'Y')

def setup_git():
    if input('Set up gitconfig? (yes/no) ') not in yes_answers:
        return
    name = input('Enter full name (for gitconfig): ')
    email = input('Enter email (for gitconfig): ')

    with open('git/.gitconfig', 'r') as f:
        gitconfig = f.read()

    gitconfig = gitconfig.format(name, email)

    if system == 'Windows':
        try:
            os.rename(os.path.join(home, '.gitconfig'), os.path.join(home, '.gitconfig.bak'))
        except WindowsError:
            pass
    else:
        try:
            os.rename(os.path.join(home, '.gitconfig'), os.path.join(home, '.gitconfig.bak'))
        except OSError:
            pass

    with open(os.path.join(home, '.gitconfig'), 'w') as f:
        f.write(gitconfig)

    os.symlink(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'git/.gitconfig-symlink'), os.path.join(home, '.gitconfig-symlink'))


def setup_bashrc():
    if input('Set up .bashrc? (yes/no) ') not in yes_answers:
        return

    if system == 'Windows':
        print('You are running Windows - .bashrc cannot be setup')
        return
    try:
        with open(os.path.join(home, '.bashrc')) as f:
            bashrc = f.read()
    except FileNotFoundError:
        bashrc = ''

    bashrc = 'source ~/.bashrc-symlink\n' + bashrc

    with open(os.path.join(home, '.bashrc'), 'w') as f:
        f.write(bashrc)

    try:
        os.rename(os.path.join(home, '.bashrc-symlink'), os.path.join(home, '.bashrc-symlink.bak'))
    except OSError:
        pass

    os.symlink(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.bashrc'), os.path.join(home, '.bashrc-symlink'))

def main():
    setup_bashrc()
    setup_git()


if __name__ == '__main__':
    main()

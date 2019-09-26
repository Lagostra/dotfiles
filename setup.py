import os
import platform
home = os.path.expanduser("~")
system = platform.system()

def setup_git():
    if input('Set up gitconfig? (yes/no) ') not in ('yes', 'YES', 'y', 'Y'):
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

    os.link('git/.gitconfig-symlink', os.path.join(home, '.gitconfig-symlink'))


def main():
    setup_git()


if __name__ == '__main__':
    main()

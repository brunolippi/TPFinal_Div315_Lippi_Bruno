import os

def install_requirements():
    if os.name in ['nt', 'dos']:
        command = 'python '
    else:
        command = 'python3 '

    os.system(f'{command} -m pip install -r requirements.txt')


if __name__ == '__main__':
    install_requirements()
    
    from game import dragon_ball
    
    dragon_ball()
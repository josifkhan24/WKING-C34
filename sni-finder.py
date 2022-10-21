import platform as p

if str(p.machine())=='aarch64':
    import sni
else:
    print('\033[1;31mCurrently your system is not supported, sorry\033[0m')
    sys.exit()
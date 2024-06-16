import click
import subprocess
import platform

def check(dst, size):
    print(f"Checking {dst}, size = {size}")
    param = '-n' if platform.system().lower()=='windows' else '-c'
    cmd = ['ping', dst, param, '1', '-M', 'do', '-s', str(size - 28)]
    return subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

@click.command()
@click.argument('dst', type=str)
@click.option('-m', '--min_mtu', type=int, default=68, show_default=True, help="Minimum MTU value to start the search")
@click.option('-M', '--max_mtu', type=int, default=1500, show_default=True, help="Maximum MTU value to start the search")
def find_mtu(dst, min_mtu, max_mtu):
    if not check(dst, min_mtu):
        print(f"{dst} unreachable with MTU = {min_mtu}")
        exit(1)

    l = min_mtu
    r = max_mtu + 1
    while r - l > 1:
        mid = (r + l) // 2
        if check(dst, mid):
            l = mid
        else:
            r = mid

    print(f"MTU = {l}")


if __name__ == '__main__':
    find_mtu()

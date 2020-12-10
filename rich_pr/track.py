from rich.progress import track
from time import sleep


def do_step(step):
    sleep(1)


for step in track(range(100)):
    do_step(step)

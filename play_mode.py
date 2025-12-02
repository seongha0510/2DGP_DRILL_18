import random

from pico2d import *
import game_framework


import game_world
import common

from boy import Boy
from court import Court


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        else:
            # 키보드 이벤트(KEYDOWN/KEYUP) 만 boy에게 전달
            if event.type in (SDL_KEYDOWN, SDL_KEYUP):
                common.boy.handle_event(event)
            # 마우스 이동 등 불필요한 이벤트는 무시하여 상태머신의 처리되지 않은 이벤트 로그를 줄임


def init():
    common.court = Court()
    game_world.add_object(common.court, 0)

    common.boy = Boy()
    game_world.add_object(common.boy, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

"""
Created on Sat Dec 11   23:50:10 2021

@author: Charlie
"""

# Play mode, when we can play the Tetris normally, with the keyboard
import cv2
from tetris import Tetris
from sys import exit

def run_interactive():
    env = Tetris()
    env.reset()
    env.render(wait_key=False)

    iteration = 0
    while True:
        k = cv2.waitKey(100)  # 10 milliseconds
        env.render(wait_key=False)
        if k == 27:
            print('ESC')
            break
        elif k == ord('a'):  # left
            env.move([-1, 0], 0)
            env.render(wait_key=False)
        elif k == ord('d'):  # right
            env.move([+1, 0], 0)
            env.render(wait_key=False)
        elif k == ord('s'):  # down
            env.move([0, +1], 0)
            env.render(wait_key=False)
        elif k == ord('w'):  # up
            # clockwise rotation
            env.move([0, 0], -90)
            env.render(wait_key=False)
        elif k == 32:  # space
            _, done = env.hard_drop(env.current_pos, env.current_rotation, render=False)
            env.render(wait_key=False)
            if done:
                break

        if iteration >= 8:
            env.fall()
            if env.game_over:
                break
            iteration = 0
        else:
            iteration += 1


if __name__ == "__main__":
    run_interactive()
    # do this after the break from the while loop
    cv2.destroyAllWindows()
    # to avoid python console running
    exit(0)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import sys
import os

# Game state
window_width, window_height = 800, 600
catcher_width, catcher_height = 80, 20
diamond_size = 20
score = 0
game_over = False
paused = False

# Position and speed
catcher_x = window_width // 2 - catcher_width // 2
catcher_y = 30
diamond_x = random.randint(0, window_width - diamond_size)
diamond_y = window_height - diamond_size
diamond_speed = 2

def midpoint_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1_zone0, y1_zone0 = convert_to_zone0(x1, y1, zone)
    x2_zone0, y2_zone0 = convert_to_zone0(x2, y2, zone)

    dx = x2_zone0 - x1_zone0
    dy = y2_zone0 - y1_zone0
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x, y = x1_zone0, y1_zone0

    while x <= x2_zone0:
        draw_point(*convert_back_to_original_zone(x, y, zone))
        if d > 0:
            d += incNE
            y += 1
        else:
            d += incE
        x += 1

def draw_point(x, y):
    glBegin(GL_POINTS)
    glVertex2i(int(x), int(y))
    glEnd()

def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx >= 0 and dy < 0:
            return 7
        elif dx < 0 and dy >= 0:
            return 3
        else:
            return 4
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx >= 0 and dy < 0:
            return 6
        elif dx < 0 and dy >= 0:
            return 2
        else:
            return 5

def convert_to_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convert_back_to_original_zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def draw_diamond(x, y):
    glColor3f(1.0, 1.0, 0.0)  # Yellow diamond
    midpoint_line(x, y, x + diamond_size // 2, y + diamond_size // 2)
    midpoint_line(x + diamond_size // 2, y + diamond_size // 2, x, y + diamond_size)
    midpoint_line(x, y + diamond_size, x - diamond_size // 2, y + diamond_size // 2)
    midpoint_line(x - diamond_size // 2, y + diamond_size // 2, x, y)

def draw_catcher():
    if game_over:
        glColor3f(1, 0, 0)
    else:
        glColor3f(1, 1, 1)
    base_y = catcher_y
    top_y = catcher_y + catcher_height
    left_x = catcher_x
    right_x = catcher_x + catcher_width
    midpoint_line(left_x + 20, base_y, left_x, top_y)
    midpoint_line(left_x, top_y, right_x, top_y)
    midpoint_line(right_x, top_y, right_x - 20, base_y)
    midpoint_line(right_x - 20, base_y, left_x + 20, base_y)

def draw_pause_button():
    x, y = window_width // 2 - 15, window_height - 40
    glColor3f(1, 1, 0)  # Yellow color for play/pause
    if paused:
        glBegin(GL_TRIANGLES)
        glVertex2i(x + 8, y + 6)
        glVertex2i(x + 8, y + 24)
        glVertex2i(x + 22, y + 15)
        glEnd()
    else:
        glBegin(GL_QUADS)
        glVertex2i(x + 7, y + 6)
        glVertex2i(x + 12, y + 6)
        glVertex2i(x + 12, y + 24)
        glVertex2i(x + 7, y + 24)

        glVertex2i(x + 18, y + 6)
        glVertex2i(x + 23, y + 6)
        glVertex2i(x + 23, y + 24)
        glVertex2i(x + 18, y + 24)
        glEnd()

def draw_restart_button():
    x, y = 10, window_height - 40  # Move to top-left
    glColor3f(0, 0, 1)  # Blue color for restart
    midpoint_line(x + 25, y + 5, x + 10, y + 15)
    midpoint_line(x + 10, y + 15, x + 25, y + 25)

def draw_exit_button():
    x, y = window_width - 50, window_height - 40  # Move to top-right
    glColor3f(1, 0, 0)  # Red color for exit
    midpoint_line(x, y, x + 20, y + 20)
    midpoint_line(x + 20, y, x, y + 20)

def update(value):
    global diamond_y, diamond_speed, score, diamond_x, game_over
    if not paused and not game_over:
        diamond_y -= diamond_speed
        if has_collided():
            score += 1
            diamond_y = window_height - diamond_size
            diamond_x = random.randint(0, window_width - diamond_size)
            diamond_speed += 0.2
        elif diamond_y < catcher_y:
            game_over = True

        # Clear the terminal and print the updated score
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {score}")

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def has_collided():
    return (diamond_x < catcher_x + catcher_width and
            diamond_x + diamond_size > catcher_x and
            diamond_y < catcher_y + catcher_height and
            diamond_y + diamond_size > catcher_y)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_diamond(diamond_x, diamond_y)
    draw_catcher()
    draw_pause_button()
    draw_restart_button()
    draw_exit_button()
    glutSwapBuffers()

def keyboard(key, x, y):
    global catcher_x
    if not game_over and not paused:
        if key == b'a' and catcher_x > 0:
            catcher_x -= 20
        elif key == b'd' and catcher_x + catcher_width < window_width:
            catcher_x += 20

def special_keys(key, x, y):
    if not game_over and not paused:
        global catcher_x
        if key == GLUT_KEY_LEFT and catcher_x > 0:
            catcher_x -= 20
        elif key == GLUT_KEY_RIGHT and catcher_x + catcher_width < window_width:
            catcher_x += 20

def mouse(button, state, x, y):
    global paused
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        adjusted_y = window_height - y

        px, py, pw, ph = window_width // 2 - 15, window_height - 40, 30, 30
        if px <= x <= px + pw and py <= adjusted_y <= py + ph:
            paused = not paused

        rx, ry, rw, rh = 10, window_height - 40, 30, 30  # Restart button top-left
        if rx <= x <= rx + rw and ry <= adjusted_y <= ry + rh:
            restart_game()

        ex, ey, ew, eh = window_width - 50, window_height - 40, 30, 30  # Exit button top-right
        if ex <= x <= ex + ew and ey <= adjusted_y <= ey + eh:
            sys.exit(0)

def restart_game():
    global score, catcher_x, diamond_x, diamond_y, diamond_speed, game_over, paused
    score = 0
    catcher_x = window_width // 2 - catcher_width // 2
    diamond_x = random.randint(0, window_width - diamond_size)
    diamond_y = window_height - diamond_size
    diamond_speed = 2
    game_over = False
    paused = False

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    gluOrtho2D(0, window_width, 0, window_height)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Catch the Diamonds!")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMouseFunc(mouse)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()

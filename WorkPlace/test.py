import OpenGL.GL as GL
import OpenGL.GLU as GLU
from OpenGL.arrays import vbo as VBO
import glfw

from .utils import init_work, event_loop, end_work, get_shader


SCR_WIDTH = 800
SCR_HEIGHT = 600

def main():
    window = init_work(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL")

    shader = get_shader("shaders/vertex_shader.vs", "shaders/fragment_shader.fs")

    def render():
        GL.glClearColor(0.2, 0.3, 0.3, 1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    def process_input(window):
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

    event_loop(window, render, process_input)

    end_work()

if __name__ == "__main__":
    main()
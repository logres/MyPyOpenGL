import OpenGL.GL as GL
from OpenGL.GL import shaders as Shaders
from OpenGL.GLU import *
import glfw


def init_work(width, height, title):
    if not glfw.init():
        print("glfw init failed")
        return None

    window = glfw.create_window(width, height, title, None, None)
    if not window:
        print("glfw create window failed")
        glfw.terminate()
        return None

    glfw.make_context_current(window)

    def frame_buffer_size_callback(window, width, height):
        GL.glViewport(0, 0, width, height)
    
    glfw.set_framebuffer_size_callback(window, frame_buffer_size_callback)
    return window

def event_loop(window, render_func, process_input_func=None):
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render_func()
        if process_input_func:
            process_input_func(window)
        glfw.swap_buffers(window)
        glfw.poll_events()

def end_work():
    glfw.terminate()

def get_shader(vertex_shader_path, fragment_shader_path):
    with open(vertex_shader_path, "r") as f:
        vertex_shader = f.read()
    with open(fragment_shader_path, "r") as f:
        fragment_shader = f.read()
    vertex_shader = Shaders.compileShader(vertex_shader, GL.GL_VERTEX_SHADER)
    fragment_shader = Shaders.compileShader(fragment_shader, GL.GL_FRAGMENT_SHADER)
    shader = Shaders.compileProgram(vertex_shader, fragment_shader)
    return shader
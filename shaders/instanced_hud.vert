#version 330 core

layout (location = 0) in vec4 in_position;
layout (location = 1) in vec2 in_uv;
layout (location = 2) in mat4 m_model;
layout (location = 4) in int in_tex_id;

out vec2 uv;
flat out int tex_id;


void main() {
    uv = in_uv;
    tex_id = in_tex_id;

    gl_Position = m_model * in_position;
}
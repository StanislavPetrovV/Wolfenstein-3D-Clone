#version 330 core

layout (location = 0) in vec4 in_position;
layout (location = 1) in vec2 in_uv;

uniform mat4 m_model;
out vec2 uv;


void main() {
    uv = in_uv;
    gl_Position = m_model * in_position;
}
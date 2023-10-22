#version 330 core

layout (location = 0) in vec4 in_position;
layout (location = 1) in vec2 in_uv;
layout (location = 2) in mat4 m_model;
layout (location = 4) in int in_tex_id;

uniform mat4 m_proj, m_view;

out vec2 uv;
flat out int tex_id;

void main() {
    uv = in_uv;
    tex_id = in_tex_id;

    mat4 m_model_view = m_view * m_model;
    // First colunm.
    m_model_view[0][0] = m_model[0][0];
    m_model_view[0][1] = 0.0;
    m_model_view[0][2] = 0.0;
    // Second colunm.
    m_model_view[1][0] = 0.0;
    m_model_view[1][1] = m_model[1][1];
    m_model_view[1][2] = 0.0;

    gl_Position = m_proj * m_model_view * in_position;
}

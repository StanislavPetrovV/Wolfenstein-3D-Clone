#version 330 core

out vec4 frag_color;
in vec2 uv;

uniform sampler2DArray u_texture_array_0;
uniform int tex_id;


void main() {
    frag_color = texture(u_texture_array_0, vec3(uv, tex_id));
}
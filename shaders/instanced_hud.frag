#version 330 core

out vec4 frag_color;
in vec2 uv;
flat in int tex_id;

uniform sampler2DArray u_texture_array_0;


void main() {
    vec4 tex_col = texture(u_texture_array_0, vec3(uv, tex_id));
    if (tex_col.a <= 0.1) discard;

    frag_color = tex_col;
}
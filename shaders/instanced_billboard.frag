#version 330 core

out vec4 frag_color;

in vec2 uv;
flat in int tex_id;

uniform sampler2DArray u_texture_array_0;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;


void main() {
    vec4 tex_col = texture(u_texture_array_0, vec3(uv, tex_id));
    if (tex_col.a <= 0.1) discard;

    vec3 col = pow(tex_col.rgb, gamma);

    // fog
    float fog_dist = gl_FragCoord.z / gl_FragCoord.w;
    col = mix(col, vec3(0.05), (1.0 - exp2(-0.015 * fog_dist * fog_dist)));

    col = pow(col, inv_gamma);
    frag_color = vec4(col, tex_col.a);
}
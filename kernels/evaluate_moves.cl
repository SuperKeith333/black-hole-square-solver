__kernel void evaluate_moves(
    __global const float2 *positions, // move/tile positions
    __global float *scores,           // output scores
    const float goal_x,               // target position (example)
    const float goal_y)
{
    int i = get_global_id(0);
    
    float dx = positions[i].x - goal_x;
    float dy = positions[i].y - goal_y;
    
    // simple scoring example: closer = higher score
    float dist = sqrt(dx * dx + dy * dy);
    scores[i] = 1.0f / (1.0f + dist);
}

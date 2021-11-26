/// Shoot Gun every 5 seconds
bullet_inst = instance_create_layer(x, y, "Instances", obj_enemy_bullet)
bullet_inst.direction = image_xscale == -1 ? 180 : 0
alarm[0] = room_speed * 2
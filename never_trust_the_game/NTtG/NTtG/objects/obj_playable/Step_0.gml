key_right = keyboard_check(ord("D"))
key_left = keyboard_check(ord("A"))
key_jump = keyboard_check_pressed(ord("S"))
	
move = key_right - key_left

if (move < 0 && image_xscale > 0) { image_xscale = -1 }
if (move > 0 && image_xscale < 0) { image_xscale = 1 } // turn the sprite around

if (abs(hsp) > 0) {
  hsp -= sign(hsp)	
}

hsp += move * move_speed
vsp += grav

on_ground = place_meeting(x, y + 1, obj_wall)  // bool
on_wall = place_meeting(x + 4, y, obj_wall) - place_meeting(x - 4, y, obj_wall) // -1, 0, 1

if (on_ground) {
	vsp = key_jump * (-jump_speed)
}

// Horizontal Collision
if (place_meeting(x + hsp, y, obj_wall)) {
	while (!place_meeting(x + sign(hsp), y, obj_wall)) {  
		// While we are "pretty close" to the wall, but not exactly up to it,
		// move the sprite up to it.
		x += sign(hsp)
	}
	hsp = 0
}

// Vertical Collision
if (place_meeting(x, y + vsp, obj_wall)) {
	while (!place_meeting(x, y + sign(vsp), obj_wall)) {
		y += sign(vsp)
	}
	vsp = 0
}

// Wall Jump
if (on_wall != 0) && (!on_ground) && (key_jump) {
	hsp = -on_wall * wall_jump_hsp
	vsp = wall_jump_vsp
}

hsp = clamp(hsp, -7, 7)

x += hsp
y += vsp

// Level End -- TODO: bad, refactor this.
if (riley_got_game_obj) {
	end_level_timer += 1
}

if (end_level_timer > (60 * 2)) {
	switch (room) {
		case rm_forest:
			room_goto(rm_gun_zone)
			end_level_timer = 0
			break
		case rm_gun_zone:
			room_goto(rm_tundra)
			end_level_timer = 0
			break
		case rm_tundra:
			room_goto(rm_clouds)
			end_level_timer = 0
			break
		case rm_clouds:
			room_goto(rm_sea)
			end_level_timer = 0
			break
		case rm_sea:
			room_goto(rm_desert)
			end_level_timer = 0
			break
	}
}
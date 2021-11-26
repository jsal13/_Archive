if (!stop_alpha) {
	draw_set_alpha(fade_timer / fade_timer_max);
	draw_set_color(c_black);
	draw_rectangle(0,
				   0,
				   room_width[0],
				   room_height[0],
				   false);
} else {
	draw_set_alpha(1);
}
// 	draw_set_color(c_black);
//	draw_rectangle(0,
//				   0,
//				   room_width[0],
//				   room_height[0],
//				   false);
//}
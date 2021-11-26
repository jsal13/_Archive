switch(room) {
	case rm_start:
		draw_set_halign(fa_center)
		
		var c = c_red
		var c1 = c_fuchsia
		
		draw_text_transformed_color(
			room_width/2, 100, "Never Trust The " + global._title_thing,
			2, 2, 0, c, c, c, c, 1
		);
		draw_text_transformed_color(room_width/2, 250, ">> Press enter, Pls. <<", 1.2, 1.2,  0,
			c1, c1, c1, c1, 1)
		break;
}

switch (room) {
	case rm_start:
		if (!audio_is_playing(snd_bkgd_title)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_title, 2, true) 
		}
		break
	case rm_forest:
		if (!audio_is_playing(snd_bkgd_forest)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_forest, 2, true) 
		}	
		break
	case rm_gun_zone:
		if (!audio_is_playing(snd_bkgd_gun_zone)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_gun_zone, 2, true) 
		}
		break
	case rm_tundra:
		if (!audio_is_playing(snd_bkgd_tundra)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_tundra, 2, true) 
		}
		break
	case rm_clouds:
		if (!audio_is_playing(snd_bkgd_clouds)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_clouds, 2, true) 
		}
		break
	case rm_sea:
		if (!audio_is_playing(snd_bkgd_sea)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_sea, 2, true) 
		}
		break
	case rm_desert:
		if (!audio_is_playing(snd_bkgd_desert)) { 
			audio_stop_all()
			audio_play_sound(snd_bkgd_desert, 2, true) 
		}
		break
}


if ((fade_timer < fade_timer_max) && getting_darker) {
	fade_timer += 1
} else if (fade_timer >= fade_timer_max) {
	getting_darker = false
	fade_timer -= 1
} else if (fade_timer > 0 && !getting_darker) {
	fade_timer -= 1
} else if (fade_timer <= 0 && !getting_darker) {
	getting_darker = true
	fade_timer += 1
}

from scipy.spatial.distance import euclidean as euclidean_dist

RED = 0
GREEN = 1
BLUE = 2

colors = {
	'red': [255, 0, 0],
	'black': [0, 0, 0],
	'blue': [0, 0, 255],
	'green': [0, 255, 0],
	'yellow': [255, 255, 0],
	'grey': [128, 128, 128],
	'pink': [240, 128, 128],
	'white': [255, 255, 255],
	'brown': [139, 69, 19],
}

def find_closest_color(rgb):
	closest_color = ''
	closest_distance = float('Inf')

	for color in colors:
		dist = euclidean_dist (colors[color], rgb)
		if dist <= closest_distance:
			closest_color = color
			closest_distance = dist

	return closest_color

print find_closest_color([0, 0, 0])

from numpy import *

def compute_error_for_given_point(b, m, points):
	totalError = 0
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		totalError += (y - (m * x + b)) ** 2
	return totalError/float(len(points))


def step_gradient(current_b, current_m, points, learningRate):
	# gradient descent
	b_gradient = 0
	m_gradient = 0

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	b = starting_b
	m = starting_m

	for i in range(num_iterations):
		b, m = step_gradient(b, m, array(points), learning_rate)
	return [b,m]


def run():
	points = genfromtext('data.csv', delimiter=',')
	#hyperparameter
	learning_rate = 0.0001
	#slope, y = mx + b
	initial_b = 0
	initial_m = 0
	num_iterations = 1000
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print(b)
	print(m)

if__name__ = '__main__':
	run()
import random


def gradient(w):
    return 2 * w

def gradient_descent(initial_point, rate=0.1, max=300, ws=1e-5):
    w = initial_point

    if abs(gradient(w)) < ws:
        print("Initial gradient is too small; choosing a new initial point >:) .")
        w = random.uniform(-13, 13)

    for i in range(max):
        grad = gradient(w)
        new_x = w - rate * grad
        if abs(new_x - w) < ws:
            break

        w = new_x


    return w

minimum = gradient_descent(initial_point=0)
print(f"Global Minimum found at w = {minimum}")

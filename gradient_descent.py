import random

def gradient(w):
    return 2 * w

def gradient_descent(rate=0.1, max=300, ws=1e-5):
    w = random.uniform(-13, 13)

    for i in range(max):
        grad = gradient(w)
        new_w = w - rate * grad
        if abs(new_w - w) < ws:
            break

        w = new_w

    return w

minimum = gradient_descent()
print(f"Global Minimum found at w = {minimum}")

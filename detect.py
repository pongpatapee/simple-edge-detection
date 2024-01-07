import PIL
import matplotlib.pyplot as plt
import numpy as np


def convolve(mat, filter):
    n_h = mat.shape[0]
    n_w = mat.shape[1]
    f, f = filter.shape

    output = np.zeros((n_h - f + 1, n_w - f + 1))

    for h in range(output.shape[0]):
        vert_start = h
        vert_end = vert_start + filter.shape[0]
        for w in range(output.shape[1]):
            horiz_start = w
            horiz_end = horiz_start + filter.shape[0]

            output[h, w] = convolve_one_pass(
                mat[vert_start:vert_end, horiz_start:horiz_end], filter
            )

    return output


def convolve_one_pass(mat_slice, filter):
    assert mat_slice.shape == filter.shape

    return np.sum(mat_slice * filter)


img = PIL.Image.open("hard_gradient.jpg")
gray_img = img.convert("L")
gray_img = np.array(gray_img)

Gx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

Gx = convolve(gray_img, Gx)
Gy = convolve(gray_img, Gy)
G = np.sqrt((Gx**2) + (Gy**2))

plt.subplot(2, 2, 1)
plt.imshow(gray_img, cmap="gray")
plt.title("Original")

plt.subplot(2, 2, 2)
plt.imshow(Gy, cmap="gray")
plt.title("Horizontal Edge (Gy)")

plt.subplot(2, 2, 3)
plt.imshow(Gx, cmap="gray")
plt.title("Vertical Edge (Gx)")

plt.subplot(2, 2, 4)
plt.imshow(G, cmap="gray")
plt.title("Combined Magnitude")

plt.show()

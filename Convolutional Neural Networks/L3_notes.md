# Convolutional Neural Networks

## Quiz

10 out of 15 points (**66.67%**)

Time for this attempt: 30 minutes 20 seconds

**Your Answers:**

---

### 1. Multi-layer perceptrons are suitable for image processing.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> Well, at least CNNs are more efficient.

---

### 2. Convolutional neural networks are position equivariant, because they apply the same filter at every location in the input.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> This applies to the singular convolutional layer, but not to the network as a whole.

---

### 3. When applying 4 filters to a colour image with 3 colour channels, how many feature maps are created?

1 / 1 point

Options:

-   36

-   3

-   12 <span style="color: lime"> **Correct answer**

-   4

---

### 4. When applying one filter to an image with shape (255, 255, 1), what is the output shape if no padding is used and the stride is set to 1?

1 / 1 point

-   (255, 255, 1)

-   (127, 127, 1)

-   (255, 255)

-   (253, 253, 1) <span style="color: lime"> **Correct answer**

---

### 5. When applying one filter to an image with shape (255, 255, 1), what is the output shape if no padding is used and the stride is set to 3?

1 / 1 point

-   (85, 85, 1) <span style="color: lime"> **Correct answer**

-   (255, 255, 1)

-   (253, 253, 1)

---

### 6. When applying one filter to an image with shape (255, 255, 5), what is the shape of the filter?

1 / 1 point

-   (5, 3, 3)

-   (3, 3, 5) <span style="color: lime"> **Correct answer**

-   (3, 3)

-   (255, 255, 5)

---

### 7. Max pooling checks the activations in a feature map in a specified neighbourhood and outputs the smallest value.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 8. Dilated convolutions "skip" the pixels in a pixel's direct neighbourhood, since it is assumed that they will have almost identical values.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

---

### 9. Deformed convolutions select randomly the pixels to be processed at a given location.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 10. Convolutional neural networks can only be applied to images.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 11. A LeNet-style CNN architecture can be applied to larger images than those on which it has been trained.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> Since the feature maps are converted into one dimensional vectors, which are fed into a feedforward network, the input size is fixed.

---

### 12. When applying one convolution on an input with shape (255, 255, 5), what is the output shape if no pooling is used and the stride is set to 1?

0 / 1 point

-   (253, 253, 1)

-   (255, 255, 5) <span style="color: orangered"> **Incorrect answer**

-   (255, 255, 1) <span style="color: lime"> **Correct Answer**

-   (255, 255, 1)

-   (253, 253, 5)

---

### 13. ResNet simplifies the learning process by adding the original input into a convolutional block to the output of the same block.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 14. Given that a UNet is a neural network which consists only of convolutional layers, it can be applied to images of varying size without the need for resizing the images.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 15. Transposed convolutions can be used to upscale an image by learning filters, which are applied by each pixel location with each value in the filter.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

# Training Neural Networks

## Quiz

16 out of 20 points (**80%**)

Time for this attempt: 248 hours 20 minutes 5 seconds

**Your Answers:**

---

### 1. Network initialisation is important for training, because starting at a good position on the loss surface simplifies training.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 2. Initialising the biases with a constant value is bad for training.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 3. Xavier initialisation works better than He initialisation for deep networks.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 4. When transferring trained weights to a new network, those weights should initially be frozen.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 5. It is important to freeze pre-trained weights initially when transferring them to a new network because large errors lead to large weight updates, which will destroy the pre-trained weights.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 6. When training a neural network, the data samples are provided in batches because the average gradient direction over the samples in the batch is more stable than if we would compute the average gradient over all training samples.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 7. When using the Adam optimisation algorithm, it is not necessary to tune the learning rate.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 8. The most important hyper parameter to tune is:

1 / 1 point

Options:

-   Model capacity

-   Dataset size

-   Learning rate <span style="color: lime"> **Correct answer**

---

### 9. Applying regularisation reduces the generalisation error at the interpolation threshold of the error-complexity curve.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

---

### 10. Adding more data to the training set does not affect the interpolation threshold.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> If the training set is larger, it is probably more difficult to get zero error on the entire training set. Thus, the interpolation threshold will shift.

---

### 11. Parameter norm penalties affect a model's capacity by modifying the loss function to penalise large weights.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 12. Early stopping determines when to stop the training process if the training error did not improve for a set number of epochs (patience).

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> Well, normally you would define a separate validation set based on which the training is stopped.

---

### 13. By randomly setting neuron outputs to zero, dropout implicitly trains an ensemble of sub-networks.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 14. Batch normalisation ensures that the output distribution of a neuron has zero mean and a standard deviation of one.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 15. Batch norm requires large batch sizes when applied to fully connected layers to obtain valid mean and standard deviation estimates.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 16. The main idea of augmentation is to modify the training instances, so that look like new and valid instances.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 17. The main idea of curriculum learning is to train a model based on a random selection of the training set.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 18. In Keras, defining a model means to define a computational graph, while in Torch defining a model means to write which function is called to compute the model output.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 19. After defining the model in Keras, it can directly be trained by calling the fit() function.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> You need to first compile the model.

---

### 20. Additional training behaviour, such as logging, early stopping or creating checkpoints can be configured in Keras using the callback API.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

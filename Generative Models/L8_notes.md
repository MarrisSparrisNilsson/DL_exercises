# Generative Models

## Quiz

15 out of 18 points (**83.33%**)

Time for this attempt: 32 minutes 36 seconds

**Your Answers:**

---

### 1. The idea of manifold learning is to find a space in which instances with the same class lie close together even if they have different feature values.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 2. Data generation via manifold learning works by finding a point on the manifold and mapping it back into the feature domain.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 3. An auto-encoder learns the manifold by mapping an input instance to a given label.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 4. Auto-encoders are well suited to learn manifolds which allow smooth interpolation.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

**Feedback based on answering incorrectly:**

> Somewhat smooth interpolations may emerge, but it is not incentivized in any way.

---

### 5. Variational auto-encoders generate instances by sampling from a normal distribution and mapping the obtained sample into the feature space.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 6. In order to allow for random sampling, Variational Auto-encoders use the reparameterization trick.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 7. Generative Adversarial Networks (GANs) consist of a generator and a discriminator.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 8. The goal of the discriminator in a GAN is to distinguish between convincing and not convincing generated images.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 9. Training GANs is easy since the generator and the discriminator naturally improve their performance getting better and better at the respective task.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 10. Conditional GANs allow to influence the generation process by providing a class label.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 11. Cycle GANs avoid mode collapse by ensuring cycle consistency, i.e., mapping from one style to another and back should yield approximately the same image.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 12. Stable diffusion works by predicting which parts of a given input are noise and removing them.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 13. Generative models can be used to generate new data samples, since they model the whole data generating distribution and not just the decision boundary.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 14. Score-based diffusion models learn to remove the noise in a noisy image given its noise level.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

**Feedback based on answering incorrectly:**

> Well, they are trained to predict the noise. Of course, you could remove it afterwards, but it is not what the model does.

---

### 15. Latent diffusion models perform de-noising on the images.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

**Feedback based on answering incorrectly:**

> The de-noising happens in feature space. That means we have a decoder, which projects the de-noised features into the output space, which are the generated images

---

### 16. Stable diffusion applies attention to the de-noising process in order to focus on those parts, which correspond to a text embedding vector.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 17. The idea of retrieval augmented generation (RAG) is to train generative models well enough, so that they can retrieve the relevant information needed for generation from their weights.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 18. Retrieval augmented generation (RAG) works only for large language models (LLMs).

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

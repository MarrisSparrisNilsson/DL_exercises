# Self-supervised Learning

## Quiz

11 out of 13 points (**84.62%**)

Time for this attempt: 13 minutes 16 seconds

**Your Answers:**

---

### 1. The main idea of self-supervised learning is to train on a large number of labeled samples.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 2. A pretext task is a machine learning task for which training data can be derived automatically from unlabeled data.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 3. Training using pretext tasks and freezing the weights of the initial layers results in better performance than training only on labeled data, even if a large number of training samples are available.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

**Feedback based on answering incorrectly:**

> If you just have enough labeled data, training on that without pretext training and freezing the weights tends to perform better. However, you may finetune the weights of the pre-trained model to achieve comparable performance.

---

### 4. Inpainting is a pretext task which works best if it is trained by optimizing the reconstruction loss alone.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 5. The split-brain autoencoder is trained by decomposing an image into different types of information, e.g., luminance and color and then using one half of the network to reconstruct one type of information from the other.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 6. Object tracking emerges automatically from training to color a video based on one reference frame.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 7. The main idea of contrastive representation learning (CRL) is to train a neural network by providing it with a set of instance pairs and letting it identify positive and negative instance pairs.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 8. A positive pair in CRL is a pair of instances of the same class.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

**Feedback based on answering incorrectly:**

> A positive pair is a pair of instances, which were derived from the same source instance.

---

### 9. One key idea of SimCRL is to use a projection head to map instance representations from a representation space, which will be used for downstream tasks, to a matching space, in which the similarity of two instances is assessed.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 10. SimCRL requires only a small number of negative instance pairs and thus a small batch size, since a low number of negative instances results in a tighter bound for the mutual information between the instances of the positive pair.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 11. Momentum Contrastive Learning (MoCo) requires only relatively small batch sizes because this approach keeps a queue of encoded negative instances, which can be used for contrastive learning.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 12. Contrastive Predictive Coding (CPC) can be applied to do self-supervised learning only on time series data.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 13. Self-supervised learning works only if the compared pairs have the same modality, e.g., both images.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

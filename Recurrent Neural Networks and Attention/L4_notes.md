# Recurrent Neural Networks and Attention

Interesting paper to read: [Neural Joke Generation](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/reports/2760332.pdf)

## Basic RNNs

**Problem:**

A common problem with RNNs is that in order to correctly calculate the next steps of a sequence we need to know the output of previous steps in the past iterations. For larger inputs this will mean that we need to backpropagate over many more output results which increases computational cost and memory cost.

### Vanishing and Exploding Gradients

For backpropagating n time steps, the weight vector `w` is multiplied with itself `n` times i.e. $w^n$ which is not very good. Weights that gets too small (close to 0) or too large (close to or larger than 2) makes the network create bigger differences between layers which makes it essentially not learn anything.

### Training RNNs

Training is done by unrolling the RNN and performing Backpropagation Through Time (BPTT)

## Gated RNNs

### Long Short Term-Memory (LSTM)

**Basic Idea:** Store information in cell state.

**Control flow of information through gates:**

-   **Forget gate** - Helps to reset the memory in case the information is not needed anymore.
-   **Input gate** - Overrides information which is used for learning and remembering new information.
-   **Output gate** - Values in the output gate close to 0 makes the cell not share any information with other cells and values close to 1 will make the information to pass. We allow the memory cell's internal state to impact the subsequent layers uninhibited.

### Gated and Linear Recurrent Units (GRUs & LRUs)

**GRUs** are similar to a LSTM cell but with fewer gates.

-   Reset gate - Similar to the forget gate
-   Update gate - Outputs the cell state between 0 and 1.
-   Cell state update
-   Cell output
-   **LRUs** are used to help with the problem of long sequences, as in the Long Range Arena benchmark. Another problem is that they need to be trained sequentially since cell states depend on the previous ones, thus training is not parallelized.

## Attentions

Attentions are used to process large sequences, but more generally we need it to focus on a particular signal that could have a lot of noise.

**Cocktail party problem:** Focus on what one person says when multiple people talk simultaneously.

So its all about what we choose to ignore.

### Soft Attention

-   Can be used for unsupervised segmentation.
-   Shows implicitly learned attention.

### Hard Attention

---

## Quiz

14 out of 21 points (**66.67%**)

Time for this attempt: 27 minutes 56 seconds

**Your Answers:**

---

### 1. Feedforward neural networks can remember previous inputs.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 2. A recurrent neural network bases its decsions on the current input as well as its previous output.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 3. In backpropagation through time, the weight update is applied only to the weight of the current time step.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> The update is applied to the weights at past time steps, even though they are the same weights, but with different inputs.

---

### 4. While resilient to exploding gradients, backpropagation through time is affected by the vanishing gradient problem.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 5. The vanishing gradient problem describes the issue that the gradient signal diminishes exponentially the further it needs to travel.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 6. Unlike feedforward neural networks, an RNN can remember inputs it has seen in a previous input sequences.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> The memory of an RNN is limited to inputs it has seen previously in the input sequence.

---

### 7. A bidirectional RNN processes an input sequence from start to finish and from finish to start.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 8. The forget gate of an LSTM cell determines how much of the previous cell state is remembered.

0 / 1 point

True
Incorrect Answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

---

### 9. The output of an LSTM cell's output gate is the final output of that cell.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> The final output of an LSTM cell is the product of the output gate and the updated cell state.

---

### 10. LSTMs can remember longer ranging dependencies than vanilla RNNs since information can be stored unaltered in its memory cell.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 11. Which of the following problems is a one to many sequence problem?

0 / 1 point

-   Image caption generation <span style="color: lime"> **Correct Answer**
-   Sentiment analysis
-   Translation <span style="color: orangered"> **Incorrect Answer**

---

### 12. It is not possible to combine RNNs and CNNs.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 13. Neural networks learn to pay attention to certain parts of the input implicitly.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 14. Soft attention identifies relevant tokens in an input sequence by comparing the token encoding with the previous hidden state of the processing RNN.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 15. In soft attention, a context vector is produced by a weighted sum over the token encodings scaled by the respective attention weight.

0 / 1 point

True
Incorrect Answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

---

### 16. CA-Net's spatial attention scales the feature maps based on their importance.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 17. CA-Net's scale attention identifies which of the feature maps of different scales are relevant, as well as which locations in those feature maps are relevant.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 18. Hard attention scales the entire input based on its attention weights.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 19. Hard attention can only be implemented using reinforcement learning.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> There is, for example, the deep recurrent writer by Gregor et al. (2015), which implements fully differentiable hard attention.

---

### 20. The Neural Turing Machine implements its memory with the help of LSTM memory cells.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 21. The addressing mechanism of the neural turing machine allows key-based access, as well as iterating over a list of consecutive memory locations.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

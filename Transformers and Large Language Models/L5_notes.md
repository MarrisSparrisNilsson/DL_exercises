# Transformers and Large Language Models (LLMs)

## Resources

-   [Illustration of transformers](https://jalammar.github.io/illustrated-transformer/)
-   [Transformers Explained Visually (Part 3): Multi-head Attention, deep dive](https://medium.com/data-science/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853)

## Problems and successes with LLMs

#### Good

-   Shows slight potential for general intelligence capabilities
-   Passes a few standardized intelligence tests such as the bar exam
-   Theory of Mind (Don't see or understand the context or get the full image of the environment or problem)

#### Bad

-   Bad at math
-   Lack of planning ahead
-   Hallucinations (Comes up with new false information or adds information not connected to the initial statements)
-   Easily tricked by adversarial prompts
-   Basic abstraction and reasoning

## Transformers

### How do they work?

They are typically **autocomplete on steroids**.

Takes advantage of attention networks to derive the probability of something being in the following sequence.

#### Self-attention

##### Self-attention encoder

**Example:**

The input sequence is fed to the Input Embedding and Position Encoding, which produces an encoded representation for each word in the input sequence that captures the meaning and position of each word. This is fed to all three parameters, Query, Key, and Value in the Self-Attention in the first Encoder which then also produces an encoded representation for each word in the input sequence, that now incorporates the attention scores for each word as well. As this passes through all the Encoders in the stack, each Self-Attention module also adds its own attention scores into each word’s representation.

They commonly use multiple attention heads to

## Large Language Models (LLMs)

## Quiz

9 out of 13 points (**69.23%**)

Time for this attempt: 20 minutes 9 seconds

**Your Answers:**

---

### 1. Transformers are implemented with the help of LSTMs.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

---

### 2. The encoder branch of a transformer can process all input tokens in parallel.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 3. Self-attention identifies which input tokens to pay attention to when processing an input token t by:

1 / 1 point

-   Comparing t's **key vector** with the **value vectors** of all input tokens

-   Comparing t's **query vector** with the **value vectors** of all input tokens

-   Comparing t's **query vector** with the **key vectors** of all input tokens <span style="color: lime"> **Correct answer**

-   Comparing t's **key vector** with the **query vectors** of all input tokens

---

### 4. In the mechanism for a transformer's multi-head attention, removing one head automatically adds two new heads to the architecture.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 5. In transformers, positional encoding is necessary to preserve token order, which otherwise would be lost.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 6. The decoder of a transformer produces all output tokens in parallel.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 7. Transformers work only on text.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 8. Large language models are implemented using transformer architectures with many layers.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 9. According to the scaling laws, we will get better and better performing LLMs simply by training them for longer.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> The scaling laws show that it is not sufficient to increase only the computation time, we also need to increase the network size and add more data.

---

### 10. Instruction fine-tuning requires a large set of human generated task descriptions.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> It is possible to let the language model generate task examples from a small set of human generated tasks.

---

### 11. LLMs can be trained using reinforcement learning.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 12. Low-rank adaptation (LoRA) learns an update to the original weight matrix which has the same number of parameter as the original matrix.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> While the update matrix has the same dimensionality, the number of learnable parameters is less, since the update matrix gets decomposed into two smaller matrices with significantly fewer parameters.

---

### 13. In a sparse mixture-of-experts are all experts queried and their individual responses are combined using soft attention.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

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

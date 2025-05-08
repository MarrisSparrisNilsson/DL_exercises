# Transformers and Large Language Models (LLMs)

## Resources

-   [Illustration of transformers](https://jalammar.github.io/illustrated-transformer/)
-   [Transformers Explained Visually (Part 3): Multi-head Attention, deep dive](https://medium.com/data-science/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853)
-

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

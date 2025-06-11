# Neurosymbolic Reasoning

## Main Concept

**Can we improve the predictions from what we already have?**

**Example:** By changing the pixel of a single pixel of an object, how can we make a model stable so that it doesn't lose the perception of the objects in the images?

When mixing/overlapping objects the models can be confused depending on the different scenarios it's been trained on. If we match a monkey with a bicycle the models might recognize the bicycle with no problem, but the monkey might be recognized as a person, because the most often associated humanoid creature with a bicycle, are humans.

### The Binding/Grounding Problem

Recognition failures stem from inability to form meaningful entities from unstructured inputs.

Binding types:

-   Visual binding (color, shape, texture)
-   Auditory binding (a voice from a crowd)
-   Binding across time (motion)
-   Cross-modal binding (sound and vision into an event)

### Symbolic Approaches

With the help of symbolic definitions you can run inference on recognized object to eventually determine and increase the certainty of the type of object.

Based on high level symbols and symbol manipulation:

-   Logic programming (e.g., Prolog)
-   Semantic Networks
-   Description logic
-   Fuzzy logic (What does it mean by "red" apple? Red is a fairly fuzzy definition. There could be different color mixtures in an image)
-   Knowledge graph

## Quiz

11 out of 12 points (**91.67%**)

Time for this attempt: 33 minutes 34 seconds

**Your Answers:**

---

### 1. The existence of adversarial samples for deep learning algorithms is surprising.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 2. One challenge for neural network based systems is to solve the binding problem.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 3. Symbolic approaches are known to be stable even in the presence of uncertainty and ambiguity.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 4. A Symbolic[Neuro] system uses neural networks to extract symbolic data from raw input data and uses symbolic problem solvers to operate on this data.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 5. Neuro|Symbolic systems perform reasoning using both neural networks and symbolic systems.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 6. Neuro\_{Symbolic} systems use symbolic rules to impose a certain inductive bias on the neural network.

0 / 1 point

Incorrect Answer: <span style="color: orangered">
**False**

Correct Answer: <span style="color: lime">
**True**

---

### 7. Neuro[Symbolic] systems are the easiest to implement neurosymbolic approaches.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 8. Propositional logic is more expressive than first order logic.

1 / 1 point

Correct Answer: <span style="color: lime">
**False**

---

### 9. Logic Tensor Networks is a framework for imposing first order logic constraints on the training process of neural networks.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 10. In LTNs, variables are represented as sequence of instance representations.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 11. Connectives (conjunction, disjunction, negation, implication) and quantifiers (existential and universal) are represented in LTNs as vector operations, which allow for "soft" reasoning.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

---

### 12. LTNs are trained by maximizing the satisfiability of all defined rules.

1 / 1 point

Correct Answer: <span style="color: lime">
**True**

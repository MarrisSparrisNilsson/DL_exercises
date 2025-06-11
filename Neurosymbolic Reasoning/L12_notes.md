# Neurosymbolic Reasoning

## Main Concept

**Can we improve the predictions from what we already have?**

**Example:** By changing the pixel of a single pixel of an object, how can we make a model stable so that it doesn't lose the perception of the objects in the images?

When mixing/overlapping objects the models can be confused depending on the different scenarios it's been trained on. If we match a monkey with a bicycle the models might recognize the bicycle with no problem, but the monkey might be recognized as a person, because the most often associated humanoid creature with a bicycle, are humans.

### The Binding/Grounding Problem

Recognition failures stem from inability to form meaningful entities from unstructured inputs.

Binding types:

- Visual binding (color, shape, texture)
- Auditory binding (a voice from a crowd)
- Binding across time (motion)
- Cross-modal binding (sound and vision into an event)

### Symbolic Approaches

With the help of symbolic definitions you can run inference on recognized object to eventually determine and increase the certainty of the type of object.

Based on high level symbols and symbol manipulation:

- Logic programming (e.g., Prolog)
- Semantic Networks
- Description logic
- Fuzzy logic (What does it mean by "red" apple? Red is a fairly fuzzy definition. There could be different color mixtures in an image)
- Knowledge graph

## Quiz

# Deep Reinforcement Learning

## Quiz

5 out of 11 points (**45.45%**)

Time for this attempt: 20 minutes 17 seconds

**Your Answers:**

---

### 1. In reinforcement learning, an agent learns by trial and error.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 2. Using reinforcement learning is the most efficient way to learn something.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 3. A reinforcement learning agent interacts with its environment by assessing its state and taking an action based on this state alone.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**True**

> **Feedback based on answering incorrectly:**
> Based on the Markov assumption that the states are independent of each other we only need to know the current state and not past states.

---

### 4. The goal of an reinforcement learning agent is to choose the action yielding the immediate highest reward.

1 / 1 point

Correct answer: <span style="color: lime">
**False**

---

### 5. The quality of an action taken in a given state is composed of the reward obtained in that state plus the expected future reward.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**True**

---

### 6. A reinforcement learning agent should always choose the action with the expected highest final reward.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> In order to avoid getting stuck in some local minimum, we need to explore actions which do not seem to be optimal.

---

### 7. In deep Q-Learning, the quality of a state-action pair is predicted by a deep neural network.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

---

### 8. Experience replay captures a sequence of state-action transitions to be replayed for training the reinforcement learning agent further.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**False**

> **Feedback based on answering incorrectly:**
> The replay buffer yields single state, action, reward, new state tuples instead of sequences of state transitions.

---

### 9. In double deep Q-Learning, two neural networks are used one which is trained and one with frozen weights, which is used to estimate the expected future reward.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**True**

> **Feedback based on answering incorrectly:**
> It was shown that having a separate network with frozen weights predict the expected future reward stabilizes training.

---

### 10. Policy gradient based methods model the agent's policy directly by predicting the probability of performing an action.

0 / 1 point

Incorrect answer: <span style="color: orangered">
**True**

Correct Answer: <span style="color: lime">
**True**

---

### 11. The actor-critic approach to reinforcement learning uses a neural network to estimate the quality of a state-action pair, which is used to update the policy.

1 / 1 point

Correct answer: <span style="color: lime">
**True**

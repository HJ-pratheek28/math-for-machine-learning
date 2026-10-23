# Information Theory — Practice

## By hand
1. What does entropy measure intuitively?
2. For a fair binary variable, calculate entropy using base-2 logarithms.
3. Compare entropy for distributions `(0.5, 0.5)` and `(0.99, 0.01)`.
4. Explain entropy versus cross-entropy.
5. What does KL divergence compare? Why is it not generally symmetric?
6. Explain information gain in a decision tree.

## Python
1. Calculate entropy from a probability vector, handling zero probabilities safely.
2. Calculate binary cross-entropy for predicted probabilities and labels.
3. Plot binary entropy for `p` from near 0 to near 1.
4. Compare categorical distributions using KL divergence.

## ML connection
Why is cross-entropy a natural loss for classification with predicted probabilities? Distinguish predicted probability from the final class decision.
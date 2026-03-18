import numpy as np
import matplotlib.pyplot as plt

sensitivity = 0.99

specificities = [0.99, 0.999, 0.9999, 0.99999]

prevalence = np.linspace(0.00001, 0.5, 500)

def posterior_prob(prev, sens, specificity):
    false_positive = 1 - specificity
    numerator = sens * prev
    denominator = sens * prev + false_positive * (1 - prev)
    return numerator / denominator

plt.figure(figsize=(8,6))

for spec in specificities:
    probs = posterior_prob(prevalence, sensitivity, spec)
    plt.plot(prevalence*100, probs*100, label=f"Specificity {spec*100:.3f}%")

plt.xlabel("Infection Prevalence (%)")
plt.ylabel("P(Infected | Positive Test) (%)")
plt.title("Probability of Infection Given Positive Test")
plt.legend()
plt.grid(True)

plt.show()
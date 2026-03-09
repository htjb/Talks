## Preparing the UK for the SKA Data Future

19th - 20th March 2026
At Royal Observatory Edinburgh.

```
The 1.5 day workshop will be organized around three key areas, where we are looking for your input:

- Scientific drivers for AI in radio astronomy: how do you and your team plan to use AI/ML for SKA-related science?
- Technical enablers that make AI adoption possible: what are the computing facilities you will rely on?
- Policy requirements for responsible and effective use of AI/ML: what is your approach to metascience principles such as FAIR data, sustainability, and transparency?
```

## Talk?

**Title**: Understanding the impact of emulators in our inference pipelines

**Abstract**: 
Neural network emulators are widely used in astrophysics and cosmology to approximate computationally expensive simulations inside inference loops, and their role in radio astronomy will only grow as the SKA begins delivering data at unprecedented scale and complexity. However, understanding the uncertainty they introduce is crucial for responsible and reliable science. Researchers often measure emulator accuracy in signal space and use ad hoc rules of thumb to determine what is "good enough" for inference. We present a theoretically motivated approach to translate emulator error directly into an error on the recovered posterior, quantified via a Kullback–Leibler divergence. Under assumptions of linearity, uncorrelated noise, and a Gaussian likelihood, we provide a rigorous bound on the maximum incorrect information inferred when using an emulator. The resulting metric is instrument-aware, depending explicitly on the noise level, and can be used both to build confidence in inference products and as an instrument-aware loss function during emulator training. We demonstrate performance on mock observations from 21-cm instruments and argue that with principled accuracy metrics, emulators are a powerful and trustworthy tool for SKA-era science.
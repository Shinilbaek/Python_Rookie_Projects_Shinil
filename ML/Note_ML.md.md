# Machine Learning Note

*Machine Learning A Probabilistic Perspective*, Chap5-Chap8

---

## Chapter 5 Bayesian Statistics

### 1. Intro

MAP parameter estimates $\hat{\theta}=argmax\ p(\theta|D)$

posterior predictive density $p(x|D)$

### 2. Summarizing Posterior Distributions

1. Drawbacks of MAP:

   1. No measure of uncertaincy

   2. plugging in the MAP estimate can result in overfitting

   3. The mode is an untypical point

      0-1 loss: $L(\theta,\hat{\theta})=I(\theta \neq \hat{\theta})$

      squared error loss: $L(\theta,\hat{\theta})=(\theta - \hat{\theta})^2$ -> posterior mean

      absotlute error loss: $L(\theta,\hat{\theta})= |\theta -\hat{\theta}|$ -> posterior median

   4. A more subtle problem with MAP estimation is that the result we get depends on how we pa- rameterize the probability distribution. Thus the MAP estimate depends on the parameterization.

2. The difference between credible interval and confidence interval

   A frequentist 95% confidence interval means that with a large number of repeated samples, 95% of such calculated confidence intervals would include the true value of the parameter. In frequentist terms, the parameter is fixed (cannot be considered to have a distribution of possible values) and the confidence interval is random (as it depends on the random sample).

   - credible intervals incorporate problem-specific contextual information from the prior distribution whereas confidence intervals are based only on the data
   - credible intervals and confidence intervals treat nuisance parameters in radically different ways.

3. Bayesian Occam’s razor effect: models with more parameters do not necessarily have higher marginal likelihood.  

4. Conservation of probability mass principle: 

5. Complex models, which can predict many things, must spread their probability mass thinly, and hence will not obtain as large a probability for any given data set as simpler models.

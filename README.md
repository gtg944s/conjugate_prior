# conjugate_prior
Python implementation of the conjugate prior table for Bayesian Statistics


See wikipedia page:

https://en.wikipedia.org/wiki/Conjugate_prior#Table_of_conjugate_distributions

## Installation:
`pip install conjugate_prior`

## Supported Models:
  1. BetaBinomial - Useful for independent trials such as click-trough-rate (ctr), web visitor conversion.
  1. BetaBernoulli - Same as above.
  1. GammaExponential - Useful for churn-rate analysis, cost, dwell-time.
  1. GammaPoisson - Useful for time passed until event, as above.
  1. NormalNormalKnownVar - Useful for modeling a centralized distribution with constant noise.
  1. InvGammaNormalKnownMean - Useful for modeling the effect of a noise.
  1. InvGammaWeibullKnownShape - Useful for reasoning about particle sizes over time.
  1. DirichletMultinomial - Extension of BetaBinomial to more than 2 types of events (Limited support).

## Coin flip example:

    from conjugate_prior import BetaBinomial
    heads = 95
    tails = 105
    prior_model = BetaBinomial() #Uninformative prior
    updated_model = prior_model.update(heads, tails)
    credible_interval = updated_model.posterior(0.45, 0.55)
    print ("There's {p:.2f}% chance that the coin is fair".format(p=credible_interval*100))
    predictive = updated_model.predict(50, 50)
    print ("The chance of flipping 50 Heads and 50 Tails in 100 trials is {p:.2f}%".format(p=predictive*100))

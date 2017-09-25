from distutils.core import setup
setup(
  name = 'conjugate_prior',
  packages = ['conjugate_prior'],
  install_requires=[
          'scipy',
          'numpy',
          'matplotlib',
  ],
  version = '0.1',
  description = 'Bayesian Statistics conjugate prior distributions',
  author = 'Uri Goren',
  author_email = 'uri@goren4u.com',
  url = 'https://github.com/urigoren/conjugate_prior',
  download_url = 'https://github.com/urigoren/conjugate_prior/archive/0.1.tar.gz',
  keywords = ['conjugate', 'bayesian', 'stats', 'statistics', 'bayes', 'distribution', 'probability', 'hypothesis', 'modelling'],
  classifiers = [],
)

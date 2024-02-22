class ModelBase:
    def __init__(self, model_str, prefix, hyperparams):
    """
      Set up class with model string, prefix and hyperparams.

      Args:
        self: class instance
        model_str: model to use
        prefix: model name
        hyperparams: model hyperparameters 
      """
      self.model_str = model_str
      self.prefix = prefix
      self.hyperparams = hyperparams

    get_model_str(self):
      """
      Returns:
        A model string of class instance
      """
      return self.model_str

    get_prefix(self):
      """
      Returns:
        A prefix string of class instance
      """
      return self.prefix

    get_hyperparams(self):
      """
      Returns:
       A hyperparameter dictionary of class instance
      """
      return self.hyperparams

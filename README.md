# overfit - training code generation
Not ready for use.

## Examples
```python
from overfit.unsupervised import UnsupervisedPipeline
fit = SupervisedPipeline(data = data,
                         target = 'varname',
                         type = 'regression',
                         nfolds = 10
                         )
fit.get_code()

```
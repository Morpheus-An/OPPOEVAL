from mmengine.config import read_base

with read_base():
    # import everything you need in `imports`
    from ..imports import *


# if it is a local huggingface model,
# `name` should be the name of the folder inside model_base;
# if it is a api model,
# `name` should be the same as its api name
name = "model_name"


# if it is a local hugginface model, use model_base from `imports`:
# path should be `model_base/name`. Se the following line:
# path = osp.join(model_base, name)
# if its a api model,
# `path` should be the same as its api name
path = "path/to/the/model"

# model_name should be the same as the value of `name`
model_name = dict(
    abbr=name,
    type=...,
    other_params=...
)

from functools import wraps
import logging

#### Display the return value (rval) of a function
def return_val(func):
  @wraps(func)
  def decorated(*args, **kwds):
    ret = func(*args, **kwds)
    print("#"*80)
    print("func: {}".format(func.__name__))
    print("args: {}".format(args))
    print("kwds: {}".format(kwds))
    print("rval: {}".format(ret))
    return ret
  return decorated

#### Interrupt error handling
def exception(func):
  @wraps(func)
  def decorated(*args, **kwds):
    "Insert ErrorHandling"
    try:
      return func(*args, **kwds)
    except:
      logging.exception("Error is happened in {}".format(func.__name__))
  return decorated

#### Unit Test (private)
@return_val
def _return_val(a:int,b:int) -> int:
  return (a/b)

@exception
def _execption() -> int:
  return (1/0)

if __name__ == "__main__":
  _return_val(1,1)
  _execption()
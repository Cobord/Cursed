"""
try finally pattern
/context managers which do similarly
pylint doesn't even complain about
this control flow in the finally
"""

import random
from typing import Callable, ContextManager, Optional


def logged_close(obj : ContextManager,*,
                 logger_pre : Optional[Callable[[],None]] = None,
                 logger_post : Optional[Callable[[],None]] = None) -> ContextManager:
    """
    modify the obj's close by putting in logger_pre call first
    then normal closing, then logger_post
    """
    old_close = obj.close
    def new_close():
        if logger_pre is not None:
            logger_pre()
        old_close()
        if logger_post is not None:
            logger_post()
    obj.close = new_close
    return obj

def check_logged_close():
    """
    see the insertion of "about to close"
    in between return statement of function
    and continuing after the call
    """
    with logged_close(open("context_manager.py","r",encoding="utf-8"),
                    logger_pre=lambda : print("about to close")) as _my_fp:
        print("inside with")
        return print("returning")
check_logged_close()

def control_flow_in_finally():
    """
    a continue in finally preventing the
    exception from stopping the loop
    the value error is lost
    and pylint didn't say lost-exception
    """
    for i in range(10):
        print(i)
        try:
            raise ValueError("some error")
        except ValueError as exc:
            raise ValueError(f"{i}") from exc
        finally:
            continue
control_flow_in_finally()

def finally_overwrites_return() -> int:
    """
    this one is caught by pylint as
    return-in-finally and lost-exception
    """
    # pylint:disable = lost-exception
    try:
        if random.randint(0,10) < 5:
            return 0
        raise ValueError("something")
    except ValueError as exc2:
        raise exc2
    finally:
        return 1
print(f"finally_overwrites_return gives : {finally_overwrites_return()} instead of 0 or raising ValueError")

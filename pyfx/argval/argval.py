"""Validation for function arguments."""

from functools import wraps
from inspect import signature


def enforce_type(arg_name, type_or_tuple):
    """Decorator that enforces the type of the function argument given.

    :param arg_name: Name of the argument whose type to enforce
    :type arg_name: str
    :param type_or_tuple: Expected type(s) of the argument
    :type type_or_tuple: Type | Tuple[Type, ...]
    """

    if not isinstance(arg_name, str):
        raise TypeError(
            f"Parameter 'arg_name' must be type 'str', not '{type(arg_name).__name__}'"
        )

    def decorator(func):
        sig = signature(func)

        if arg_name not in sig.parameters:
            raise ValueError(
                f"Given argument name '{arg_name}' not found in function '{func.__name__}'"
            )

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            arg_value = bound_args.arguments[arg_name]

            if not isinstance(arg_value, type_or_tuple):
                type_string = (
                    type_or_tuple.__name__
                    if isinstance(type_or_tuple, type)
                    else " or ".join(t for t in type_or_tuple)
                )
                raise TypeError(
                    f"Argument '{arg_name}' must be of type '{type_string}' or a subclass, "
                    f"not '{type(arg_value).__name__}'"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator


def enforce_types(**type_map):
    """Decorator that enforces the types of multiple function arguments.

    :param type_map: A dictionary where keys are argument names and values are expected types
    :type type_map: Dict[str, Type | Tuple[Type, ...]]
    """

    def decorator(func):
        sig = signature(func)
        for arg_name in type_map:
            if arg_name not in sig.parameters:
                raise ValueError(
                    f"Given argument name '{arg_name}' not found in function '{func.__name__}'"
                )

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            for arg_name, type_or_tuple in type_map.items():
                arg_value = bound_args.arguments[arg_name]
                if not isinstance(arg_value, type_or_tuple):
                    type_string = (
                        type_or_tuple.__name__
                        if isinstance(type_or_tuple, type)
                        else " or ".join(t for t in type_or_tuple)
                    )
                    raise TypeError(
                        f"Argument '{arg_name}' must be of type '{type_string}' or a subclass, "
                        f"not '{type(arg_value).__name__}'"
                    )

            return func(*args, **kwargs)

        return wrapper

    return decorator


def enforce_arg_within(arg_name, lower_bound, upper_bound):
    """Enforce that a function argument is within a specified range.

    :param arg_name: Name of the argument whose value to enforce
    :type arg_name: string
    :param lower_bound: Lower bound of the range (inclusive)
    :type lower_bound: Comparable
    :param upper_bound: Upper bound of the range (inclusive)
    :type upper_bound: Comparable
    """

    if not isinstance(arg_name, str):
        raise TypeError(
            f"Parameter 'arg_name' must be type 'str', not '{type(arg_name).__name__}'"
        )

    def decorator(func):
        sig = signature(func)

        if arg_name not in sig.parameters:
            raise ValueError(
                f"Given argument name '{arg_name}' not found in function '{func.__name__}'"
            )

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            arg_value = bound_args.arguments[arg_name]

            if not lower_bound <= arg_value <= upper_bound:
                raise ValueError(
                    f"Argument '{arg_name}' must be within range [{lower_bound}, {upper_bound}]"
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator

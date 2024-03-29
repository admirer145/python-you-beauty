from functools import wraps


def validate_annotated_args_type(func):
    """This function validate the correct argument type for a function 'func'

    This functions works only if function 'func' have all the arguments as annotated.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function for validating the argument types
        """
        index = 0
        for argument, expected_type in func.__annotations__.items():
            if argument == 'return':
                break
            if index < len(args):
                input_type = type(args[index])
            else:
                input_type = type(kwargs.get(argument)) if kwargs.get(argument) else expected_type
            if input_type != expected_type:
                raise TypeError(f"Invalid argument type: {input_type} for argument {argument}, expected: {expected_type}")
            index += 1
        # actual function call
        resp = func(*args, **kwargs)
        return resp
    return wrapper


### Instead of checking valid input data types of arguments using commented way
### in 'calculate_sum' function
### we can create our own custom decorator for validation.

@validate_annotated_args_type
def calculate_sum(first_num: int, second_num: int = 0) -> int:
    """This method calculate sum of 2 values

    Arguments:
        first_num  (int): First input number
        second_num (int): Second input number

    Returns:
        sum of first_num and second_num
    """
    # if not isinstance(first_num, int) or not isinstance(second_num, int):
    #     raise TypeError("Invalid argument type provided, expected int")

    return first_num + second_num


# Testing with sample inputs
calculate_sum(3)
calculate_sum(3, 4)
calculate_sum(3, second_num = 4)
calculate_sum("3", "4")

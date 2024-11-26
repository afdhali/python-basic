def __sum_array(arr):  # berikan __ agar hanya dapat diakses oleh internal file
    if len(arr) == 0:
        return 0
    return arr[0] + __sum_array(arr[1:])

def _add_calculation(*numbers):
    try:
        if not numbers:
            raise ValueError("Cannot be empty on numbers input")
        if not all(isinstance(x,(int,float)) for x in numbers):
            raise ValueError("Must be numbers")
        return __sum_array(numbers)
    except Exception as e:
        raise ValueError(f"Erros in calculation: {str(e)}")

sum_modules = _add_calculation

if __name__ == "__main__" :
    print(_add_calculation(1,5,10.5))



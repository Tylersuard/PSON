import ast

class PSONDecodeError(Exception):
    def __init__(self, message, expression=None):
        super().__init__(message)
        self.expression = expression

class PSON:
    @staticmethod
    def dumps(py_obj):
        """
        Converts a Python object to a PSON-formatted string.
        
        Args:
            py_obj (dict or list): The Python object to be converted.
        
        Returns:
            str: A string of the object
        """
        return str(py_obj)

@staticmethod
def loads(pson_string):
    """
    Converts a PSON-formatted string (using Python syntax) to a Python object.
    
    Args:
        pson_string (str): The PSON string to be parsed.
    
    Returns:
        dict or list: The resulting Python object.
    """
    try:
        # Strip leading/trailing whitespace to handle multiline strings
        pson_string = pson_string.strip()
        # Use ast.literal_eval to safely evaluate Python-like expressions
        py_obj = ast.literal_eval(pson_string)
        if not isinstance(py_obj, (dict, list)):
            raise PSONDecodeError("PSON should be a dictionary or list format.")
        return py_obj
    except (SyntaxError, ValueError) as e:
        raise PSONDecodeError("Error parsing PSON: Invalid syntax. Please check for proper Python-style formatting.", expression=pson_string) from e
    except Exception as e:
        raise PSONDecodeError(f"Error parsing PSON: {e}", expression=pson_string) from e
        
# Example Usage
if __name__ == "__main__":
    # Define a PSON string using Python syntax
    pson_str = """
    {
        'name': 'Alice',
        'age': 30,
        'is_student': False,
        'hobbies': ['reading', 'hiking', 'coding']
    }
    """

    try:
        # Convert PSON to Python dict
        data = PSON.loads(pson_str)
        print("Parsed PSON to Python object:")
        print(data)

        # Convert Python dict back to PSON
        pson_str_converted = PSON.dumps(data)
        print("\nConverted Python object to PSON string:")
        print(pson_str_converted)
    except PSONDecodeError as e:
        print("\nPSON Decode Error:")
        print(e)
        if e.expression:
            print("Problematic expression:")
            print(e.expression)

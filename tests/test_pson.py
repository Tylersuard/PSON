import PSON

def test_loads():    # Define a PSON string using Python syntax
    pson_str = """
    {
        'name': 'Alice',
        'age': 30,
        'is_student': False,
        'hobbies': ['reading', 'hiking', 'coding']
    }
    """

      # Convert PSON to Python dict
    data = PSON.loads(pson_str)
    assert data is not None
    print("Parsed PSON to Python object:")
    print(data)


  def test_dumps():
    data = {
        'name': 'Alice',
        'age': 30,
        'is_student': False,
        'hobbies': ['reading', 'hiking', 'coding']
    }
  # Convert Python dict back to PSON
    pson_str_converted = PSON.dumps(data)
    print("\nConverted Python object to PSON string:")
    print(pson_str_converted)
    assert pson_str_converted is not None

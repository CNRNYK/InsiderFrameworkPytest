import jsonpickle


def snake_to_camel(string):
    arr = string.split('_')
    arr[0] = arr[0].lower()
    if len(arr) > 1:
        arr[1:] = [u.title() for u in arr[1:]]
    return ''.join(arr)


def all_lower(string):
    arr = string.split('_')
    arr[0] = arr[0].lower()
    return ''.join(arr)


def serialise_json(obj):
    return {snake_to_camel(k): v for k, v in obj.__dict__.items()}


def serialise_lower(obj):
    return {all_lower(k): v for k, v in obj.__dict__.items()}


def encode_json(obj):
    return jsonpickle.encode(obj, unpicklable=False)


def decode_json(obj):
    return jsonpickle.decode(obj)


def clean_nones_from_json(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    if isinstance(value, list):
        return [clean_nones_from_json(x) for x in value if x is not None]
    elif isinstance(value, dict):
        return {
            key: clean_nones_from_json(val)
            for key, val in value.items()
            if val is not None
        }
    else:
        return value

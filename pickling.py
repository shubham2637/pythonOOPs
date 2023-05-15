import pickle


def serialize():
    """
    Serializing python objects
    """
    f = open('pickled.txt', 'wb')
    dct = {"name":"Shubham", "age":23, "Gender":"Male"}
    pickle.dump(dct, f)
    f.close()

def deserialize():
    """
    Serializing python objects
    :return obj:
    """
    f = open('pickled.txt', 'rb')
    dct_obj = pickle.load(f)
    print(dct_obj)
    f.close()

deserialize()
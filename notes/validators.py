'Collection of generally useful data validation utilities'

def validate_percentage(value):
    'Verify a value is an int or float in the range 0 to 100'
    if not isinstance(value, (int, float)):
        raise TypeError('Expected an int or float')
    if value < 0 or value > 100:
        raise ValueError('Expected between 0 and 100')

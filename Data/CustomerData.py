import random
import string


class CustomerData:

    CustomerEmail = "naveenku+" + ''.join(random.choice(string.digits + string.ascii_lowercase) for i in range(8)) + "@adobetest.com"
    FirstName = 'Naveen'.join(random.choice(string.ascii_lowercase) for i in range(8))
    LastName = 'Kumar'.join(random.choice(string.ascii_lowercase) for i in range(8))
    Organization = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
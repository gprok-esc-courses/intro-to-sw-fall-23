# Generate fake yet realistic data
# https://faker.readthedocs.io/en/master/providers.html
# Install by: pip install faker

import faker

f = faker.Faker()

for i in range(10):
    print(f.first_name(),f.last_name(),f.email())
    print(f.profile())
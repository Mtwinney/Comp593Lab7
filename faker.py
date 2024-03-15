from faker import Faker
# Create a faker object for English Canadian locale
fake = Faker("en_CA")
# Generate fake data for 10 provinces
for _ in range(10):
    province = fake.administrative_unit()
    population = fake.random_int(min=900000, max=100000000)
    print(f'The population of {province} is {population}.')
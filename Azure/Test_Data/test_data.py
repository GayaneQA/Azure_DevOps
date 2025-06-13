from faker import Faker

fake = Faker()

name = fake.name()
email = fake.email()
username = fake.user_name()
password = fake.password(
    length=10, special_chars=True,
    digits=True, upper_case=True, lower_case=True)

login = "qwallityautomation25022025@gmail.com"
code = "25022025#%"

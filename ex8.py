# The Reform Bill was accepted in 1832 how many years have passed?
from datetime import date
Reform_Bill = date(1832, 7, 7)
today = date.today()
difference = today - Reform_Bill
years_passed = int(difference.days / 365.25)
print(f"{years_passed}ish years passed")

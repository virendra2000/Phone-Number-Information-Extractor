import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter Your Phone Number with +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print("Your Entered Phone Number : ",phone)
print("Timezone : ",time)
print("Carrier / Service Provider : ",car)
print("Region : ",reg)

from stix2 import TAXIICollectionSource, Filter
from taxii2client import Server, Collection

# Instantiate server and get API Root
taxi_server = Server("https://cti-taxii.mitre.org/taxii/")
api_root = taxi_server.api_roots[0]

# Print name and ID of all ATT&CK technology-domains available as collections
for collection in api_root.collections:
    print(collection.title + ": " + collection.id)

# Initialize dictionary to hold Enterprise ATT&CK content
attack_dict = {}

attack_stix_root_url = "https://cti-taxii.mitre.org/stix/collections/"
attack_enterprise = attack_stix_root_url + api_root.collections[0].id
print(attack_enterprise)

#Establish TAXII2 Collection instance for Enterprise ATT&CK collection
collection = Collection(attack_enterprise)

#Supply the collection to TAXIICollection

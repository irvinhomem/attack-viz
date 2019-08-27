from stix2 import TAXIICollectionSource, Filter
from taxii2client import Server, Collection

# Instantiate server and get API Root
taxi_server = Server("https://cti-taxii.mitre.org/taxii/")
api_root = taxi_server.api_roots[0]

print("------------------------------------------------------------------------")
# Print TAXII Server Information (Title, description, contact, etc):
print("Server Title: " + taxi_server.title)
print("Number of API Roots: " + str(len(taxi_server.api_roots)))
print("API Root [0]: " + str(taxi_server.api_roots[0]))
print("TAXII Server Description: " + str(taxi_server.description))
print("TAXII Server Contacts: " + str(taxi_server.contact))
print("TAXII Server Default API Root: " + str(taxi_server.default))
print("------------------------------------------------------------------------")


# Print name and ID of *all* ATT&CK technology-domains available as collections
for collection in api_root.collections:
    print(collection.title + ": " + collection.id)

print("------------------------------------------------------------------------")

# Initialize dictionary to hold Enterprise ATT&CK content
attack_dict = {}

attack_stix_root_url = "https://cti-taxii.mitre.org/stix/collections/"
attack_enterprise_collection_url = attack_stix_root_url + api_root.collections[0].id + '/'
# Print ATT&CK Enterprise Collection URL
print("ATT&CK Enterprise collection URL: " + attack_enterprise_collection_url)

print("------------------------------------------------------------------------")

#Establish TAXII2 Collection instance for Enterprise ATT&CK collection
Enterprise_collection = Collection(attack_enterprise_collection_url)

#Supply the collection to TAXIICollection
tc_source = TAXIICollectionSource(Enterprise_collection)

print("TAXII Collection Source :" + str(type(tc_source)))

print("------------------------------------------------------------------------")

# Create filters to retrieve content from Enterprise ATT&CK based on type
# filter_objs = {"techniques": Filter("type", "=", "attack-pattern"), # Technique
#                "mitigations": Filter("type", "=", "course-of-action"), # Mitigation
#                "groups": Filter("type", "=", "intrusion-set"), # Group
#                "malware": Filter("type", "=", "malware"), # Software
#                "tools": Filter("type", "=", "tool"), # Software
#                "relationships": Filter("type", "=", "relationship")
#                }
#
# # Retrieve all Enterprise ATT&CK content
# for key in filter_objs:
#     attack_dict[key] = tc_source.query(filter_objs[key])
#
# # For visual purposes, print the first technique received from the server
# print(attack_dict["techniques"][0])

print("------------------------------------------------------------------------")

# # Create filters to retrieve content from Enterprise ATT&CK based on type
# filter_objs = {
#     "techniques": Filter("type", "=", "attack-pattern")
# }

# filter_objs = {
#     "techniques": Filter("type", "=", "kill-chain-phase")
# }

# # Retrieve all Enterprise ATT&CK content
# for key in filter_objs:
#     attack_dict[key] = tc_source.query(filter_objs[key])
#
# # For visual purposes, print the first technique received from the server
# print(attack_dict["techniques"][1])


# ===============================================================================
technique_filter = Filter("type", "=", "attack-pattern")
response = tc_source.query(technique_filter)
print('Type: ' + str(type(response)))
print('--')
print(response[0])
print(response[0]['kill_chain_phases'])
print('Type: ' + str(type(response[0]['kill_chain_phases'])))
print('Len: ' + str(len(response[0]['kill_chain_phases'])))
print('List:' + str(response[0]['kill_chain_phases'][0]))
print(response[0]['kill_chain_phases'][0]['phase_name'])






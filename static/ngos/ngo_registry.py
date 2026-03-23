ngo_list = []

def register_ngo(name, contact, service_area):
    ngo = {"name": name, "contact": contact, "service_area": service_area}
    ngo_list.append(ngo)
    print(f"NGO '{name}' registered successfully.")

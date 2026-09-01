site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iphone',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}


import copy


def display_struct(struct, spaces = 1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(" " * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print(" " * spaces + f"{key}: {value}")


def replace_text(dictionary, old_text, new_text):
    for key, value in dictionary.items():
        if isinstance(value, str):
            dictionary[key] = value.replace(old_text, new_text)
        elif isinstance(value, dict):
            replace_text(value, old_text, new_text)


def create_product_site(product_name):
    new_site = copy.deepcopy(site)
    replace_text(new_site, "телефон", product_name)
    replace_text(new_site, "iphone", product_name)
    return new_site


def print_site(site_data):
    print("site = {")
    display_struct(site_data)
    print("}")


def print_all_sites(site_catalog):
    for product_site in site_catalog:
        print_site(product_site)
        print()


all_sites = []
quantity = int(input("Сколько сайтов: "))

for site_quantity in range(quantity):
    product_name = input("Введите название для нового сайта: ")
    new_site = create_product_site(product_name)
    all_sites.append(new_site)
    
    print(f"\nСайт для {product_name}:")
    print_all_sites(all_sites)
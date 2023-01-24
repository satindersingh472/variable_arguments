def print_order(*order_items):
    print(order_items)

print_order("apple juice","orange juice","pancakes")


tables={
    1: {
        "name": "satinder",
        "vip_status": True,
        "order": "apple juice, Orange juice"
    },
    2: {

    },
    3: {

    },
    4: {}
}


def assign_table(table_number, name, vip_status,*order_items):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = order_items

    print(tables)

assign_table(2,"sam",True,"orange juice","apple juice")
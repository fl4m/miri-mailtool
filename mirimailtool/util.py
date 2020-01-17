import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def filter_addresses(addr_str, remove_str='', sep=';'):
    """
    Email address filtering.
    
    Each valid email address from the list which isn't in the remove list is
    returned. Duplicates are removed.
    Additionally, statistics are generated to show the number of addresses and
    duplicates in each field.
    """
    addr_list = addr_str.split(sep)
    if addr_list == ['']: addr_list = []
    
    remove_list = remove_str.split(sep)
    if remove_list == ['']: remove_list = []
    
    remove_set = {
        addr.strip() for addr in remove_list if EMAIL_REGEX.match(addr)
    }
    addr_set = {
        addr.strip() for addr in addr_list if EMAIL_REGEX.match(addr)
    }
    
    stats = { 
        'addrs': {'count': len(addr_set), 'dup': len(addr_list)-len(addr_set)}, 
        'remove': {'count': len(remove_set), 'dup': len(remove_list)-len(remove_set)}, 
        'res': {'count': 0} 
    }

    addr_set -= remove_set
    stats['res']['count'] = len(addr_set)
    return (addr_set, stats)

def union_addresses(addr_str, join_str='', sep=';'):
    """
    Email address union

    Joins two lists of addresses.
    Filter duplicates.
    """

    if (len(join_str) > 0):
        addr_str += sep + join_str;

    return filter_addresses(addr_str, sep=sep)
    

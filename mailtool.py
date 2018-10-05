import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def filter_addresses(new_str, old_str, sep=';'):
    """
    Email address filtering.
    
    Each valid email address which exists in the 'old' list but not in the 'new'
    is returned. Duplicates are removed.
    """
    old = old_str.split(sep)
    new = new_str.split(sep)
    
    new_set = {addr.strip() for addr in new if EMAIL_REGEX.match(addr)}
    ret_set = {addr.strip() for addr in old if EMAIL_REGEX.match(addr)}
    ret_set -= new_set
    
    return ret_set
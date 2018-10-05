from mirimailtool.util import filter_addresses

def test_address_verification():
    """Tests if wrongly formatted addresses are filtered out."""
    addrs = 'this_isnt_an_address; this-neither; i@dontknow'
    res, stats = filter_addresses(addrs)
    assert len(res) == 0
    
def test_duplicate_removal():
    """Tests if duplicate entries are removed."""
    addr = 'test@test.com'
    addrs = [addr, addr, addr]
    res, stats = filter_addresses('; '.join(addrs))

    # duplicates
    assert len(res) == 1
    
    # statistics
    assert stats['addrs']['count'] == 1
    assert stats['addrs']['dup'] == 2
    assert stats['res']['count'] == 1
    
def test_address_filtering():
    """Tests if the addresses from the removal list are ignored."""
    addrs = 'a.b@c.de;test@test.com;me@you.org'
    remove = 'me@you.org'
    res, stats = filter_addresses(addrs, remove)
    
    # addresses
    assert len(res) == 2
    assert 'a.b@c.de' in res
    assert 'test@test.com' in res
    
    # stats
    expected = {
        'addrs': {'count': 3, 'dup': 0},
        'remove': {'count': 1, 'dup': 0},
        'res': {'count': 2}
    }
    assert stats == expected
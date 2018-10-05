from mirimailtool import create_app

def test_config():
    """Test different configurations"""
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    """Tests if the index template is properly returned"""
    response = client.get("/")

    assert response.status_code == 200
    assert b'Mail-Verteiler generieren' in response.data

def test_warning_alert(client):
    """Test if an alert is displayed when posting no data"""
    response = client.post('/', data={'new-addr':'', 'old-addr': ''})
    
    assert response.status_code == 200
    assert b'alert-warning' in response.data
    
def test_success(client):
    """Test if the result is displayed properly."""
    data = {
        'new-addr': '',
        'old-addr': 'a.b@c.de'
    }
    response = client.post('/', data=data)
    
    assert response.status_code == 200
    assert b'alert-success' in response.data
    assert b'a.b@c.de' in response.data
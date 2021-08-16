from sharedprojectQSTC.lib import try_me

def test_try_me():
    user='Gerard'
    assert try_me(user)=='Hello Gerard'

from weather import get_weather

def test_get_weather():
    assert get_weather(21) == "hot" 
    #assert is going to tell us if something is true or false
    #This gives a sucess, if "cold" it will fail because then the condition isnt true.
    assert get_weather(10) == "cold"
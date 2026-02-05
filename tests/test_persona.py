from honeypot.persona import DecoyPersona
def test_persona_response_is_string():
    persona = DecoyPersona()
    response = persona.respond("Your account will be blocked")
    assert isinstance(response, str)
    assert len(response) > 0

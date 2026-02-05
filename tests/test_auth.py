import yaml
from honeypot.auth import APIKeyAuth
def test_valid_api_key(tmp_path, monkeypatch):
    # Create a temporary config.yaml
    config_file = tmp_path / "config.yaml"
    config_file.write_text("""
security:
  api_key: "TEST_KEY"
  expiry_days: 30
""")
    monkeypatch.chdir(tmp_path)
    auth = APIKeyAuth()
    assert auth.is_valid("TEST_KEY") is True
def test_invalid_api_key(tmp_path, monkeypatch):
    config_file = tmp_path / "config.yaml"
    config_file.write_text("""
security:
  api_key: "TEST_KEY"
  expiry_days: 30 
""")
    monkeypatch.chdir(tmp_path)
    auth = APIKeyAuth()
    assert auth.is_valid("WRONG_KEY") is False
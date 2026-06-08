from unittest.mock import MagicMock, patch

from src.api_adapter import APIAdapter


@patch("src.api_adapter.get")
def test_get_aeroplanes(mock_get):

    nominatim_response = MagicMock()
    nominatim_response.json.return_value = [{"boundingbox": ["10.0", "20.0", "30.0", "40.0"]}]

    opensky_response = MagicMock()
    opensky_response.json.return_value = {"states": [[None, "ABC123", None, None, None, None, None, 10000, None, 250]]}

    mock_get.side_effect = [
        nominatim_response,
        opensky_response,
    ]

    api = APIAdapter()
    api.get_aeroplanes("Canada")

    assert api.aeroplanes is not None
    assert "states" in api.aeroplanes
    assert len(api.aeroplanes["states"]) == 1

from unittest.mock import MagicMock, patch

from src.api_adapter import APIAdapter


@patch("src.api_adapter.get")
def test_get_aeroplanes(mock_get):

    mock_response = MagicMock()

    # ✔ ВАЖНО: это ДОЛЖЕН БЫТЬ список, а не dict
    mock_response.json.return_value = [{"boundingbox": ["10.0", "20.0", "30.0", "40.0"]}]

    mock_get.return_value = mock_response

    api = APIAdapter()
    api.get_aeroplanes("Canada")

    assert api.aeroplanes is not None

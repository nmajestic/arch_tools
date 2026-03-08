"""Tests for the AUR helper detection service."""

from unittest.mock import patch, MagicMock

from src.services.aur_helper_service import get_aur_helper


def test_get_aur_helper_paru():
    """Test that paru is returned when pacman reports it as installed."""
    with patch("subprocess.run") as mock_subprocess_run:
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess_run.return_value = mock_result

        result = get_aur_helper()
        assert result == "paru"


def test_get_aur_helper_yay():
    """Test that yay is returned when paru is absent but yay is installed."""
    with patch("subprocess.run") as mock_subprocess_run:
        mock_subprocess_run.side_effect = [
            MagicMock(returncode=1),
            MagicMock(returncode=0),
        ]

        result = get_aur_helper()
        assert result == "yay"


def test_get_aur_helper_none():
    """Test that None is returned when neither paru nor yay is installed."""
    with patch("subprocess.run") as mock_subprocess_run:
        mock_subprocess_run.side_effect = [
            MagicMock(returncode=1),
            MagicMock(returncode=1),
        ]

        result = get_aur_helper()
        assert result is None

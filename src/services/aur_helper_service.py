"""Service for detecting installed AUR helpers on Arch Linux."""

import subprocess


def get_aur_helper():
    """Detect which AUR helper is installed on the system.

    Queries pacman for the presence of paru or yay, in that order of
    preference. paru is checked first as it is the more actively maintained
    fork of yay.

    Returns:
        str: The name of the detected AUR helper ("paru" or "yay").
        None: If no supported AUR helper is found.
    """
    paru_result = subprocess.run(
        ["pacman", "-Qq", "paru"], capture_output=True, check=False
    )
    yay_result = subprocess.run(
        ["pacman", "-Qq", "yay"], capture_output=True, check=False
    )

    if paru_result.returncode == 0:
        return "paru"
    if yay_result.returncode == 0:
        return "yay"
    return None

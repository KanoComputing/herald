# start_internet_available_user.py
#
# Copyright (C) 2019 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Main program for start-user-internet-available script.


import os

from herald.utils import start_user_target_for_all_users


def main():
    """Main function for start-internet-available-user script."""

    # Ensure this script is running as root.
    if os.getuid() != 0:
        return 10

    # Note: At the moment, it's expected there will only be a single user
    # logged in at any one time.
    successful = start_user_target_for_all_users(
        'internet-available-user.target'
    )
    return 0 if successful else 1

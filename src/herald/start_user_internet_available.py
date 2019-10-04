# start_internet_available_user.py
#
# Copyright (C) 2019 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Main program for start-user-internet-available script.


import os

from herald.utils import get_logged_in_users, start_user_target


def start_internet_available_user_target(user):
    """Start the internet-available-user.target for a given user."""

    return start_user_target('internet-available-user.target', user)


def start_internet_available_user_target_for_all_users():
    """
    Start the internet-available-user.target for all currently
    logged in users.
    """

    users = get_logged_in_users()
    users.discard('root')

    successful = True

    for user in users:
        rc = start_internet_available_user_target(user)
        successful &= (rc == 0)

    return successful


def main():
    """Main function for start-internet-available-user script."""

    # Ensure this script is running as root.
    if os.getuid() != 0:
        return 10

    # Note: At the moment, it's expected there will only be a single user
    # logged in at any one time.
    successful = start_internet_available_user_target_for_all_users()
    return 0 if successful else 1

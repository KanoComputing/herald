# utils.py
#
# Copyright (C) 2019 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Utility functions for the project.


from kano.utils.shell import run_cmd, run_cmd_log


def get_logged_in_users():
    """Get a set of currently logged in users."""

    out, err, rc = run_cmd("who --users | awk '{print $1}'")
    if rc != 0:
        return None

    return set(out.strip().split())


def start_user_target(target, user):
    """Start a user systemd target for a given logged in user."""

    dummy, dummy, rc = run_cmd_log(
        "sudo su -c 'systemctl --user restart {target}' - {user}"
        .format(target=target, user=user)
    )
    return rc

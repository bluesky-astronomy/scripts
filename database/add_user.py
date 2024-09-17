"""Manually adds an account to the feeds."""

from astrofeed_lib.accounts import fetch_dids
from astrofeed_lib.database import Account, db


# List of all account names to add.
ACCOUNTS_TO_ADD = ["glifencible.bsky.social"]


# Perms to give the new accounts (both True by default)
IS_VALID = True
FEED_ALL = True


def account_exists_already(handle_did_pairs: dict):
    """Checks if certain accounts are already in the database."""
    dids_to_check = list(handle_did_pairs.values())
    existing_dids = [
        x.did for x in Account.select().where(Account.did << dids_to_check)
    ]

    if existing_dids:
        raise_prexisting_handles_as_error(handle_did_pairs, existing_dids)

    print(f"-> 0 / {len(handle_did_pairs)} DIDs exist in the DB already!")


def raise_prexisting_handles_as_error(handle_did_pairs, existing_dids):
    """Raises an error including all handles that exist already."""
    did_handle_pairs = reverse_dict(handle_did_pairs)
    existing_handles_string = ", ".join(
        [did_handle_pairs[did] for did in existing_dids]
    )
    raise ValueError(
        f"Some accounts are already in the database: {existing_handles_string}"
    )


def reverse_dict(handle_did_pairs):
    """Reverses a dictionary. Source: https://stackoverflow.com/a/483833"""
    return {v: k for k, v in handle_did_pairs.items()}


if __name__ == "__main__":
    # Fetch DIDs and ensure that they aren't in the DB
    print("Fetching DIDs for handles from Bluesky")
    did_dict = fetch_dids(ACCOUNTS_TO_ADD)

    print("Checking that DIDs not in database already")
    account_exists_already(did_dict)

    print("Creating accounts")
    with db.atomic():
        for handle, did in did_dict.items():
            print("CREATING USER", handle, "WITH DID =", did)
            Account.create(handle=handle, did=did, is_valid=IS_VALID, feed_all=FEED_ALL)

"""Sets the moderators on the feed"""

from astrofeed_lib.database import Account

"""DESCRIPTION OF MOD LEVELS:

5: Admin. This is ONLY for emily.space. Allows all actions.
4: Developer. Same as admin except for maybe a few very niche things.
3: Senior moderator. All mod actions.
2: Moderator. Almost all mod actions.
1: Junior moderator. Can validate signups. No banning/muting.

Mods cannot act on mod levels higher than them.
"""


MODERATORS = {
    "did:plc:jcoy7v3a2t4rcfdh6i4kza25": 5  # emily.space
}


def print_current_moderators(min_level=1):
    current_moderators = Account.select(
        Account.handle, Account.did, Account.mod_level
    ).where(Account.mod_level >= min_level)
    for moderator in current_moderators.execute():
        print(f"{moderator.handle}: {moderator.mod_level}  ({moderator.did})")


def update_moderators():
    print("Executing update...")
    for user in Account.select().where(Account.did << list(MODERATORS.keys())).execute():
        if user.mod_level != MODERATORS[user.did]:
            print("Updating", user.handle)
            user.mod_level = MODERATORS[user.did]
            user.save()
        else:
            print(user.handle, "already has correct level")


if __name__ == "__main__":
    print("Current moderators:")
    print_current_moderators()
    print("")
    update_moderators()
    print("")
    print("New moderators:")
    print_current_moderators()

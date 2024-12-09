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


# "did : level" dict of feed moderators, sorted by level and then alphabetically.
MODERATORS = {
    "did:plc:jcoy7v3a2t4rcfdh6i4kza25": 5,  # emily.space
    "did:plc:iaterevirjtn4sh2o2ykqyak": 3,  # celtuk.bsky.social (Chris)
    "did:plc:4kb66qy7xqqprdeopyzwvlms": 3,  # kwcookastro.bsky.social (Kyle)
    "did:plc:4aa2mtfyjewhfg7uinr7hti4": 3,  # mpoessel.de (Markus)
    "did:plc:curm4ncx66fzzygplesli77a": 1,  # jamiezvirzdin.com (Jamie)
    "did:plc:3wghkixdyfxcdqjw6bpnsn6b": 1,  # noelstoj.bsky.social (Jake N)
    "did:plc:uzecijkzuq4b7yjiwdg4b52i": 1,  # jakepost.tech (Jake P)
    "did:plc:54qsxdbgcjs47qqm7phoapyn": 1,  # epsori.bsky.social (Jerry)
    "did:plc:32jhd3zbo5zlj5yc5lcyf7rt": 1,  # kellylepo.bsky.social (Kelly)
    "did:plc:toptt6pljgctu63uwv26yb2w": 1,  # nrutkowski.bsky.social (Nathaniel )
    "did:plc:jcedpw4itvgtr42x4nizr33w": 1,  # naztronomy.bsky.social (Naz)
    # "did:plc:mspg53rhq553n65o5fa7gyrf": 1,  # cosmicrami.com (Rami)
    "did:plc:w6m2zca3mkact4znrc55gfdl": 1,  # spacemarschall.net (Raphael)
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

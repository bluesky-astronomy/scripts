"""Tool for adding a column(s) to the database."""

from astrofeed_lib.database import db, Account, Post, SubscriptionState, BotActions, ModActions
from playhouse.migrate import migrate, MySQLMigrator, IntegerField
from playhouse.reflection import print_model


def print_current_database_model():
    print("CURRENT DATABASE MODEL:")
    print_model(Account)
    print("\n-----------\n")
    print_model(Post)
    print("\n-----------\n")
    print_model(SubscriptionState)
    print("\n-----------\n")
    print_model(BotActions)
    print("\n-----------\n")
    print_model(ModActions)


def migrate_2024_06_22():
    """Tasks for migration on 22/06/2024"""
    migrator = MySQLMigrator(db)

    # All new columns
    mod_level = IntegerField(null=False, index=True, unique=False, default=0)

    migrate(
        # Add an index on DID - is stupid that there isn't one
        # migrator.add_index("account", ("did",), unique=False),

        # Add a moderator level field & index it
        migrator.add_column("account", "mod_level", mod_level),
    )


if __name__ == "__main__":
    print_current_database_model()
    # migrate_2024_06_22()
    # print_current_database_model()


    

    

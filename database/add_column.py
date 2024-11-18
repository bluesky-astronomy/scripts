"""Tool for adding a column(s) to the database."""

from astrofeed_lib.database import (
    db,
    Account,
    Post,
    SubscriptionState,
    BotActions,
    ModActions,
)
from playhouse.migrate import migrate, MySQLMigrator, IntegerField, BooleanField, DateTimeField
from playhouse.reflection import print_model
from datetime import datetime


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


def migrate_2024_08_05():
    """Tasks for migration on 05/08/2024"""
    migrator = MySQLMigrator(db)

    # All new columns
    authorized = BooleanField(null=False, index=True, default=True)

    migrate(
        # Add an index on DID - is stupid that there isn't one
        # migrator.add_index("account", ("did",), unique=False),
        # Add a moderator level field & index it
        migrator.add_column("botactions", "authorized", authorized),
    )


def migrate_2024_08_20():
    """Tasks for migration on 05/08/2024"""
    migrator = MySQLMigrator(db)

    migrate(
        # Add an index on DID - is stupid that there isn't one
        migrator.add_index("account", ("did",), unique=False),
        migrator.add_index("account", ("is_valid",), unique=False),
        migrator.add_index("post", ("author",), unique=False),
        migrator.add_index("post", ("indexed_at",), unique=False),
        migrator.add_index("post", ("feed_all",), unique=False),
        migrator.add_index("post", ("feed_astro",), unique=False),
        migrator.add_index("post", ("feed_exoplanets",), unique=False),
        migrator.add_index("post", ("feed_astrophotos",), unique=False),
    )


def migrate_2024_09_12():
    """Tasks for migration on 12/09/2024"""
    migrator = MySQLMigrator(db)

    migrate(
        migrator.add_column(
            "post",
            "feed_cosmology",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_extragalactic",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_highenergy",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_instrumentation",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_methods",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_milkyway",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_planetary",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_radio",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_stellar",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_education",
            BooleanField(null=False, index=True, default=False),
        ),
        migrator.add_column(
            "post",
            "feed_history",
            BooleanField(null=False, index=True, default=False),
        ),
    )


def migrate_2024_11_18():
    """Add an extra column to BotActions."""
    migrator = MySQLMigrator(db)

    migrate(
        migrator.add_column(
            "botactions",
            "checked_at",
            DateTimeField(null=False, index=True, default=datetime.utcnow),
        ),
    )



if __name__ == "__main__":
    print_current_database_model()
    # migrate_2024_06_22()
    # migrate_2024_08_05()
    # migrate_2024_08_20()
    # migrate_2024_09_12()
    migrate_2024_11_18()
    # print_current_database_model()

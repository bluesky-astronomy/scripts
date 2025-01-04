from astrofeed_lib.dev_database import build_dev_db
import shutil



build_dev_db("../data/database_backup", overwrite_existing=True)
shutil.move("./dev_db.db", "../data/devdb.db")

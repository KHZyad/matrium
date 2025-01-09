import os

class Config:
    # Database URI for deployment on Aiven
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://avnadmin:AVNS_64D7XhVDVS5mweyqAHs@mysql-615390b-matrium-24.h.aivencloud.com:21017/mrp'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os


default_name = "DefaultIni"
default_period = 10


class Config:
    name = os.getenv('name') if os.getenv('name') else default_name
    period = os.getenv('period') if os.getenv('period') else default_period
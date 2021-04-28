import os, sys
import logging.config
from dependency_injector import containers, providers
from apps.example_module.example import Example


class Containers(containers.DeclarativeContainer):
    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.fileConfig,
        fname=os.path.join(os.getcwd(), "logging.ini")
    )

    # declare objects initialize

    example_instance = providers.Singleton(
        Example,
        name=config.name,
        period=config.period
    )

    # or factory initail instance
    # example_instance = providers.Factory(
    #     Example,
    #     name=config.name,
    #     period=config.period
    # )

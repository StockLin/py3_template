import os, sys
import logging
from dependency_injector.wiring import inject, Provide
from containers import Containers
from config import Config
from apps.example_module.example import IExample


@inject
def main(example:IExample=Provide[Containers.example_instance]):
    example.run()


if __name__ == "__main__":
    try:
        container = Containers()
        container.init_resources()
        container.config.from_dict(
            {
                "name": Config.name,
                "period": Config.period
            } 
        )

        logging.warning(f"start main service.")

        container.wire(modules=[sys.modules[__name__]])
        main(*sys.argv[1:])

    except KeyboardInterrupt:
        logging.warning("KeyboardInterrupt in main.")

    except Exception as e:
        logging.error(f"unexcepted error...... {str(e)}")
        raise e
from pythonjsonlogger import jsonlogger
from datetime import datetime
from uuid import uuid4
import traceback
import logging

from project.config import get_settings
config = get_settings()


#########################
# all records available
#########################
# records = "%(asctime)s %(created)f %(filename)s %(funcName)s %(levelname)s " \
#           "%(levelno)s %(lineno)d %(message)s %(module)s %(msecs)d %(name)s " \
#           "%(pathname)s %(process)d %(processName)s %(relativeCreated)d " \
#           "%(thread)d %(threadName)s"


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    Custom Json Formatter to use with CloudLogging (GCP)
    """
    def add_fields (self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['insertId'] = str(uuid4())
        log_record['timestamp'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        log_record['severity'] = record.levelname
        log_record['exc_info'] = traceback.format_exc()


records = "$(insertId)s %(timestamp)s %(name)s %(severity)s %(message)s %(filename)s %(funcName)s %(exc_info)s"


def config_logs(format_: str = records, debug: bool = True, app_name: str = config.APP_NAME):
    formatter = CustomJsonFormatter(format_)
    logHandler = logging.StreamHandler()
    logHandler.setFormatter(formatter)

    log = logging.getLogger(app_name)
    log.handlers.clear()
    log.addHandler(logHandler)
    log.setLevel(logging.DEBUG if debug else logging.WARN)

    log = logging.getLogger('sqlalchemy')
    log.handlers.clear()
    log.addHandler(logHandler)
    log.setLevel(logging.WARN)

    log = logging.getLogger('fastapi')
    log.handlers.clear()
    log.addHandler(logHandler)
    log.setLevel(logging.DEBUG if debug else logging.WARN)

    # for name in logging.root.manager.loggerDict:
    #     log = logging.getLogger(name)
    #     log.handlers.clear()
    #     log.addHandler(logHandler)
    #     log.setLevel(logging.DEBUG if debug else logging.WARN)

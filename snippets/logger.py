import logging.config


logger = logging.getLogger(__name__)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'stream_handler': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
        },
        'rotating_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'errors.log',
            'maxBytes': 1000,
            'backupCount': 5,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['stream_handler', 'rotating_file_handler'],
            'level': 'DEBUG'
        }
    }
})

# inclass_logger_name = self.__class__.__name__

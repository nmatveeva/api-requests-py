import logging
import sys

import pytest
from reportportal_client import RPLogger, RPLogHandler

from utils.file_reader import read_json_file
import random


@pytest.fixture
def create_data():
    payload = read_json_file('create_user.json')

    random_no = random.randint(0, 1000)
    last_name = f'LastName{random_no}'

    payload['lname'] = last_name
    yield payload


@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)

        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)

    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger

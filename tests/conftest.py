#!/usr/bin/python3

import pytest

@pytest.fixture(scope="session")
def LOBContract(accounts, project):
    return accounts[0].deploy(project.limit_order, accounts[0])

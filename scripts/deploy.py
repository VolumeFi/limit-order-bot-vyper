from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    contract = acct.deploy(project.limit_order)
    return contract
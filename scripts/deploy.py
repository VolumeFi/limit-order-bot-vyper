from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    COMPASS_EVM = "0x24B10a62385C2d04F3f04Dd55297ADD7b4502530"
    contract = acct.deploy(project.limit_order, COMPASS_EVM)
    return contract
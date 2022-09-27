from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    COMPASS_EVM = "0x6D727250bd150A9dC006b65b6C7a0D817B02bB2e"
    contract = acct.deploy(project.limit_order, COMPASS_EVM)
    return contract
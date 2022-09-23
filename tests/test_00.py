#!/usr/bin/python3

from conftest import *
import ape
import math

def test_deposit(LOBContract, accounts, project):
    
    pool = project.UniswapV3Pool.at("0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640")
    weth = project.WETH.at("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")

    upper_tick = int(pool.slot0()[1] / 10) * 10
    lower_tick = upper_tick - 100
    lower_sqrt_price_x96 = tick2sqrtpricex96(lower_tick)
    deadline = 9999999999
    receipt = LOBContract.deposit(lower_tick, lower_sqrt_price_x96, upper_tick, deadline, sender=accounts[0], value=10**17)
    token_id = 0
    for log in LOBContract.Deposited.from_receipt(receipt):
        token_id = log.token_id
    print(token_id)
    with ape.reverts():
        LOBContract.cancel(token_id, sender=accounts[1])
    deadline = 0
    receipt = LOBContract.deposit(lower_tick, lower_sqrt_price_x96, upper_tick, deadline, sender=accounts[0], value=10**17)
    for log in LOBContract.Deposited.from_receipt(receipt):
        token_id = log.token_id
    print(token_id)
    LOBContract.cancel(token_id, sender=accounts[1])
    binance = accounts["0x28C6c06298d514Db089934071355E5743bf21d60"]

    # usdc = project.USDC.at("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
    # print(usdc.balanceOf(binance.address))


def tick2sqrtpricex96(tick):
    return int(math.sqrt(1.0001 ** tick) * (1 << 96))

def sqrtpricex962tick(sqrtpricex96):
    return int(math.log((sqrtpricex96 / (1 << 96)) ** 2, 1.0001))
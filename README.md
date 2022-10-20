# Limit Order Bot Vyper

## ApeWorx installation

```sh
pipx install eth-ape
ape plugins install infura vyper etherscan
```

## Test

```sh
ape test
```

## Add account

```sh
ape accounts import deployer_account
```

## Deploy on mainnet
Edit Compass-EVM contract address in `scripts/deploy.py`.
```sh
ape run deploy --network :mainnet:infura
```

## Functions

### deposit

Deposit WETH token with expected price information(tick in Uniswap V3, SqrtPriceX96, etc) and deadline. This emits event and Paloma will collect events from this smart contract and register information to CosmWasm smart contract on Paloma.

| Key                  | Type    | Description                                                |
|----------------------|---------|------------------------------------------------------------|
| depositor            | address | Orderer address who already approved WETH to this contract |
| amount               | uint256 | Ordering amount                                            |
| lower_tick           | int24   | tick of expected price in Uniswap V3                       |
| lower_sqrt_price_x96 | uint256 | sqrtpricex96 of expected price in Uniswap V3               |
| deadline             | uint256 | deadline of limit-order                                    |

### withdraw

Withdraw WETH and USDC of the order which reaches to the expected price.

| Key     | Type    | Description                                  |
|---------|---------|----------------------------------------------|
| tokenId | uint256 | Uniswap V3 token ID of the order to withdraw |

### multiple_withdraw

Withdraw WETH and USDC of the order which reaches to the expected price.

| Key      | Type      | Description                                    |
|----------|-----------|------------------------------------------------|
| tokenIds | uint256[] | Uniswap V3 token IDs of the orders to withdraw |

### cancel

Cancel order.

| Key     | Type    | Description                                |
|---------|---------|--------------------------------------------|
| tokenId | uint256 | Uniswap V3 token ID of the order to cancel |

### multiple_cancel

Cancel orders

| Key      | Type      | Description                                    |
|----------|-----------|------------------------------------------------|
| tokenIds | uint256[] | Uniswap V3 token IDs of the orders to withdraw |

### update_admin

Update admin address.

| Key       | Type    | Description       |
|-----------|---------|-------------------|
| new_admin | address | New admin address |

### update_compass_evm

Update Compass-EVM address.

| Key             | Type    | Description       |
|-----------------|---------|-------------------|
| new_compass_evm | address | New admin address |
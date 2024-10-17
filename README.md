# Ethereum Account Balance and Transaction Lookup
This Python script fetches the Ethereum account balance and displays transaction details for a given Ethereum address using the Etherscan API. It provides essential information about the balance and past transactions, including value, gas usage, and timestamps.

### Features
- Account Balance: Retrieves the current balance of an Ethereum address.
- Transaction History: Lists transactions (with a user-specified limit) including details like:
- Transaction hash
- Sender and receiver addresses
- Transaction value (in ETH)
- Status and gas used
- Timestamp of the transaction
- API Integration: Utilizes the Etherscan API for fetching balance and transaction data.

### Prerequisites
To run this script, you need to have the following installed:

- Python 3.x
- Requests: You can install it by running:
  ```bash
  pip install requests
- Matplotlib: If you wish to extend with balance plotting, install using:
  ```bash
  pip install matplotlib

You will also need an API key from [Etherscan API](https://etherscan.io/apis).

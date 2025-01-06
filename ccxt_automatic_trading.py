# Pip install ccxt
import ccxt

# Authentication
dex =ccxt.hyperliquid({
    "walletAddress" = "0xa95625212Bf25FC326d8EbF6743c649a39EeC07b",
    "privateKey = "0xe12481c02dc70cc3bd0a62cd3e6ad3415f3fdb3e6ffd97d38856deb982552f07",
})

dex.fetch_balance()

# Market order 
symbol = "ETH/USDC:USDC" #futures
order_type = "market"
side = "buy"
amount = 0.01 #given in base asset
price = dex.load_markets()["ETH/USDC:USDC"]["Info"]["midPx"]

## Open a position (symbol, order_type, side, amount, price)
dex.create_order(symbol, order_type, side, amount, price=price)

## Load Market
dex.load_markets()

# Fetch open positions
symbol = "ETH/USDC:USDC"
dex.fetch_positions()

# Close position
symbol = "ETH/USDC:USDC"
market_type = "market"
side = "sell"
amount = dex.fetch_positions([symbol])[0]]["contracts"]
price = dex.load_markets()["ETH/USDC:USDC"]["info"]["midPx"]
dex.create_order(symbol, order_type, side, amount, price=price, params={"reduceOnly":True})

# Limit order
symbol = "ETH/USDC:USDC"
market_type = "limit"
side = "buy"
amount = 0.01
price = 3300
order = dex.create_order(symbol, order_type, side, amount, price=price)
print(order)

symbol = "ETH/USDC:USDC"
order_id = order["id"]
dex.cancel_order(order_id, symbol)
dex.fetch_open_orders("ETH/USDC:USDC)

# set leverage and mode







    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gdAhB1RlLlDc"
      },
      "outputs": [],
      "source": [
        "usdt_available = exchange.fetchBalance()['USDT']['free']\n",
        "print(usdt_available)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BCbiru_pp1-V"
      },
      "source": [
        "<h1>Load Markets</h1>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZqmRXvC8p1-X"
      },
      "outputs": [],
      "source": [
        "markets = exchange.loadMarkets()\n",
        "print(markets)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "scrolled": true,
        "id": "EZ5pWoWWLlDe"
      },
      "outputs": [],
      "source": [
        "print(exchange.loadMarkets()['BTC/USDT'])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3EwiqqI_LlDe"
      },
      "source": [
        "<h1>Fetch ticker</h1>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RapT_P8LLlDf"
      },
      "outputs": [],
      "source": [
        "ticker = exchange.fetchTicker('ADA/USDT')\n",
        "print(ticker)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N-l9pGO0LlDf"
      },
      "outputs": [],
      "source": [
        "print('Bid price is', ticker['bid'], 'USDT')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "u8sIwdzpp1-Y"
      },
      "source": [
        "<h1>Place Orders</h1>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TmWuXIkjLlDf"
      },
      "outputs": [],
      "source": [
        "symbol = 'ADA/USDT'\n",
        "order_type = 'limit'\n",
        "side = 'buy'\n",
        "\n",
        "base_price = 0.1  # The price at which you want to buy or sell\n",
        "\n",
        "amount_in_usdt = 10.\n",
        "# amount_in_usdt = usdt_available / 2.\n",
        "current_price = (exchange.fetchTicker(symbol)['ask'] + exchange.fetchTicker(symbol)['bid'] ) / 2\n",
        "amount = amount_in_usdt / current_price\n",
        "\n",
        "order = exchange.createOrder(symbol, order_type, side, amount, base_price)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yt5dLuSBp1-Y"
      },
      "outputs": [],
      "source": [
        "print(order)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q3_a2nlXLlDh"
      },
      "source": [
        "<h1>Fetch Orders</h1>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "C773cdvuLlDh"
      },
      "outputs": [],
      "source": [
        "order_status = exchange.fetchOrder(order['id'])\n",
        "print(order_status)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "trqnZSx_LlDh"
      },
      "source": [
        "<h1>Cancel Orders</h1>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vrzs5gJWLlDh"
      },
      "outputs": [],
      "source": [
        "exchange.cancelOrder(order['id'], symbol)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.12"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}

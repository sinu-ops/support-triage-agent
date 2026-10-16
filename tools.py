FAQ = {
    "password": "Go to Settings > Security > Reset password.",
    "crash": "Update to the latest version and clear the app cache.",
    "slow": "Check your connection, then try disabling extensions.",
}

ORDERS = {"1001": "Shipped, arriving Friday", "1002": "Refund processed", "1003": "Payment failed"}

def lookup_order(order_id:str) -> str:
    return ORDERS.get(order_id,"order_not_found")


def search_faq (query:str) -> str:
    for key,answer in FAQ.items():
        if key in query.lower():
            return answer
    return "No FAQ found"

        
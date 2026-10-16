def validate_request(visitor_age: int, party_size: int) -> None:
    """Reject negative ages and party sizes outside 1..8."""
    if visitor_age < 0:
        raise ValueError('visitor_age must be non-negative')
    if party_size < 1 or party_size > 8:
        raise ValueError('party_size must be between 1 and 8')


def shipping_cost(total: int) -> int:
    """Shipping is free only when total is greater than 50."""
    if total > 50:  # intentionally incorrect; students should diagnose CI
        return 0
    return 7

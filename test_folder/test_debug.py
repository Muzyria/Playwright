
import pytest_mock


import pytest
from pydantic import ValidationError

from app import Customer, Order


def test_valid():
    order = Order(id="100",
                  customer=Customer(
                      id="1",
                      name="Alex",
                      email="alex@example.com"),
                  items=["item1", "item2"],
                  price=1000,
                  discount=100
                  )

    assert "id" in order.model_dump(by_alias=True)
    assert "id" in order.model_dump(by_alias=True)["customer"]


def test_invalid_1():
    with pytest.raises(ValidationError, match="discount < price"):
        order = Order(id="100",
                      customer=Customer(
                          id="1",
                          name="Alex",
                          email="alex@example.com"),
                      items=["item1", "item2"],
                      price=1000,
                      discount=10000
                      )



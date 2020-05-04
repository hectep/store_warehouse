import pytest
from mixer.backend.django import mixer

from warehouse.celery import app
from unittest.mock import patch


pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture(scope='module')
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)
    return app


def test_new_orders_are_not_sent_to_store_via_celery(celery_app):
    with patch('core.tasks.update_order_in_store.delay') as task:
        mixer.blend('core.Order')
        assert not task.called


def test_updated_orders_are_sent_to_store(celery_app):
    order = mixer.blend('core.Order')
    with patch('core.tasks.update_order_in_store.delay') as task:
        order.order_name = 'test'
        order.save()
        assert task.called

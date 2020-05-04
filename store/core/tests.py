import pytest
from mixer.backend.django import mixer

from store.celery import app
from unittest.mock import patch


pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture(scope='module')
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)
    return app


def test_new_orders_are_sent_to_warehouse_via_celery(celery_app):
    with patch('core.tasks.send_created_order.delay') as task:
        mixer.blend('core.Order')
        assert task.called


def test_updated_orders_are_not_sent_to_warehouse(celery_app):
    order = mixer.blend('core.Order')
    with patch('core.tasks.send_created_order.delay') as task:
        order.order_name = 'test'
        order.save()
        assert not task.called

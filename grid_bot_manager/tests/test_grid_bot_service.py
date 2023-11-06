## tests/test_grid_bot_service.py
import pytest
from grid_bot_manager.models import User, Bot
from grid_bot_manager.services.grid_bot_service import GridBotService

@pytest.fixture
def user():
    return User(username='test', password='test')

@pytest.fixture
def bot(user):
    return Bot(exchange='kucoin', symbol='BTC/USDT', lower_price=30000.0, upper_price=40000.0, grid_levels=10, user=user)

def test_start_bot(bot):
    GridBotService.start_bot(bot)
    assert bot.status is not None, "Bot status should not be None after starting the bot"

def test_update_bot_status(bot):
    service = GridBotService(bot)
    service.update_bot_status('Running')
    assert bot.status == 'Running', "Bot status should be 'Running' after updating the status to 'Running'"

from crypto_games.base import CryptoGames
from crypto_games.looper import Looper
from crypto_games.bet import Betting
from crypto_games.handler import TwiceStrategyHandler, CrisisDetectHandler
from YHbot.handler import MyHandler

default = Betting(coin_kind="BTC",
                  bet=0.00000001,
                  payout=2,
                  under_over=False,
                  client_seed=None)

while True:
    mylooper = Looper("secret",
                      default, 0.00000640)
    mylooper.add_handler(MyHandler())
    try:
        mylooper.run()
    except BaseException:
        pass
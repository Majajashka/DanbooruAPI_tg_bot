from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


env = Env()
env.read_env()
config = Config(
    tg_bot=TgBot(
        token=env('BOT_TOKEN'),
    ),
    db=DatabaseConfig(
        database=env('DATABASE'),
        db_host=env('DB_HOST'),
        db_user=env('DB_USER'),
        db_password=env('DB_PASSWORD')
    )
)

if __name__ == '__main__':
    print('BOT_TOKEN:', config.tg_bot.token)
    print()
    print('DATABASE:', config.db.database)
    print('DB_HOST:', config.db.db_host)
    print('DB_USER:', config.db.db_user)
    print('DB_PASSWORD:', config.db.db_password)

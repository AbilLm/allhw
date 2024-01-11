import asyncio
import os
import random

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from os import getenv
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
scheduler = AsyncIOScheduler()
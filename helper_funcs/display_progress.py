# © aceknox

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

import math
import os
import time
import shutil
import aiohttp
import asyncio

from config import Config
from translation import Translation


async def progress_for_pyrogram(current, total, ud_type, message, filename, start):

    now = time.time()
    diff = now - start

    if round(diff % 10.00) == 0 or current == total:

        percentage = current * 100 / total
        speed = current / diff

        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000

        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress_bar = (
            "[" +
            "".join(["⬡" for i in range(math.floor(percentage / 10))]) +
            "".join(["⬢" for i in range(10 - math.floor(percentage / 10))]) +
            "]"
        )

        current_message = f"""
╭━━━━❰ Upload Progress ❱━━━━╮
┣⪼ 📄 <b>File:</b> {filename}
┣⪼ 📦 <b>Uploaded:</b> {humanbytes(current)} / {humanbytes(total)}
┣⪼ {progress_bar} <b>{round(percentage, 2)}%</b>
┣⪼ 🚀 <b>Speed:</b> {humanbytes(speed)}/s
┣⪼ ⏱️ <b>ETA:</b> {TimeFormatter(time_to_completion) if time_to_completion != '' else '0s'}
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""

        try:
            await message.edit_text(
                "{}\n{}".format(
                    ud_type,
                    current_message
                )
            )

            await asyncio.sleep(1)

        except Exception as e:
            pass


async def ContentDisposition(url):

    session = aiohttp.ClientSession()
    filename = None

    async with session.get(
        url,
        timeout=Config.PROCESS_MAX_TIMEOUT
    ) as response:

        content_disposition = response.headers.get(
            "Content-Disposition",
            ""
        )

        if "filename=" in content_disposition:
            filename = content_disposition.split(
                "filename="
            )[-1].replace("\"", "")

        filesize = int(
            response.headers.get("Content-Length", 0)
        )

        await session.close()

    return filename, humanbytes(filesize)


async def ContentLength(url):

    session = aiohttp.ClientSession()

    async with session.get(
        url,
        timeout=Config.PROCESS_MAX_TIMEOUT
    ) as response:

        filesize = int(
            response.headers.get("Content-Length", 0)
        )

        await session.close()

    return humanbytes(filesize)


def humanbytes(size):

    if not size:
        return ""

    power = 2**10
    n = 0

    Dic_powerN = {
        0: '',
        1: 'K',
        2: 'M',
        3: 'G',
        4: 'T'
    }

    while size > power:
        size /= power
        n += 1

    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:

    seconds, milliseconds = divmod(int(milliseconds), 1000)

    minutes, seconds = divmod(seconds, 60)

    hours, minutes = divmod(minutes, 60)

    days, hours = divmod(hours, 24)

    tmp = (
        ((str(days) + "d, ") if days else "") +
        ((str(hours) + "h, ") if hours else "") +
        ((str(minutes) + "m, ") if minutes else "") +
        ((str(seconds) + "s, ") if seconds else "") +
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    )

    return tmp[:-2]

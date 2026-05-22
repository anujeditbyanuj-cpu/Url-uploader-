# =========================
# FULL M3U8 DOWNLOADER
# =========================

import os
import asyncio
import subprocess
import time
import aiohttp

# -------------------------
# Detect M3U8 URL
# -------------------------
def is_m3u8(url):
    return ".m3u8" in url.lower()


# -------------------------
# FFmpeg M3U8 Downloader
# -------------------------
async def download_m3u8_video(
    m3u8_url,
    output_path,
    info_msg
):
    """
    Download m3u8 stream using ffmpeg
    Supports standard HLS + AES-128 HLS
    """

    cmd = [
        "ffmpeg",
        "-y",
        "-headers", "User-Agent: Mozilla/5.0\\r\\n",
        "-i", m3u8_url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output_path
    ]

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    start = time.time()

    while True:

        if process.returncode is not None:
            break

        elapsed = int(time.time() - start)

        try:
            await info_msg.edit_text(
                f"📥 Downloading M3U8 Stream...\\n\\n"
                f"⏳ Elapsed: {elapsed} sec"
            )
        except:
            pass

        await asyncio.sleep(5)

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        raise Exception(stderr.decode())

    return output_path


# =========================
# NORMAL FILE DOWNLOADER
# =========================

async def download_coroutine(info_msg, session, url, file_name):

    async with session.get(url) as response:

        with open(file_name, "wb") as f:

            async for chunk in response.content.iter_chunked(1024 * 1024):
                f.write(chunk)


# =========================
# MAIN DOWNLOAD HANDLER
# =========================

async def start_download(
    dl_url,
    download_directory,
    info_msg
):

    # M3U8 DOWNLOAD
    if is_m3u8(dl_url):

        await info_msg.edit_text(
            "🎬 M3U8 stream detected..."
        )

        await download_m3u8_video(
            dl_url,
            download_directory,
            info_msg
        )

    # NORMAL FILE DOWNLOAD
    else:

        async with aiohttp.ClientSession() as session:

            await download_coroutine(
                info_msg,
                session,
                dl_url,
                download_directory
            )

    return download_directory


# =========================
# AUTO FILE NAME
# =========================

def generate_filename(dl_url):

    if ".m3u8" in dl_url:
        return dl_url.split("/")[-1].replace(".m3u8", ".mp4")

    return dl_url.split("/")[-1]


# =========================
# EXAMPLE
# =========================

"""
dl_url = "https://example.com/master.m3u8"
filename = generate_filename(dl_url)
print(filename)
"""

from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 21119132))
API_HASH = getenv("API_HASH", "c0a90d0ba66e6bdea356894a55f4856e")

BOT_TOKEN = getenv("BOT_TOKEN", "5889085407:AAHSyJtD6xPwGGktbE5nnwXpOqB4Fjq3HW8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", 5905988205))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAFCQJwAGrYXjDFaxg3O1ERyerchyfSEcd-p1WWEQGd4YS-7uTWeTESYFnFDs70kfdlQPZrxhX9qLxmy3vQvpvVdp8oYvwB0WF6q4KVapxLyhgoGUpmvnd22tmAIBiEHwepqNHH216-77LnER3uUwbVB2vTea4dA1W86Ep1hMsQAltbh2OtoXyP3cxfpTKeVTmxcsRPRE1YN9kXVEMfY31VSnxprQbwuSB7-QblCy4RZEBuCvU3LvpnIcDecm5wd06ytseeFPiZ7oAAKcdTn9mEMIryYgvxnomhfZr83JNwOwf4GtCR2nrkObUkOIDIbRnNm_44Xi4hNabpsyBCOyjrKWdXXTQAAAAFgBjptAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

"""
popular_apps.py
Uploads a large curated list of popular apps across categories
(social, games, streaming, finance, VPN, productivity, education, etc.)
to Supabase with source='playstore'. These link to the official Play
Store listing instead of hosting APKs.
Run manually: python popular_apps.py
"""

import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def play_store_url(package_id: str) -> str:
    return f"https://play.google.com/store/apps/details?id={package_id}"


POPULAR_APPS = [
    # Social
    {"id": "com.facebook.katana", "name": "Facebook", "summary": "Connect with friends and the world around you.", "category": "Social"},
    {"id": "com.facebook.lite", "name": "Facebook Lite", "summary": "Lightweight version of Facebook.", "category": "Social"},
    {"id": "com.instagram.android", "name": "Instagram", "summary": "Share photos and videos with friends.", "category": "Social"},
    {"id": "com.zhiliaoapp.musically", "name": "TikTok", "summary": "Short videos, endless entertainment.", "category": "Social"},
    {"id": "com.snapchat.android", "name": "Snapchat", "summary": "Share moments with friends.", "category": "Social"},
    {"id": "com.twitter.android", "name": "X (Twitter)", "summary": "See what's happening in the world.", "category": "Social"},
    {"id": "com.pinterest", "name": "Pinterest", "summary": "Discover ideas and inspiration.", "category": "Social"},
    {"id": "com.linkedin.android", "name": "LinkedIn", "summary": "Professional networking.", "category": "Social"},
    {"id": "com.reddit.frontpage", "name": "Reddit", "summary": "Communities and discussions.", "category": "Social"},
    {"id": "com.tumblr", "name": "Tumblr", "summary": "Discover and share blogs.", "category": "Social"},
    {"id": "com.discord", "name": "Discord", "summary": "Chat, hang out, and stay close with friends.", "category": "Social"},
    {"id": "com.bereal.ft", "name": "BeReal", "summary": "Be yourself with friends.", "category": "Social"},

    # Communication
    {"id": "com.whatsapp", "name": "WhatsApp Messenger", "summary": "Simple, secure, reliable messaging.", "category": "Communication"},
    {"id": "org.telegram.messenger", "name": "Telegram", "summary": "Fast and secure messaging.", "category": "Communication"},
    {"id": "com.facebook.orca", "name": "Messenger", "summary": "Text and video chat for free.", "category": "Communication"},
    {"id": "com.skype.raider", "name": "Skype", "summary": "Video calls and messaging.", "category": "Communication"},
    {"id": "com.viber.voip", "name": "Viber", "summary": "Free messaging and calls.", "category": "Communication"},
    {"id": "com.google.android.gm", "name": "Gmail", "summary": "Secure, smart, and easy email.", "category": "Communication"},
    {"id": "com.microsoft.office.outlook", "name": "Microsoft Outlook", "summary": "Email and calendar.", "category": "Communication"},
    {"id": "com.imo.android.imoim", "name": "imo", "summary": "Free video calls and chat.", "category": "Communication"},
    {"id": "us.zoom.videomeetings", "name": "Zoom", "summary": "Video conferencing and meetings.", "category": "Communication"},
    {"id": "com.google.android.apps.tachyon", "name": "Google Meet", "summary": "Video calling for everyone.", "category": "Communication"},
    {"id": "com.microsoft.teams", "name": "Microsoft Teams", "summary": "Chat, meetings, calls, and collaboration.", "category": "Communication"},
    {"id": "com.Slack", "name": "Slack", "summary": "Where work happens.", "category": "Communication"},
    {"id": "com.truecaller", "name": "Truecaller", "summary": "Caller ID and spam blocking.", "category": "Communication"},

    # Entertainment / Streaming
    {"id": "com.netflix.mediaclient", "name": "Netflix", "summary": "Watch TV shows and movies anytime, anywhere.", "category": "Entertainment"},
    {"id": "com.google.android.youtube", "name": "YouTube", "summary": "Watch, upload, and share videos.", "category": "Entertainment"},
    {"id": "com.google.android.apps.youtube.music", "name": "YouTube Music", "summary": "Stream music and videos.", "category": "Entertainment"},
    {"id": "com.spotify.music", "name": "Spotify", "summary": "Music and podcasts streaming.", "category": "Entertainment"},
    {"id": "com.amazon.avod.thirdpartyclient", "name": "Prime Video", "summary": "Movies and TV shows.", "category": "Entertainment"},
    {"id": "com.disney.disneyplus", "name": "Disney+", "summary": "Stream Disney, Pixar, Marvel, Star Wars.", "category": "Entertainment"},
    {"id": "com.hbo.hbonow", "name": "Max", "summary": "Stream movies, series, and originals.", "category": "Entertainment"},
    {"id": "tv.twitch.android.app", "name": "Twitch", "summary": "Livestreaming for gamers.", "category": "Entertainment"},
    {"id": "com.soundcloud.android", "name": "SoundCloud", "summary": "Discover and stream music.", "category": "Entertainment"},
    {"id": "deezer.android.app", "name": "Deezer", "summary": "Music streaming service.", "category": "Entertainment"},
    {"id": "com.audible.application", "name": "Audible", "summary": "Audiobooks and podcasts.", "category": "Entertainment"},
    {"id": "com.boomplay.musicplay", "name": "Boomplay", "summary": "Music and video streaming.", "category": "Entertainment"},

    # Maps & Navigation
    {"id": "com.google.android.apps.maps", "name": "Google Maps", "summary": "Navigate your world with ease.", "category": "Maps & Navigation"},
    {"id": "com.waze", "name": "Waze", "summary": "GPS, maps, traffic alerts.", "category": "Maps & Navigation"},
    {"id": "com.ubercab", "name": "Uber", "summary": "Request a ride anytime, anywhere.", "category": "Maps & Navigation"},
    {"id": "com.bolt.eu.partner.taxi.driver", "name": "Bolt", "summary": "Ride-hailing and delivery.", "category": "Maps & Navigation"},

    # Shopping
    {"id": "com.amazon.mShop.android.shopping", "name": "Amazon Shopping", "summary": "Shop millions of products.", "category": "Shopping"},
    {"id": "com.ebay.mobile", "name": "eBay", "summary": "Buy and sell online.", "category": "Shopping"},
    {"id": "com.alibaba.aliexpresshd", "name": "AliExpress", "summary": "Online shopping from China.", "category": "Shopping"},
    {"id": "com.jumia.android", "name": "Jumia", "summary": "Online shopping in Africa.", "category": "Shopping"},
    {"id": "com.shein.android", "name": "SHEIN", "summary": "Fashion shopping app.", "category": "Shopping"},
    {"id": "com.contextlogic.wish", "name": "Wish", "summary": "Shopping made fun.", "category": "Shopping"},

    # Finance / Trading
    {"id": "com.binance.dev", "name": "Binance", "summary": "Buy and trade crypto.", "category": "Finance"},
    {"id": "com.coinbase.android", "name": "Coinbase", "summary": "Buy, sell, and store crypto.", "category": "Finance"},
    {"id": "com.robinhood.android", "name": "Robinhood", "summary": "Investing, simplified.", "category": "Finance"},
    {"id": "com.etoro.openbook", "name": "eToro", "summary": "Social trading and investing.", "category": "Finance"},
    {"id": "com.paypal.android.p2pmobile", "name": "PayPal", "summary": "Send, spend, and manage money.", "category": "Finance"},
    {"id": "com.transferwise.android", "name": "Wise", "summary": "International money transfer.", "category": "Finance"},
    {"id": "com.skrill.skrill", "name": "Skrill", "summary": "Digital wallet and money transfer.", "category": "Finance"},
    {"id": "com.kcbgroup.mobi", "name": "KCB Bank", "summary": "Mobile banking app.", "category": "Finance"},
    {"id": "com.equitybankgroup.eazzybanking", "name": "Equity Bank Eazzy Banking", "summary": "Mobile banking for Equity Bank.", "category": "Finance"},
    {"id": "com.exness.android", "name": "Exness Trader", "summary": "Forex and CFD trading.", "category": "Finance"},
    {"id": "com.metaquotes.metatrader5", "name": "MetaTrader 5", "summary": "Trading platform for forex and stocks.", "category": "Finance"},
    {"id": "com.metaquotes.metatrader4", "name": "MetaTrader 4", "summary": "Forex trading platform.", "category": "Finance"},

    # VPN & Security
    {"id": "com.nordvpn.android", "name": "NordVPN", "summary": "Fast and secure VPN.", "category": "VPN & Security"},
    {"id": "com.expressvpn.vpn", "name": "ExpressVPN", "summary": "Secure VPN for privacy.", "category": "VPN & Security"},
    {"id": "free.vpn.unblock.proxy.turbovpn", "name": "Turbo VPN", "summary": "Free VPN proxy.", "category": "VPN & Security"},
    {"id": "com.psiphon3", "name": "Psiphon", "summary": "Free VPN to bypass censorship.", "category": "VPN & Security"},
    {"id": "com.surfshark.vpnclient.android", "name": "Surfshark VPN", "summary": "Fast VPN for privacy.", "category": "VPN & Security"},
    {"id": "com.protonvpn.android", "name": "Proton VPN", "summary": "Secure and private VPN.", "category": "VPN & Security"},
    {"id": "com.avast.android.mobilesecurity", "name": "Avast Antivirus", "summary": "Mobile security and antivirus.", "category": "VPN & Security"},
    {"id": "com.lookout", "name": "Lookout Security", "summary": "Mobile security and identity protection.", "category": "VPN & Security"},
    {"id": "com.hotspotshield.android.vpn", "name": "Hotspot Shield VPN", "summary": "Fast secure VPN proxy.", "category": "VPN & Security"},
    {"id": "com.cyberghost.vpn", "name": "CyberGhost VPN", "summary": "Privacy and security VPN.", "category": "VPN & Security"},
    {"id": "com.windscribe.vpn", "name": "Windscribe VPN", "summary": "Free VPN and ad blocker.", "category": "VPN & Security"},
    {"id": "com.atlasvpn.android", "name": "Atlas VPN", "summary": "Fast and secure VPN service.", "category": "VPN & Security"},
    {"id": "com.kape.vpn.private.fast.secure", "name": "PIA VPN", "summary": "Private Internet Access VPN.", "category": "VPN & Security"},
    {"id": "net.tunnelbear.android", "name": "TunnelBear VPN", "summary": "Simple secure VPN.", "category": "VPN & Security"},
    {"id": "com.vpn.proxymaster", "name": "Proxy Master VPN", "summary": "Free unlimited VPN proxy.", "category": "VPN & Security"},
    {"id": "com.thunder.vpn", "name": "Thunder VPN", "summary": "Free, fast, and unlimited VPN.", "category": "VPN & Security"},
    {"id": "com.x8bit.bitwarden", "name": "Bitwarden", "summary": "Free password manager.", "category": "VPN & Security"},
    {"id": "com.lastpass.lpandroid", "name": "LastPass", "summary": "Password manager and vault.", "category": "VPN & Security"},
    {"id": "com.dashlane", "name": "Dashlane", "summary": "Password manager and digital wallet.", "category": "VPN & Security"},
    {"id": "com.kaspersky.android.antivirus", "name": "Kaspersky Antivirus", "summary": "Mobile security and antivirus.", "category": "VPN & Security"},

    # Productivity
    {"id": "com.google.android.apps.docs", "name": "Google Drive", "summary": "Cloud storage and file sharing.", "category": "Productivity"},
    {"id": "com.microsoft.office.officehubrow", "name": "Microsoft 365 (Office)", "summary": "Word, Excel, PowerPoint and more.", "category": "Productivity"},
    {"id": "com.dropbox.android", "name": "Dropbox", "summary": "Cloud storage.", "category": "Productivity"},
    {"id": "notion.id", "name": "Notion", "summary": "Notes, docs, and project management.", "category": "Productivity"},
    {"id": "com.evernote", "name": "Evernote", "summary": "Notes and organization.", "category": "Productivity"},
    {"id": "com.todoist", "name": "Todoist", "summary": "To-do list and task manager.", "category": "Productivity"},
    {"id": "com.trello", "name": "Trello", "summary": "Organize anything with boards.", "category": "Productivity"},
    {"id": "com.asana.app", "name": "Asana", "summary": "Project and task management.", "category": "Productivity"},
    {"id": "com.canva.editor", "name": "Canva", "summary": "Design anything, publish anywhere.", "category": "Productivity"},
    {"id": "com.adobe.scan.android", "name": "Adobe Scan", "summary": "PDF scanner.", "category": "Productivity"},
    {"id": "com.adobe.reader", "name": "Adobe Acrobat Reader", "summary": "View and edit PDFs.", "category": "Productivity"},

    # Education
    {"id": "com.duolingo", "name": "Duolingo", "summary": "Learn languages for free.", "category": "Education"},
    {"id": "org.khanacademy.android", "name": "Khan Academy", "summary": "Free online courses.", "category": "Education"},
    {"id": "org.coursera.android", "name": "Coursera", "summary": "Online courses from top universities.", "category": "Education"},
    {"id": "com.udemy.android", "name": "Udemy", "summary": "Online learning and courses.", "category": "Education"},
    {"id": "com.quizlet.quizletandroid", "name": "Quizlet", "summary": "Flashcards and study tools.", "category": "Education"},
    {"id": "com.microblink.photomath", "name": "Photomath", "summary": "Math problem solver.", "category": "Education"},
    {"id": "com.brainly", "name": "Brainly", "summary": "Homework help and answers.", "category": "Education"},

    # Games
    {"id": "com.king.candycrushsaga", "name": "Candy Crush Saga", "summary": "Match candies in this puzzle game.", "category": "Games"},
    {"id": "com.king.candycrushsodasaga", "name": "Candy Crush Soda Saga", "summary": "Soda-themed match puzzle.", "category": "Games"},
    {"id": "com.dts.freefireth", "name": "Free Fire", "summary": "Battle royale survival game.", "category": "Games"},
    {"id": "com.tencent.ig", "name": "PUBG Mobile", "summary": "Battle royale shooter.", "category": "Games"},
    {"id": "com.activision.callofduty.shooter", "name": "Call of Duty: Mobile", "summary": "First-person shooter game.", "category": "Games"},
    {"id": "com.roblox.client", "name": "Roblox", "summary": "Create and play games.", "category": "Games"},
    {"id": "com.mojang.minecraftpe", "name": "Minecraft", "summary": "Build, explore, and survive.", "category": "Games"},
    {"id": "com.supercell.clashofclans", "name": "Clash of Clans", "summary": "Build your village and battle.", "category": "Games"},
    {"id": "com.supercell.clashroyale", "name": "Clash Royale", "summary": "Real-time strategy card game.", "category": "Games"},
    {"id": "com.supercell.brawlstars", "name": "Brawl Stars", "summary": "Fast-paced multiplayer battles.", "category": "Games"},
    {"id": "com.supercell.hayday", "name": "Hay Day", "summary": "Farming simulation game.", "category": "Games"},
    {"id": "com.ea.gp.fifamobile", "name": "EA Sports FC Mobile", "summary": "Football/soccer game.", "category": "Games"},
    {"id": "com.miniclip.eightballpool", "name": "8 Ball Pool", "summary": "Multiplayer pool game.", "category": "Games"},
    {"id": "com.gameloft.android.ANMP.GloftA9HM", "name": "Asphalt 9", "summary": "Racing game.", "category": "Games"},
    {"id": "com.ea.game.nfs14_row", "name": "Need for Speed: No Limits", "summary": "High-speed racing game.", "category": "Games"},
    {"id": "com.kiloo.subwaysurf", "name": "Subway Surfers", "summary": "Endless running game.", "category": "Games"},
    {"id": "com.innersloth.spacemafia", "name": "Among Us", "summary": "Multiplayer social deduction game.", "category": "Games"},
    {"id": "com.ludo.king", "name": "Ludo King", "summary": "Classic board game online.", "category": "Games"},
    {"id": "com.zynga.wwf2.free", "name": "Words With Friends", "summary": "Word puzzle game.", "category": "Games"},
    {"id": "com.outfit7.mytalkingtomfree", "name": "My Talking Tom", "summary": "Virtual pet game.", "category": "Games"},
    {"id": "com.outfit7.mytalkingtom2", "name": "My Talking Tom 2", "summary": "Virtual pet adventure.", "category": "Games"},
    {"id": "com.scopely.monopolygo", "name": "Monopoly GO!", "summary": "Board game adventure.", "category": "Games"},
    {"id": "com.miHoYo.GenshinImpact", "name": "Genshin Impact", "summary": "Open-world action RPG.", "category": "Games"},
    {"id": "com.dreamgames.royalmatch", "name": "Royal Match", "summary": "Match-3 puzzle adventure.", "category": "Games"},
    {"id": "com.playrix.gardenscapes", "name": "Gardenscapes", "summary": "Match-3 garden renovation game.", "category": "Games"},
    {"id": "com.playrix.homescapes", "name": "Homescapes", "summary": "Match-3 home renovation game.", "category": "Games"},
    {"id": "com.zynga.toonblast", "name": "Toon Blast", "summary": "Cartoon puzzle adventure.", "category": "Games"},
    {"id": "com.moonactive.coinmaster", "name": "Coin Master", "summary": "Slot and village building game.", "category": "Games"},
    {"id": "com.miniclip.bowmasters", "name": "Bowmasters", "summary": "Multiplayer archery game.", "category": "Games"},
    {"id": "com.sybogames.archero", "name": "Archero", "summary": "Action roguelike adventure.", "category": "Games"},
    {"id": "com.netease.lztgglobal", "name": "Lifeafter", "summary": "Survival adventure game.", "category": "Games"},
    {"id": "com.epicgames.fortnite", "name": "Fortnite", "summary": "Battle royale game.", "category": "Games"},
    {"id": "com.nianticlabs.pokemongo", "name": "Pokemon GO", "summary": "Augmented reality adventure game.", "category": "Games"},
    {"id": "com.gamestar.pianoperfect", "name": "Piano Tiles 2", "summary": "Music rhythm game.", "category": "Games"},
    {"id": "com.halfbrick.fruitninjafree", "name": "Fruit Ninja", "summary": "Slice fruits action game.", "category": "Games"},
    {"id": "com.rovio.angrybirds2", "name": "Angry Birds 2", "summary": "Bird-slinging puzzle action.", "category": "Games"},

    # More Social
    {"id": "com.vk", "name": "VK", "summary": "Social network and messaging.", "category": "Social"},
    {"id": "com.kakao.talk", "name": "KakaoTalk", "summary": "Free calls and text.", "category": "Social"},
    {"id": "jp.naver.line.android", "name": "LINE", "summary": "Free calls and messages.", "category": "Social"},
    {"id": "com.mico", "name": "MICO", "summary": "Live streaming and chat.", "category": "Social"},
    {"id": "com.yubo", "name": "Yubo", "summary": "Make new friends.", "category": "Social"},

    # More Finance / Trading
    {"id": "com.kucoin.android", "name": "KuCoin", "summary": "Crypto exchange.", "category": "Finance"},
    {"id": "com.okinc.okex.gp", "name": "OKX", "summary": "Crypto trading platform.", "category": "Finance"},
    {"id": "com.bybit.app", "name": "Bybit", "summary": "Crypto derivatives exchange.", "category": "Finance"},
    {"id": "com.trustwallet.app", "name": "Trust Wallet", "summary": "Crypto wallet.", "category": "Finance"},
    {"id": "piuk.blockchain.android", "name": "Blockchain.com Wallet", "summary": "Crypto wallet and exchange.", "category": "Finance"},
    {"id": "com.fxpro.tradingapp", "name": "FxPro", "summary": "Forex and CFD trading.", "category": "Finance"},
    {"id": "com.xm.webapp", "name": "XM Trading", "summary": "Forex broker app.", "category": "Finance"},
    {"id": "com.octafx.trade", "name": "OctaFX Trading", "summary": "Forex trading platform.", "category": "Finance"},
    {"id": "com.hotforex.android", "name": "HotForex", "summary": "Online forex trading.", "category": "Finance"},
    {"id": "com.safaricom.mpesa", "name": "M-PESA App", "summary": "Mobile money for Safaricom users.", "category": "Finance"},
    {"id": "co.cellulant.tingg", "name": "Tingg", "summary": "Pay bills and send money in Africa.", "category": "Finance"},
    {"id": "com.absa.kenya", "name": "Absa Kenya", "summary": "Mobile banking app.", "category": "Finance"},
    {"id": "com.ncba.ng", "name": "NCBA Now", "summary": "Mobile banking for NCBA Bank.", "category": "Finance"},
    {"id": "com.cooperativebank.cooponline", "name": "Co-op Bank Mobile Banking", "summary": "Mobile banking app.", "category": "Finance"},
    {"id": "com.dtb.dtbonline", "name": "DTB Mobile Banking", "summary": "Diamond Trust Bank mobile app.", "category": "Finance"},
    {"id": "com.stanbicbank.kenya", "name": "Stanbic Bank Kenya", "summary": "Mobile banking app.", "category": "Finance"},

    # Lifestyle / Dating
    {"id": "com.tinder", "name": "Tinder", "summary": "Dating app.", "category": "Lifestyle"},
    {"id": "com.bumble.app", "name": "Bumble", "summary": "Dating, friends, networking.", "category": "Lifestyle"},
    {"id": "com.badoo.mobile", "name": "Badoo", "summary": "Meet new people.", "category": "Lifestyle"},

    # Food & Delivery
    {"id": "com.ubercab.eats", "name": "Uber Eats", "summary": "Food delivery.", "category": "Food & Drink"},
    {"id": "com.glovoapp23", "name": "Glovo", "summary": "Delivery for food and more.", "category": "Food & Drink"},
    {"id": "com.jumia.food", "name": "Jumia Food", "summary": "Order food online.", "category": "Food & Drink"},

    # Health & Fitness
    {"id": "com.myfitnesspal.android", "name": "MyFitnessPal", "summary": "Calorie counter and diet tracker.", "category": "Health & Fitness"},
    {"id": "com.calm.android", "name": "Calm", "summary": "Meditation and sleep.", "category": "Health & Fitness"},
    {"id": "com.getsomeheadspace.android", "name": "Headspace", "summary": "Meditation and mindfulness.", "category": "Health & Fitness"},
    {"id": "com.fitbit.FitbitMobile", "name": "Fitbit", "summary": "Health and fitness tracking.", "category": "Health & Fitness"},
    {"id": "com.strava", "name": "Strava", "summary": "Running and cycling tracker.", "category": "Health & Fitness"},
    {"id": "com.nike.ntc", "name": "Nike Training Club", "summary": "Workouts and fitness plans.", "category": "Health & Fitness"},
    {"id": "com.sec.android.app.shealth", "name": "Samsung Health", "summary": "Health and fitness tracking.", "category": "Health & Fitness"},
    {"id": "com.flo.health", "name": "Flo Period Tracker", "summary": "Period and ovulation tracker.", "category": "Health & Fitness"},
    {"id": "com.clue.android", "name": "Clue Period Tracker", "summary": "Cycle and health tracking.", "category": "Health & Fitness"},

    # News
    {"id": "com.google.android.apps.magazines", "name": "Google News", "summary": "Personalized news.", "category": "News"},
    {"id": "bbc.mobile.news.ww", "name": "BBC News", "summary": "World news and headlines.", "category": "News"},
    {"id": "com.cnn.mobile.android.phone", "name": "CNN", "summary": "Breaking news and video.", "category": "News"},
    {"id": "com.aljazeera.mobile", "name": "Al Jazeera", "summary": "World news and analysis.", "category": "News"},
    {"id": "com.nation.daily", "name": "Daily Nation", "summary": "Kenyan news app.", "category": "News"},
    {"id": "com.standardmedia.ke", "name": "The Standard Kenya", "summary": "Kenyan news and updates.", "category": "News"},

    # Tools / Utilities
    {"id": "com.estrongs.android.pop", "name": "ES File Explorer", "summary": "File manager.", "category": "Tools"},
    {"id": "com.google.android.apps.translate", "name": "Google Translate", "summary": "Translate text and speech.", "category": "Tools"},
    {"id": "com.adobe.lrmobile", "name": "Adobe Lightroom", "summary": "Photo editor.", "category": "Tools"},
    {"id": "com.picsart.studio", "name": "PicsArt", "summary": "Photo and video editor.", "category": "Tools"},
    {"id": "com.camerasideas.instashot", "name": "InShot", "summary": "Video editor and maker.", "category": "Tools"},
    {"id": "com.zhiliaoapp.musically.go", "name": "CapCut", "summary": "Video editing app.", "category": "Tools"},
    {"id": "com.miui.weather2", "name": "Weather", "summary": "Weather forecast app.", "category": "Tools"},
    {"id": "com.accuweather.android", "name": "AccuWeather", "summary": "Weather forecasts and alerts.", "category": "Tools"},
    {"id": "com.shazam.android", "name": "Shazam", "summary": "Music identification.", "category": "Tools"},
    {"id": "com.google.android.apps.photos", "name": "Google Photos", "summary": "Photo storage and sharing.", "category": "Tools"},
    {"id": "com.google.android.keep", "name": "Google Keep", "summary": "Notes and lists.", "category": "Tools"},
    {"id": "com.microsoft.skydrive", "name": "Microsoft OneDrive", "summary": "Cloud file storage.", "category": "Tools"},
    {"id": "com.google.android.apps.authenticator2", "name": "Google Authenticator", "summary": "Two-factor authentication.", "category": "Tools"},
    {"id": "com.cleanmaster.security", "name": "CM Security", "summary": "Antivirus and app lock.", "category": "Tools"},
    {"id": "com.opera.browser", "name": "Opera Browser", "summary": "Fast and secure web browser.", "category": "Tools"},
    {"id": "org.mozilla.firefox", "name": "Firefox Browser", "summary": "Fast, private web browser.", "category": "Tools"},
    {"id": "com.UCMobile.intl", "name": "UC Browser", "summary": "Fast and secure browser.", "category": "Tools"},
    {"id": "com.brave.browser", "name": "Brave Browser", "summary": "Private, fast web browser.", "category": "Tools"},
    {"id": "com.microsoft.emmx", "name": "Microsoft Edge", "summary": "Fast and secure browser.", "category": "Tools"},

    # More Entertainment
    {"id": "com.netease.cloudmusic", "name": "NetEase Cloud Music", "summary": "Music streaming app.", "category": "Entertainment"},
    {"id": "com.anghami", "name": "Anghami", "summary": "Music and podcasts streaming.", "category": "Entertainment"},
    {"id": "com.vimeo.android.videoapp", "name": "Vimeo", "summary": "Video creation and sharing.", "category": "Entertainment"},
    {"id": "com.dailymotion.dailymotion", "name": "Dailymotion", "summary": "Video sharing platform.", "category": "Entertainment"},
    {"id": "com.tubitv", "name": "Tubi", "summary": "Free movies and TV.", "category": "Entertainment"},
    {"id": "com.plexapp.android", "name": "Plex", "summary": "Stream personal media library.", "category": "Entertainment"},
    {"id": "com.iflix.app", "name": "iflix", "summary": "Movies and TV shows.", "category": "Entertainment"},

    # More Education
    {"id": "com.babbel.mobile.android.en", "name": "Babbel", "summary": "Language learning app.", "category": "Education"},
    {"id": "com.rosettastone.android", "name": "Rosetta Stone", "summary": "Language learning.", "category": "Education"},
    {"id": "com.google.android.apps.classroom", "name": "Google Classroom", "summary": "Classroom management tool.", "category": "Education"},
    {"id": "com.edx.mobile", "name": "edX", "summary": "Online courses from universities.", "category": "Education"},
    {"id": "org.edraak.android", "name": "Edraak", "summary": "Arabic online learning platform.", "category": "Education"},
    {"id": "com.skillshare.Skillshare", "name": "Skillshare", "summary": "Creative classes online.", "category": "Education"},
]


def build_rows():
    rows = []
    for app in POPULAR_APPS:
        rows.append({
            "id": app["id"],
            "name": app["name"],
            "summary": app["summary"],
            "description": app["summary"],
            "icon_url": None,
            "category": app["category"],
            "source": "playstore",
            "license": "Proprietary",
            "apk_url": None,
            "play_store_url": play_store_url(app["id"]),
            "version": "",
        })
    return rows


def upload_to_supabase(rows):
    print(f"Uploading {len(rows)} popular apps to Supabase...")
    batch_size = 50
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        supabase.table("apps").upsert(batch).execute()
        print(f"  Uploaded batch {i // batch_size + 1} ({len(batch)} apps)")
    print("Done!")


if __name__ == "__main__":
    rows = build_rows()
    upload_to_supabase(rows)
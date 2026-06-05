# Jarvis - Termux/Android Setup Guide

**आपके Android फोन पर Jarvis को चलाने के लिए सेटअप गाइड**

## ✅ Requirements

1. **Termux App** - Download from F-Droid या GitHub Releases
2. **Python 3.10+** - Termux में पहले से होगा
3. **ADB** (Android Debug Bridge) - Termux से device control के लिए
4. **Internet Connection** - LiveKit और APIs के लिए

---

## 📲 Step 1: Termux को सेटअप करें

```bash
# Termux को update करें
pkg update && pkg upgrade -y

# Python install करें (यदि नहीं है)
pkg install python python-pip -y

# आवश्यक packages install करें
pkg install git nano curl wget -y
```

---

## 📦 Step 2: Repository को Clone करें

```bash
# GitHub से Jarvis को clone करें
git clone https://github.com/Exploits5/Jarvis.git

# Jarvis directory में जाएं
cd Jarvis
```

---

## 🔧 Step 3: Dependencies Install करें

```bash
# Python requirements install करें
pip install -r requirements.txt

# यदि कुछ packages fail हों, तो individual install करें:
pip install --upgrade pip setuptools wheel
pip install livekit livekit-agents python-dotenv requests
```

---

## 🔑 Step 4: API Keys सेटअप करें

`.env` फाइल बनाएं:

```bash
nano .env
```

निम्नलिखित जोड़ें:

```env
# Google API Key (Google Search के लिए)
GOOGLE_API_KEY=your_google_api_key_here

# OpenWeather API Key (मौसम के लिए)
WEATHER_API_KEY=your_openweather_api_key_here

# LiveKit Server URL
LIVEKIT_URL=ws://your_livekit_server:7880
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Google Realtime Model Token
GOOGLE_API_TOKEN=your_google_realtime_token
```

**Ctrl+X** दबाएं, फिर **Y** और **Enter** दें।

---

## ⚙️ Step 5: ADB Setup (Device Control के लिए)

### Android Device पर:

1. **Developer Options Enable करें:**
   - Settings → About Phone → Build Number पर 7 बार टैप करें
   - Back जाएं → Developer Options मिलेगा

2. **USB Debugging Enable करें:**
   - Settings → Developer Options → USB Debugging ✓

3. **Termux को USB Permission दें:**
   ```bash
   pkg install android-tools -y
   ```

---

## ▶️ Step 6: Jarvis को चलाएं

### Option A: Basic Mode
```bash
python agent.py
```

### Option B: Termux में Background Service के रूप में

```bash
# Screen session बनाएं
screen -S jarvis python agent.py

# Detach करने के लिए: Ctrl+A, फिर D
# फिर से attach करने के लिए: screen -r jarvis
```

---

## 📝 File Structure

```
Jarvis/
├── agent.py                          # मुख्य AI Agent
├── android_input_CTRL.py             # टच/इनपुट कंट्रोल
├── Jarvis_android_CTRL.py            # ऐप्स कंट्रोल
├── Jarvis_prompts.py                 # AI Behavior
├── Jarvis_google_search.py           # Google Search
├── jarvis_get_whether.py             # मौसम की जानकारी
├── Jarvis_file_opner.py              # फाइल खोलने के लिए
├── requirements.txt                  # Dependencies
├── .env                              # API Keys (बनाएं)
└── SETUP_TERMUX.md                   # यह फाइल
```

---

## 🎤 Jarvis के साथ Interact करें

जब Jarvis चल रहा हो, तो आप कह सकते हैं:

```
"Open WhatsApp"
"Search for Python tutorials"
"What's the weather today?"
"Take a screenshot"
"Open my Downloads folder"
"Play music"
"Open Chrome and search for something"
```

---

## 🐛 Troubleshooting

### समस्या 1: Import Error
```bash
# सभी dependencies फिर से install करें
pip install --no-cache-dir -r requirements.txt
```

### समस्या 2: ADB Connection Issue
```bash
# ADB को restart करें
adb kill-server
adb start-server
```

### समस्या 3: Permission Denied
```bash
# Termux को File Permission दें
termux-setup-storage
```

### समस्या 4: No module named 'livekit'
```bash
pip install livekit livekit-agents livekit-plugins-openai
```

---

## 📞 Support

यदि कोई समस्या हो:
1. GitHub Issues में पूछें
2. लॉग्स देखें: `python agent.py 2>&1 | tee jarvis.log`
3. सभी dependencies check करें: `pip list`

---

## 🚀 Advanced Configuration

### Voice Language बदलें
`agent.py` में:
```python
voice="Charon"  # को बदलें किसी अन्य voice से
```

### Custom Commands जोड़ें
`Jarvis_prompts.py` में instructions को edit करें।

---

**Happy Voice Commanding! 🎤🤖**

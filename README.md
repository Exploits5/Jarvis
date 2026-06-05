# 🤖 Jarvis - AI Voice Assistant for Termux/Android

**आपके Android फोन को AI की आवाज से कंट्रोल करें!**

Jarvis एक advanced AI-powered voice assistant है जो Termux पर चलता है और आपके Android डिवाइस को पूरी तरह कंट्रोल कर सकता है।

---

## ✨ प्रमुख Features

✅ **Voice Commands** - बस बोलें, Jarvis काम करे  
✅ **App Control** - किसी भी ऐप को खोलें/बंद करें  
✅ **Screen Control** - टच, स्वाइप, स्क्रॉल करें  
✅ **File Management** - डाउनलोड, डॉक्यूमेंट्स खोलें  
✅ **Real-time Search** - तुरंत Google से खोजें  
✅ **Weather Updates** - मौसम की जानकारी  
✅ **Multi-platform** - Windows, Linux, और Termux/Android पर काम करता है  
✅ **AI-Powered** - Google Realtime LLM के साथ

---

## 🚀 Quick Installation (Termux)

```bash
# 1. Packages update करें
pkg update && pkg upgrade -y

# 2. Python और tools install करें
pkg install python python-pip git android-tools nano -y

# 3. Repository clone करें
git clone https://github.com/Exploits5/Jarvis.git
cd Jarvis

# 4. Dependencies install करें
pip install -r requirements.txt

# 5. API Keys setup करें
nano .env

# 6. Jarvis चलाएं
python agent.py
```

---

## 📝 API Keys Setup (.env)

```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_API_TOKEN=your_google_realtime_token_here
WEATHER_API_KEY=your_openweather_api_key_here
LIVEKIT_URL=ws://your_livekit_server:7880
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

---

## 🎤 Jarvis के साथ बातचीत करें

```
"Open WhatsApp"                      # ऐप खोलें
"Search for Python tutorials"        # Google खोजें
"What's the weather today?"          # मौसम पूछें
"Take a screenshot"                  # Screenshot लें
"Open my Downloads folder"           # फोल्डर खोलें
"Play music"                         # संगीत चलाएं
"Scroll down"                        # स्क्रीन स्क्रॉल करें
"Type a message"                     # टेक्स्ट लिखें
"Press back button"                  # Back बटन दबाएं
"Increase volume"                    # वॉल्यूम बढ़ाएं
```

---

## 📁 Project Structure

```
Jarvis/
├── agent.py                    # Main AI Agent (मुख्य एजेंट)
├── Jarvis_android_CTRL.py      # Android App Control
├── android_input_CTRL.py       # Touch & Input Control
├── Jarvis_prompts.py           # AI Behavior (व्यवहार)
├── Jarvis_google_search.py     # Google Integration
├── jarvis_get_whether.py       # Weather API
├── Jarvis_file_opner.py        # File Handler
├── Jarvis_window_CTRL.py       # Windows Control
├── keyboard_mouse_CTRL.py      # PC Input Control
├── requirements.txt            # Dependencies
├── SETUP_TERMUX.md            # Setup Guide
└── README.md                   # यह फाइल
```

---

## 🔧 Configuration

### Voice बदलें
`agent.py` में:
```python
voice="Charon"  # अन्य voice में बदलें
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Import Error | `pip install --no-cache-dir -r requirements.txt` |
| ADB Not Found | `pkg install android-tools -y` |
| Permission Denied | `termux-setup-storage` |
| No Voice Output | API Keys check करें |

---

## 📖 विस्तृत Setup Guide

👉 **[Complete Termux Setup Guide देखें](SETUP_TERMUX.md)**

---

## 📱 Available Commands

### App Management
- "Open WhatsApp / Chrome / Instagram"
- "Close WhatsApp"
- "Open settings"

### Screen Control  
- "Tap at coordinates"
- "Scroll down/up"
- "Swipe left/right"
- "Take screenshot"

### Text & Input
- "Type a message"
- "Press back button"
- "Press home button"

### Information
- "What's the weather?"
- "Search for something"
- "What time is it?"

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

MIT License - Use freely!

---

## 🙏 Credits

- **LiveKit** - Real-time communication
- **Google Cloud** - AI & Search APIs
- **OpenWeather** - Weather data
- **Termux Team** - Android terminal

---

## 🎯 Roadmap

- [ ] Web Dashboard
- [ ] Multi-language Support
- [ ] Custom Wake Word
- [ ] Cloud Sync
- [ ] Advanced Scheduling
- [ ] IoT Integration

---

## 📞 Support

Issues या सवाल हों? [GitHub Issues खोलें](https://github.com/Exploits5/Jarvis/issues)

---

**Made with ❤️ for Android & Termux Users**

**Happy Voice Commanding! 🎤🤖**

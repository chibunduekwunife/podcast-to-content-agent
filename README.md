# 🎙️ Podcast to Content Agent

Transform your podcasts into viral content across all platforms in minutes, not hours!

## 🌟 Overview

The Podcast to Content Agent is an AI-powered application that automatically converts podcast audio into multiple types of engaging content including Twitter threads, LinkedIn posts, blog articles, newsletters, and video scripts.

## ✨ Features

- **🎵 Multi-format Audio Support**: Upload MP3, MP4, WAV, M4A files or YouTube links
- **🤖 AI Transcription**: Powered by OpenAI Whisper for accurate transcription
- **📱 Multi-platform Content**: Generate content optimized for different social platforms
- **⏰ Smart Timestamps**: Automatic chapter detection and timestamp generation
- **👥 Speaker Detection**: Identify different speakers in your content
- **🎨 Beautiful UI**: Modern, responsive Streamlit interface
- **📊 Analytics Dashboard**: Track your content performance and insights

## 🎯 Generated Content Types

- 🐦 **Twitter Threads** - Engaging threads with hooks and CTAs
- 💼 **LinkedIn Posts** - Professional posts with industry insights
- 📝 **Blog Posts** - SEO-optimized articles and outlines
- 📬 **Newsletter Content** - Engaging snippets for email marketing
- 🎬 **Video Scripts** - YouTube Shorts and TikTok scripts
- 📌 **Social Media Captions** - Platform-specific content

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for transcription and content generation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/podcast-to-content-agent.git
cd podcast-to-content-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

4. Run the application:
```bash
streamlit run Home.py
```

## 📁 Project Structure

```
podcast-to-content-agent/
├── Home.py                 # Main landing page
├── pages/
│   ├── landing_page.py     # Marketing landing page
│   └── streamlit_app.py    # Main application interface
├── static/
│   └── image.png          # Static assets
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎨 UI Features

### Landing Page
- Hero section with value proposition
- Feature showcase
- Pricing tiers
- Customer testimonials
- Call-to-action buttons

### Main Application
- Drag-and-drop file upload
- YouTube URL input
- Real-time processing status
- Content type selection (sidebar)
- Advanced options (tone, length, timestamps)
- Generated content preview
- Copy/download functionality
- Analytics dashboard

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **AI/ML**: OpenAI GPT-4, Whisper
- **Content Generation**: LangChain
- **Audio Processing**: Python audio libraries
- **Styling**: Custom CSS with modern design

## 🎯 Use Cases

- 🎙️ **Podcast Creators** - Maximize reach from every episode
- 📱 **Content Creators** - Repurpose long-form content efficiently
- 🏢 **Marketing Agencies** - Scale content production for clients
- 💼 **Business Owners** - Turn webinars into marketing content
- 🎓 **Educators** - Create educational content across platforms
- 📺 **YouTubers** - Transform videos into social media content

## 🚧 Future Enhancements

- [ ] Direct social media publishing
- [ ] Batch processing capabilities
- [ ] Custom prompt templates
- [ ] Team collaboration features
- [ ] API endpoints
- [ ] Integration with content management systems
- [ ] Advanced analytics and reporting
- [ ] White-label options

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, email support@podcasttocontentagent.com or join our community Discord.

---

**Built with ❤️ for content creators everywhere**
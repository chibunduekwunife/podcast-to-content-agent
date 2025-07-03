import streamlit as st
import os
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Podcast to Content Agent",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .content-output {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
    }
    .upload-section {
        background: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
    }
    .progress-container {
        margin: 2rem 0;
    }
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .animated-card {
        animation: fadeInUp 0.6s ease-out;
    }
    
    .pulse-button {
        animation: pulse 2s infinite;
    }
    
    .processing-step {
        background: linear-gradient(45deg, #f8f9fa, #ffffff);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .processing-step.active {
        background: linear-gradient(45deg, #e3f2fd, #f8f9fa);
        border-left-color: #2196f3;
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2);
    }
    
    .processing-step.completed {
        background: linear-gradient(45deg, #e8f5e8, #f8f9fa);
        border-left-color: #4caf50;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .mini-feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
        border-top: 3px solid #667eea;
    }
    
    .mini-feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .upload-area {
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 3rem 2rem;
        text-align: center;
        background: linear-gradient(45deg, #f8f9fa, #ffffff);
        transition: all 0.3s ease;
    }
    
    .upload-area:hover {
        border-color: #764ba2;
        background: linear-gradient(45deg, #e3f2fd, #f8f9fa);
    }
    
    .success-animation {
        animation: pulse 1s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🎙️ Podcast to Content Agent</h1>
    <p>Transform your podcasts into engaging content across all platforms</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for settings and options
st.sidebar.markdown("""
<div style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
    <h2 style="margin: 0; text-align: center;">⚙️ Content Settings</h2>
    <p style="margin: 0.5rem 0 0 0; text-align: center; opacity: 0.9;">Customize your content generation</p>
</div>
""", unsafe_allow_html=True)

# Content type selection with enhanced UI
st.sidebar.markdown("### 📝 Content Types to Generate")
st.sidebar.markdown("*Select which types of content you want to create*")

content_types = {}
content_options = [
    ("Twitter Thread", "🐦", "Engaging threads with hooks and CTAs", True),
    ("LinkedIn Post", "💼", "Professional posts with industry insights", True), 
    ("Blog Post", "📝", "SEO-optimized articles and outlines", True),
    ("Newsletter", "📬", "Email-ready content snippets", False),
    ("YouTube Shorts", "🎬", "Short-form video scripts", False),
    ("TikTok Script", "🎵", "Viral short-form content", False)
]

for name, icon, description, default in content_options:
    content_types[name] = st.sidebar.checkbox(
        f"{icon} {name}", 
        value=default,
        help=description
    )

# Advanced options with better styling
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔧 Advanced Options")

# Content customization
col1, col2 = st.sidebar.columns(2)
with col1:
    include_timestamps = st.checkbox("⏰ Timestamps", value=False, help="Include time markers in content")
with col2:
    detect_speakers = st.checkbox("👥 Speakers", value=False, help="Identify different speakers")

content_tone = st.sidebar.selectbox(
    "🎭 Content Tone",
    ["Professional", "Casual", "Engaging", "Educational", "Humorous"],
    help="Choose the overall tone for your content"
)

content_length = st.sidebar.selectbox(
    "📏 Content Length", 
    ["Short", "Medium", "Long"],
    index=1,
    help="Select the desired length for generated content"
)

# Target audience
target_audience = st.sidebar.selectbox(
    "🎯 Target Audience",
    ["General", "Business Professionals", "Tech Enthusiasts", "Entrepreneurs", "Educators", "Creators"],
    help="Who is your primary audience?"
)

# Additional settings
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎨 Style Preferences")

include_emojis = st.sidebar.slider("😊 Emoji Usage", 0, 10, 5, help="How many emojis to include")
include_hashtags = st.sidebar.checkbox("# Include Hashtags", value=True, help="Add relevant hashtags")
include_cta = st.sidebar.checkbox("📢 Call-to-Action", value=True, help="Add engagement prompts")

# Processing preferences
st.sidebar.markdown("---")
st.sidebar.markdown("### ⚡ Processing Options")

auto_generate = st.sidebar.checkbox("🚀 Auto-generate all content", value=True, help="Generate all selected content types automatically")
save_template = st.sidebar.checkbox("💾 Save as template", value=False, help="Save these settings for future use")

# Quick stats in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; text-align: center;">
    <h4 style="color: #667eea; margin: 0;">📊 Quick Stats</h4>
    <p style="margin: 0.5rem 0; color: #666;">Content pieces generated today</p>
    <h3 style="margin: 0; color: #28a745;">156</h3>
</div>
""", unsafe_allow_html=True)

# Initialize session state for variables that need to be accessible across columns
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'youtube_url' not in st.session_state:
    st.session_state.youtube_url = None

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("## 🎵 Upload Your Content")
    
    # Upload section
    st.markdown("""
    <div class="upload-area animated-card">
        <h3>📁 Choose Your Input Method</h3>
        <p>Drag and drop your files or paste a YouTube link to get started</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input method tabs
    tab1, tab2, tab3 = st.tabs(["📁 File Upload", "🔗 YouTube Link", "🎙️ Direct Recording"])
    
    with tab1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #667eea;">🎵 Upload Your Audio File</h4>
            <p style="color: #666; margin: 0;">Supported formats: MP3, MP4, WAV, M4A (Max 200MB)</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Upload your podcast file",
            type=['mp3', 'mp4', 'wav', 'm4a'],
            help="Supported formats: MP3, MP4, WAV, M4A"
        )
        
        # Update session state
        st.session_state.uploaded_file = uploaded_file
        
        if uploaded_file:
            st.markdown("""
            <div class="success-animation" style="background: #e8f5e8; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                <h4 style="color: #4caf50; margin: 0;">✅ File Successfully Uploaded!</h4>
                <p style="margin: 0.5rem 0 0 0; color: #666;">Ready for processing</p>
            </div>
            """, unsafe_allow_html=True)
            
            # File details
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            with metric_col1:
                st.metric("📄 Filename", uploaded_file.name)
            with metric_col2:
                st.metric("📊 Size", f"{uploaded_file.size / 1024 / 1024:.1f} MB")
            with metric_col3:
                st.metric("🎵 Type", uploaded_file.type)
            
            st.audio(uploaded_file)
    
    with tab2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 10px; margin-bottom: 1rem;">
            <h4 style="color: #667eea;">🔗 Import from YouTube</h4>
            <p style="color: #666; margin: 0;">Paste any YouTube URL to extract audio automatically</p>
        </div>
        """, unsafe_allow_html=True)
        
        youtube_url = st.text_input(
            "🔗 YouTube URL",
            placeholder="https://www.youtube.com/watch?v=...",
            help="Paste the full YouTube URL here"
        )
        
        # Update session state
        st.session_state.youtube_url = youtube_url
        
        if youtube_url:
            if "youtube.com" in youtube_url or "youtu.be" in youtube_url:
                st.markdown("""
                <div class="success-animation" style="background: #e8f5e8; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                    <h4 style="color: #4caf50; margin: 0;">✅ Valid YouTube URL Detected!</h4>
                    <p style="margin: 0.5rem 0 0 0; color: #666;">Ready to extract audio</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Mock video info
                st.markdown("""
                <div style="background: white; padding: 1rem; border-radius: 10px; border: 1px solid #e0e0e0;">
                    <h5>📺 Video Preview</h5>
                    <p><strong>Title:</strong> Sample Podcast Episode</p>
                    <p><strong>Duration:</strong> 45:32</p>
                    <p><strong>Channel:</strong> Tech Talks</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Please enter a valid YouTube URL")
    
    with tab3:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px;">
            <h4 style="color: #667eea;">🎙️ Direct Recording</h4>
            <p style="color: #666;">Record directly in your browser (Coming Soon)</p>
            <div style="margin: 2rem 0;">
                <div style="width: 80px; height: 80px; border-radius: 50%; background: #e0e0e0; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 2rem;">🎤</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("🎙️ Start Recording", disabled=True, help="Feature coming in next update")

with col2:
    st.markdown("## ⚡ Processing Status")
    
    # Processing steps
    processing_steps = [
        "🎵 Audio Upload",
        "📝 Transcription",
        "🧠 Content Analysis", 
        "✍️ Content Generation",
        "✅ Ready for Download"
    ]
    
    # Mock progress for demo
    if st.session_state.uploaded_file or st.session_state.youtube_url:
        st.markdown("### 🔄 Processing Pipeline")
        
        progress_container = st.container()
        with progress_container:
            for i, step in enumerate(processing_steps):
                if i == 0:
                    st.success(f"{step} ✅")
                elif i == 1:
                    if st.button("🚀 Start Processing"):
                        # Simulate processing
                        with st.spinner("Processing..."):
                            progress_bar = st.progress(0)
                            for j in range(100):
                                time.sleep(0.01)
                                progress_bar.progress(j + 1)
                        st.success(f"{step} ✅")
                else:
                    st.info(f"{step} ⏳")
    else:
        # Show empty state when no file is uploaded
        st.markdown("""
        <div style="text-align: center; padding: 3rem 1rem; background: #f8f9fa; border-radius: 15px; border: 2px dashed #ccc;">
            <div style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.5;">⏳</div>
            <h4 style="color: #666; margin: 0;">Waiting for Upload</h4>
            <p style="color: #888; margin: 0.5rem 0 0 0;">Upload a file to start processing</p>
        </div>
        """, unsafe_allow_html=True)

# Results section with enhanced visuals
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h2 style="color: #667eea;">📊 Generated Content</h2>
    <p style="color: #666; font-size: 1.1rem;">Your podcast transformed into engaging content</p>
</div>
""", unsafe_allow_html=True)

# Show content generation progress
if st.session_state.uploaded_file or st.session_state.youtube_url:
    # Enhanced content generation results
    st.markdown("""
    <div style="background: linear-gradient(45deg, #e3f2fd, #f8f9fa); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="text-align: center; color: #667eea;">🎉 Content Generation Complete!</h3>
        <p style="text-align: center; color: #666;">Your content has been successfully generated across all selected platforms</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Content overview cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="mini-feature-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🐦</div>
            <h4>Twitter Thread</h4>
            <p style="color: #28a745; margin: 0;">6 tweets generated</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="mini-feature-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💼</div>
            <h4>LinkedIn Post</h4>
            <p style="color: #28a745; margin: 0;">Professional ready</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="mini-feature-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📝</div>
            <h4>Blog Outline</h4>
            <p style="color: #28a745; margin: 0;">SEO optimized</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="mini-feature-card">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📬</div>
            <h4>Newsletter</h4>
            <p style="color: #28a745; margin: 0;">Email ready</p>
        </div>
        """, unsafe_allow_html=True)
    
    content_tabs = st.tabs([key for key, value in content_types.items() if value])
    
    for i, (content_type, selected) in enumerate(content_types.items()):
        if selected and i < len(content_tabs):
            with content_tabs[list(content_types.keys()).index(content_type)]:
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
                    <h3 style="color: #667eea; border-bottom: 2px solid #e0e0e0; padding-bottom: 0.5rem;">{content_type}</h3>
                """, unsafe_allow_html=True)
                
                if content_type == "Twitter Thread":
                    st.markdown("""
                        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1da1f2;">
                            <h4 style="color: #1da1f2;">🧵 Twitter Thread (6 tweets)</h4>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>1/6</strong> 🎙️ Just discovered an amazing insight about content creation that will change how you think about podcasting...</p>
                            </div>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>2/6</strong> The key is not just creating content, but creating content that resonates with your audience on multiple platforms 🎯</p>
                            </div>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>3/6</strong> "Content is king, but context is kingdom" - This quote from the podcast really hit home 👑</p>
                            </div>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>4/6</strong> Here are 3 actionable strategies mentioned:<br>
                                • Repurpose everything<br>
                                • Know your audience<br>
                                • Stay consistent</p>
                            </div>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>5/6</strong> The most surprising stat: 73% of creators don't repurpose their content effectively 📈</p>
                            </div>
                            <div style="background: white; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border-left: 3px solid #1da1f2;">
                                <p><strong>6/6</strong> What's your biggest content creation challenge? Drop a comment below! 👇</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                elif content_type == "LinkedIn Post":
                    st.markdown("""
                        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #0077b5;">
                            <h4 style="color: #0077b5;">💼 LinkedIn Post</h4>
                            <div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #e0e0e0;">
                                <p style="font-size: 1.1rem; line-height: 1.6;">The content creation landscape is evolving rapidly, and podcasters who adapt will thrive.</p>
                                <p style="margin: 1rem 0;"><strong>Key insights from today's discussion:</strong></p>
                                <p>✅ Authenticity beats perfection every time<br>
                                ✅ Consistent value delivery builds trust<br>
                                ✅ Multi-platform thinking from day one</p>
                                <blockquote style="border-left: 3px solid #0077b5; padding-left: 1rem; margin: 1rem 0; font-style: italic; color: #666;">
                                    "Your audience doesn't just want content, they want connection."
                                </blockquote>
                                <p>What strategies have worked best for your content? Let's discuss in the comments.</p>
                                <p style="color: #0077b5; font-weight: bold;">#ContentCreation #Podcasting #Marketing #Leadership</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                elif content_type == "Blog Post":
                    st.markdown("""
                        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #ff6b35;">
                            <h4 style="color: #ff6b35;">📝 Blog Post Outline</h4>
                            <div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #e0e0e0;">
                                <h5 style="color: #333; border-bottom: 2px solid #e0e0e0; padding-bottom: 0.5rem;">Title: "The Ultimate Guide to Content Repurposing for Podcasters"</h5>
                                <div style="margin: 1rem 0;">
                                    <p><strong>🎯 Introduction:</strong> Hook about content creation challenges</p>
                                    <p><strong>📊 Section 1:</strong> Why Repurposing Matters</p>
                                    <p><strong>🚀 Section 2:</strong> The 5-Platform Strategy</p>
                                    <p><strong>🛠️ Section 3:</strong> Tools and Techniques</p>
                                    <p><strong>📈 Section 4:</strong> Measuring Success</p>
                                    <p><strong>✅ Conclusion:</strong> Action steps and next steps</p>
                                    <p><strong>📞 CTA:</strong> Download free template</p>
                                </div>
                                <div style="background: #f0f2f6; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                                    <small><strong>Estimated read time:</strong> 8-10 minutes | <strong>Word count:</strong> ~2,000 words</small>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Enhanced action buttons
                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
                with col1:
                    if st.button(f"📋 Copy", key=f"copy_{i}", help=f"Copy {content_type} to clipboard"):
                        st.success("Content copied to clipboard!")
                with col2:
                    if st.button(f"📥 Download", key=f"download_{i}", help=f"Download {content_type} as text file"):
                        st.success("Download started!")
                with col3:
                    if st.button(f"🔄 Regenerate", key=f"regen_{i}", help=f"Generate new version of {content_type}"):
                        st.info("Regenerating content...")
                with col4:
                    if st.button(f"📤 Share", key=f"share_{i}", help=f"Share {content_type}"):
                        st.success("Share link created!")
else:
    # Show empty state with call to action
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem; background: #f8f9fa; border-radius: 15px; margin: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎙️</div>
        <h3 style="color: #667eea;">Ready to Transform Your Podcast?</h3>
        <p style="color: #666; font-size: 1.1rem; margin-bottom: 2rem;">Upload your audio file or paste a YouTube link to get started</p>
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 2rem auto; max-width: 500px;">
            <h4 style="color: #333;">✨ What you'll get:</h4>
            <div style="text-align: left; margin: 1rem 0;">
                <p>🐦 Engaging Twitter threads</p>
                <p>💼 Professional LinkedIn posts</p>
                <p>📝 SEO-optimized blog outlines</p>
                <p>📬 Newsletter-ready content</p>
                <p>🎬 Video scripts for shorts</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Analytics and insights section
if st.session_state.uploaded_file or st.session_state.youtube_url:
    st.markdown("---")
    st.markdown("## 📈 Content Analytics & Insights")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Total Duration", "45:32", "2:15")
    with col2:
        st.metric("💬 Word Count", "6,847", "234")
    with col3:
        st.metric("🎯 Key Topics", "7", "1")
    with col4:
        st.metric("⭐ Quotable Moments", "12", "3")
    
    # Topic breakdown
    st.markdown("### 🏷️ Topic Breakdown")
    topics_data = {
        'Topic': ['Content Strategy', 'Social Media', 'Productivity', 'Marketing', 'Technology'],
        'Mentions': [23, 18, 15, 12, 8],
        'Relevance': [95, 87, 82, 78, 65]
    }
    st.bar_chart(pd.DataFrame(topics_data).set_index('Topic')['Mentions'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>🎙️ <strong>Podcast to Content Agent</strong> - Transforming audio into engaging content</p>
    <p>Built with ❤️ using Streamlit | Version 1.0.0</p>
</div>
""", unsafe_allow_html=True)
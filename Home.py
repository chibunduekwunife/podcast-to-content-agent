import streamlit as st
import time
import random

# Page config for multipage app
st.set_page_config(
    page_title="Podcast to Content Agent",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .main-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 2rem;
    }
    .stats-container {
        background: linear-gradient(45deg, #f8f9fa, #ffffff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    .feature-highlight {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .feature-highlight:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
    }
    .quick-action-btn {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .quick-action-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    .sidebar-section {
        background: linear-gradient(45deg, #f8f9fa, #ffffff);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    .recent-activity {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #28a745;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: scale(1.05);
    }
    .progress-ring {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: conic-gradient(#667eea 0deg 252deg, #e9ecef 252deg 360deg);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem;
    }
    .progress-inner {
        width: 40px;
        height: 40px;
        background: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Navigation Sidebar
st.sidebar.markdown("""
<div class="sidebar-section">
    <h2 style="color: #667eea; margin-bottom: 1rem;">🧭 Navigation</h2>
    <p style="color: #666; font-size: 0.9rem;">Explore different sections of the app</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.page_link("pages/landing_page.py", label="🏠 Landing Page", icon="🏠")
st.sidebar.page_link("pages/streamlit_app.py", label="🚀 Content Generator", icon="🚀")

# Quick Actions in Sidebar
st.sidebar.markdown("""
<div class="sidebar-section">
    <h3 style="color: #667eea;">⚡ Quick Actions</h3>
</div>
""", unsafe_allow_html=True)

if st.sidebar.button("🎙️ Upload Podcast", help="Go directly to upload"):
    st.switch_page("pages/streamlit_app.py")

if st.sidebar.button("📊 View Analytics", help="See your content stats"):
    st.info("Analytics coming soon!")

if st.sidebar.button("💡 Get Inspired", help="See example content"):
    st.success("Check out the sample content in the main app!")

# Recent Activity
st.sidebar.markdown("""
<div class="sidebar-section">
    <h3 style="color: #667eea;">📈 Recent Activity</h3>
</div>
""", unsafe_allow_html=True)

recent_activities = [
    "🎵 New podcast processed - 'Tech Trends 2025'",
    "📱 5 Twitter threads generated",
    "💼 3 LinkedIn posts created", 
    "📝 Blog post outline ready"
]

for activity in recent_activities:
    st.sidebar.markdown(f"""
    <div class="recent-activity">
        <small>{activity}</small>
    </div>
    """, unsafe_allow_html=True)

# Main Hero Section
st.markdown("""
<div class="main-header">
    <div class="main-title">🎙️ Podcast to Content Agent</div>
    <div class="main-subtitle">Transform your audio into viral content across all platforms</div>
    <p style="font-size: 1rem; margin-bottom: 2rem;">
        Your AI-powered content creation companion that turns one podcast into 15+ pieces of engaging content
    </p>
</div>
""", unsafe_allow_html=True)

# Quick Action Buttons
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("🚀 Start Creating", key="start_creating", help="Begin content generation"):
        st.switch_page("pages/streamlit_app.py")
with col2:
    if st.button("📖 Learn More", key="learn_more", help="Explore features"):
        st.switch_page("pages/landing_page.py")
with col3:
    if st.button("� View Demo", key="view_demo", help="See it in action"):
        st.info("Demo available in the main app!")
with col4:
    if st.button("💬 Get Support", key="get_support", help="Need help?"):
        st.success("Support: support@podcastagent.com")

# Enhanced Stats Section
st.markdown("""
<div class="stats-container">
    <h2 style="text-align: center; color: #333; margin-bottom: 2rem;">📊 Platform Impact</h2>
</div>
""", unsafe_allow_html=True)

# Dynamic stats with progress indicators
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="progress-ring">
            <div class="progress-inner">70%</div>
        </div>
        <h3 style="color: #667eea;">1,247</h3>
        <p style="color: #666;">Podcasts Processed</p>
        <small style="color: #28a745;">+12 today</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="progress-ring">
            <div class="progress-inner">85%</div>
        </div>
        <h3 style="color: #667eea;">18,705</h3>
        <p style="color: #666;">Content Pieces</p>
        <small style="color: #28a745;">+156 today</small>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="progress-ring">
            <div class="progress-inner">92%</div>
        </div>
        <h3 style="color: #667eea;">342</h3>
        <p style="color: #666;">Happy Creators</p>
        <small style="color: #28a745;">+8 today</small>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="progress-ring">
            <div class="progress-inner">95%</div>
        </div>
        <h3 style="color: #667eea;">4,980</h3>
        <p style="color: #666;">Hours Saved</p>
        <small style="color: #28a745;">+40 today</small>
    </div>
    """, unsafe_allow_html=True)

# Feature Highlights
st.markdown("---")
st.markdown("## ✨ Why Creators Love Our Platform")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-highlight">
        <h3>⚡ Lightning Fast Processing</h3>
        <p>Upload your podcast and get 15+ content pieces in under 10 minutes. Our AI works at superhuman speed while maintaining quality.</p>
        <div style="background: #e3f2fd; padding: 0.5rem; border-radius: 5px; margin-top: 1rem;">
            <strong>Average Processing Time: 8 minutes</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-highlight">
        <h3>🎯 Platform-Optimized Content</h3>
        <p>Each piece is tailored for its specific platform - Twitter threads with hooks, LinkedIn posts with professional tone, blog posts with SEO optimization.</p>
        <div style="background: #f3e5f5; padding: 0.5rem; border-radius: 5px; margin-top: 1rem;">
            <strong>6 Different Content Types</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-highlight">
        <h3>🤖 Advanced AI Technology</h3>
        <p>Powered by OpenAI's latest models, our AI understands context, tone, and audience to create content that resonates.</p>
        <div style="background: #e8f5e8; padding: 0.5rem; border-radius: 5px; margin-top: 1rem;">
            <strong>97% Accuracy Rate</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-highlight">
        <h3>📈 Proven Results</h3>
        <p>Creators see 300% increase in engagement and save 10+ hours per week. Turn your podcast into a content empire.</p>
        <div style="background: #fff3e0; padding: 0.5rem; border-radius: 5px; margin-top: 1rem;">
            <strong>300% Engagement Boost</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Live Status
st.markdown("---")
st.markdown("## 🔴 Live Platform Status")

status_col1, status_col2, status_col3 = st.columns(3)
with status_col1:
    st.success("🟢 AI Processing: Operational")
with status_col2:
    st.success("🟢 Content Generation: Optimal")
with status_col3:
    st.success("🟢 All Systems: Ready")

# Call to Action
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 3rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
    <h2 style="margin-bottom: 1rem;">Ready to Transform Your Content Strategy?</h2>
    <p style="font-size: 1.1rem; margin-bottom: 2rem;">Join thousands of creators who are already scaling their content with AI</p>
</div>
""", unsafe_allow_html=True)

final_col1, final_col2, final_col3 = st.columns([1, 1, 1])
with final_col2:
    if st.button("🎯 Start Your First Podcast", key="final_cta", help="Transform your content now"):
        st.switch_page("pages/streamlit_app.py")

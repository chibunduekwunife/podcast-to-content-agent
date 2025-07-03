import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="🎙️ Podcast to Content Agent - Landing",
    page_icon="🎙️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 4rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .pricing-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 1rem;
    }
    .pricing-card.featured {
        border: 3px solid #667eea;
        transform: scale(1.05);
    }
    .cta-section {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 3rem 0;
    }
    .stat-container {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    .workflow-step {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🎙️ Podcast to Content Agent</div>
    <div class="hero-subtitle">Transform your podcasts into viral content across all platforms in minutes, not hours</div>
    <p>Stop spending endless hours manually editing and repurposing your podcast content. Let AI do the heavy lifting while you focus on creating amazing content.</p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Try It Free Now", key="hero_cta", help="Start transforming your content today"):
        st.switch_page("pages/streamlit_app.py")

# Problem Statement
st.markdown("---")
st.markdown("## 😫 The Content Creator's Dilemma")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    ### ⏰ Time-Consuming Manual Work
    - Hours spent transcribing audio
    - Manual content adaptation for each platform
    - Repetitive formatting and editing
    - Missing opportunities for viral content
    """)

with col2:
    st.markdown("""
    ### 💸 Missed Revenue Opportunities
    - Content sits unused after initial publish
    - Limited reach across platforms
    - Inconsistent posting schedules
    - No time for audience engagement
    """)

# Solution Overview
st.markdown("---")
st.markdown("## ✨ Our Solution: AI-Powered Content Transformation")

st.markdown("""
<div class="stat-container">
    <h3 style="text-align: center; margin-bottom: 2rem;">⚡ From 1 Podcast to 15+ Content Pieces in Under 10 Minutes</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align: center;">
        <div>
            <h2>🎙️ 1</h2>
            <p>Podcast Upload</p>
        </div>
        <div>
            <h2>⚡ 10</h2>
            <p>Minutes Processing</p>
        </div>
        <div>
            <h2>📱 15+</h2>
            <p>Content Pieces</p>
        </div>
        <div>
            <h2>🚀 ∞</h2>
            <p>Platform Reach</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works
st.markdown("## 🔄 How It Works")

workflow_steps = [
    {
        "step": "1",
        "icon": "🎵",
        "title": "Upload Your Content",
        "description": "Drop your MP3, MP4, or share a YouTube link. We support all major audio formats."
    },
    {
        "step": "2", 
        "icon": "🤖",
        "title": "AI Transcription & Analysis",
        "description": "Our AI transcribes your content and identifies key topics, quotes, and insights."
    },
    {
        "step": "3",
        "icon": "✍️", 
        "title": "Content Generation",
        "description": "Generate Twitter threads, LinkedIn posts, blog outlines, and more - all optimized for each platform."
    },
    {
        "step": "4",
        "icon": "📱",
        "title": "Publish & Scale",
        "description": "Copy, download, or directly publish to your favorite platforms. Watch your reach explode!"
    }
]

for step in workflow_steps:
    st.markdown(f"""
    <div class="workflow-step">
        <h3>{step['icon']} Step {step['step']}: {step['title']}</h3>
        <p>{step['description']}</p>
    </div>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("---")
st.markdown("## 🎯 Powerful Features")

features = [
    {
        "icon": "🐦",
        "title": "Twitter Threads",
        "description": "Engaging threads with hooks, key points, and CTAs that drive engagement and followers."
    },
    {
        "icon": "💼", 
        "title": "LinkedIn Posts",
        "description": "Professional posts optimized for LinkedIn's algorithm with industry insights and thought leadership."
    },
    {
        "icon": "📝",
        "title": "Blog Posts",
        "description": "SEO-optimized blog outlines and full articles ready for your website or Medium."
    },
    {
        "icon": "📬",
        "title": "Newsletter Content", 
        "description": "Engaging newsletter snippets perfect for Substack, ConvertKit, or Mailchimp."
    },
    {
        "icon": "🎬",
        "title": "Video Scripts",
        "description": "YouTube Shorts and TikTok scripts with hooks, punchlines, and clear CTAs."
    },
    {
        "icon": "⏰",
        "title": "Smart Timestamps",
        "description": "Automatic chapter detection and timestamp generation for easy navigation."
    }
]

# Display features in a grid
cols = st.columns(3)
for i, feature in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature['icon']}</div>
            <h3>{feature['title']}</h3>
            <p>{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Use Cases
st.markdown("---")
st.markdown("## 🎯 Perfect For")

use_cases = [
    "🎙️ **Podcast Creators** - Maximize reach from every episode",
    "📱 **Content Creators** - Repurpose long-form content efficiently", 
    "🏢 **Marketing Agencies** - Scale content production for clients",
    "💼 **Business Owners** - Turn webinars into marketing content",
    "🎓 **Educators** - Create educational content across platforms",
    "📺 **YouTubers** - Transform videos into social media content"
]

col1, col2 = st.columns(2)
for i, use_case in enumerate(use_cases):
    with col1 if i % 2 == 0 else col2:
        st.markdown(use_case)

# Pricing Section
st.markdown("---")
st.markdown("## 💰 Simple, Transparent Pricing")

pricing_col1, pricing_col2, pricing_col3 = st.columns(3)

with pricing_col1:
    st.markdown("""
    <div class="pricing-card">
        <h3>🆓 Free</h3>
        <h2>$0<span style="font-size: 1rem;">/month</span></h2>
        <ul style="text-align: left;">
            <li>✅ 3 uploads per month</li>
            <li>✅ Basic content types</li>
            <li>✅ Standard processing</li>
            <li>❌ No priority support</li>
        </ul>
        <button style="width: 100%; padding: 1rem; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer;">Get Started</button>
    </div>
    """, unsafe_allow_html=True)

with pricing_col2:
    st.markdown("""
    <div class="pricing-card featured">
        <h3>⭐ Pro</h3>
        <h2>$29<span style="font-size: 1rem;">/month</span></h2>
        <ul style="text-align: left;">
            <li>✅ Unlimited uploads</li>
            <li>✅ All content types</li>
            <li>✅ Priority processing</li>
            <li>✅ Advanced templates</li>
            <li>✅ API access</li>
        </ul>
        <button style="width: 100%; padding: 1rem; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer;">Start Free Trial</button>
    </div>
    """, unsafe_allow_html=True)

with pricing_col3:
    st.markdown("""
    <div class="pricing-card">
        <h3>🚀 Agency</h3>
        <h2>$99<span style="font-size: 1rem;">/month</span></h2>
        <ul style="text-align: left;">
            <li>✅ Everything in Pro</li>
            <li>✅ Team collaboration</li>
            <li>✅ White-label options</li>
            <li>✅ Custom integrations</li>
            <li>✅ Priority support</li>
        </ul>
        <button style="width: 100%; padding: 1rem; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer;">Contact Sales</button>
    </div>
    """, unsafe_allow_html=True)

# Social Proof
st.markdown("---")
st.markdown("## 🌟 What Creators Are Saying")

testimonials = [
    {
        "name": "Sarah Johnson",
        "role": "Podcast Host @TechTalks",
        "quote": "This tool saved me 10+ hours per week. My Twitter engagement increased by 300% since I started using it!",
        "avatar": "👩‍💼"
    },
    {
        "name": "Mike Chen", 
        "role": "Content Creator @GrowthHacking",
        "quote": "Game-changer! I went from 1 piece of content per week to 15+ pieces. My audience growth has been incredible.",
        "avatar": "👨‍💻"
    },
    {
        "name": "Emily Rodriguez",
        "role": "Marketing Agency Owner",
        "quote": "Our clients love the quality and speed. We've been able to take on 3x more clients with the same team size.",
        "avatar": "👩‍🚀"
    }
]

for testimonial in testimonials:
    st.markdown(f"""
    <div class="feature-card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 3rem; margin-right: 1rem;">{testimonial['avatar']}</span>
            <div>
                <h4 style="margin: 0;">{testimonial['name']}</h4>
                <p style="margin: 0; color: #666;">{testimonial['role']}</p>
            </div>
        </div>
        <p style="font-style: italic;">"{testimonial['quote']}"</p>
    </div>
    """, unsafe_allow_html=True)

# Final CTA
st.markdown("""
<div class="cta-section">
    <h2>🚀 Ready to Transform Your Content Strategy?</h2>
    <p>Join thousands of creators who are already scaling their content with AI</p>
    <p><strong>Start your free trial today - no credit card required!</strong></p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🎯 Start Creating Content Now", key="final_cta", help="Transform your first podcast now"):
        st.switch_page("pages/streamlit_app.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; background: #f8f9fa; border-radius: 10px;">
    <h3>🎙️ Podcast to Content Agent</h3>
    <p>Built with ❤️ for content creators everywhere</p>
    <p>
        <a href="#" style="margin: 0 1rem; color: #667eea; text-decoration: none;">📧 Contact</a> |
        <a href="#" style="margin: 0 1rem; color: #667eea; text-decoration: none;">📋 Terms</a> |
        <a href="#" style="margin: 0 1rem; color: #667eea; text-decoration: none;">🔒 Privacy</a> |
        <a href="#" style="margin: 0 1rem; color: #667eea; text-decoration: none;">❓ Help</a>
    </p>
</div>
""", unsafe_allow_html=True)
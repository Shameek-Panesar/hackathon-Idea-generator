"""
Knowledge base of sample hackathon ideas for RAG implementation.
This serves as the context for retrieval-augmented generation.
"""

HACKATHON_IDEAS = [
    {
        "title": "EcoTrack - Carbon Footprint Tracker",
        "description": "A mobile app that helps users track their daily carbon footprint through activities like transportation, food consumption, and energy usage. Uses AI to provide personalized recommendations for reducing environmental impact.",
        "theme": "Sustainability",
        "difficulty": "Intermediate",
        "tech_stack": ["React Native", "Python", "TensorFlow", "Firebase"],
        "team_size": "3-4"
    },
    {
        "title": "MediConnect - Telemedicine Platform",
        "description": "A comprehensive telemedicine platform connecting patients with healthcare providers. Features include video consultations, AI-powered symptom checker, prescription management, and health record storage.",
        "theme": "Healthcare",
        "difficulty": "Advanced",
        "tech_stack": ["React", "Node.js", "MongoDB", "WebRTC", "OpenAI API"],
        "team_size": "4-5"
    },
    {
        "title": "LearnAI - Personalized Education Assistant",
        "description": "An AI-powered learning companion that adapts to individual learning styles. Generates custom practice problems, explains concepts in different ways, and tracks progress over time.",
        "theme": "Education",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "FastAPI", "React", "OpenAI API", "PostgreSQL"],
        "team_size": "3-4"
    },
    {
        "title": "BlockVote - Blockchain Voting System",
        "description": "A secure, transparent voting system built on blockchain technology. Ensures vote integrity, prevents fraud, and provides real-time results while maintaining voter anonymity.",
        "theme": "Blockchain",
        "difficulty": "Advanced",
        "tech_stack": ["Solidity", "Ethereum", "Web3.js", "React", "IPFS"],
        "team_size": "4-5"
    },
    {
        "title": "SafeRoute - Women's Safety Navigation",
        "description": "A navigation app specifically designed for women's safety. Uses crowdsourced data, police reports, and lighting information to suggest the safest routes. Includes SOS features and community alerts.",
        "theme": "Social Impact",
        "difficulty": "Intermediate",
        "tech_stack": ["Flutter", "Google Maps API", "Firebase", "Python"],
        "team_size": "3-4"
    },
    {
        "title": "FoodShare - Community Food Redistribution",
        "description": "A platform connecting restaurants and grocery stores with excess food to local food banks and shelters. Uses AI to optimize pickup routes and predict surplus food availability.",
        "theme": "Social Impact",
        "difficulty": "Beginner",
        "tech_stack": ["React", "Node.js", "MongoDB", "Google Maps API"],
        "team_size": "2-3"
    },
    {
        "title": "AR Museum Guide",
        "description": "An augmented reality app that brings museum exhibits to life. Point your phone at artifacts to see 3D reconstructions, historical context, and interactive storytelling.",
        "theme": "AR/VR",
        "difficulty": "Advanced",
        "tech_stack": ["Unity", "ARKit", "ARCore", "C#", "Firebase"],
        "team_size": "4-5"
    },
    {
        "title": "CodeMentor - AI Pair Programming",
        "description": "An AI-powered coding assistant that provides real-time code reviews, suggests improvements, explains complex algorithms, and helps debug issues. Integrated as a VS Code extension.",
        "theme": "Developer Tools",
        "difficulty": "Advanced",
        "tech_stack": ["TypeScript", "VS Code API", "OpenAI API", "Python"],
        "team_size": "3-4"
    },
    {
        "title": "FitnessBuddy - AI Personal Trainer",
        "description": "A computer vision-based fitness app that uses your phone camera to track exercise form, count reps, and provide real-time feedback. Generates personalized workout plans based on goals and progress.",
        "theme": "Health & Fitness",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "OpenCV", "TensorFlow", "React Native", "Firebase"],
        "team_size": "3-4"
    },
    {
        "title": "LocalLang - Community Language Exchange",
        "description": "A platform connecting language learners with native speakers for conversation practice. Uses AI to match users based on interests, schedule, and learning goals. Includes gamification elements.",
        "theme": "Education",
        "difficulty": "Beginner",
        "tech_stack": ["React", "Node.js", "Socket.io", "MongoDB", "WebRTC"],
        "team_size": "2-3"
    },
    {
        "title": "SmartFarm - IoT Agriculture Monitor",
        "description": "An IoT solution for farmers to monitor soil moisture, temperature, humidity, and crop health. Uses machine learning to predict optimal harvest times and detect plant diseases early.",
        "theme": "IoT",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Raspberry Pi", "TensorFlow", "MQTT", "React"],
        "team_size": "4-5"
    },
    {
        "title": "MindfulMoments - Mental Health Companion",
        "description": "An AI chatbot focused on mental health support. Provides daily check-ins, mood tracking, meditation guides, and connects users with professional resources when needed.",
        "theme": "Healthcare",
        "difficulty": "Intermediate",
        "tech_stack": ["Python", "OpenAI API", "React", "PostgreSQL", "Docker"],
        "team_size": "3-4"
    },
    {
        "title": "GreenCommute - Carpooling Optimizer",
        "description": "A smart carpooling platform that uses AI to match commuters with similar routes and schedules. Calculates carbon savings and provides incentives for regular carpoolers.",
        "theme": "Sustainability",
        "difficulty": "Beginner",
        "tech_stack": ["React Native", "Node.js", "MongoDB", "Google Maps API"],
        "team_size": "2-3"
    },
    {
        "title": "SkillSwap - Peer-to-Peer Learning",
        "description": "A platform where people can exchange skills without money. Want to learn guitar? Teach someone coding in exchange. Uses matching algorithms and includes video chat capabilities.",
        "theme": "Education",
        "difficulty": "Intermediate",
        "tech_stack": ["Vue.js", "Python", "FastAPI", "PostgreSQL", "WebRTC"],
        "team_size": "3-4"
    },
    {
        "title": "DisasterAlert - Emergency Response System",
        "description": "A real-time disaster alert and coordination system. Aggregates data from weather services, seismic sensors, and social media to provide early warnings and coordinate relief efforts.",
        "theme": "Social Impact",
        "difficulty": "Advanced",
        "tech_stack": ["Python", "Apache Kafka", "React", "MongoDB", "ML Models"],
        "team_size": "4-5"
    },
    {
        "title": "NFT Art Gallery - Virtual Exhibition Space",
        "description": "A virtual 3D gallery for displaying and trading NFT art. Users can walk through exhibitions, attend virtual art shows, and purchase digital artwork using cryptocurrency.",
        "theme": "Blockchain",
        "difficulty": "Advanced",
        "tech_stack": ["Three.js", "Solidity", "Web3.js", "React", "IPFS"],
        "team_size": "4-5"
    },
    {
        "title": "ResumeAI - Smart Resume Builder",
        "description": "An AI-powered resume builder that analyzes job descriptions and optimizes your resume accordingly. Provides suggestions for improvements and predicts compatibility with positions.",
        "theme": "Career",
        "difficulty": "Beginner",
        "tech_stack": ["React", "Python", "OpenAI API", "MongoDB", "FastAPI"],
        "team_size": "2-3"
    },
    {
        "title": "PetPal - Pet Adoption Platform",
        "description": "A comprehensive pet adoption platform with AI-powered matching between pets and potential owners. Includes virtual meet-and-greets, adoption guides, and post-adoption support.",
        "theme": "Social Impact",
        "difficulty": "Beginner",
        "tech_stack": ["React", "Node.js", "MongoDB", "WebRTC", "Stripe"],
        "team_size": "3-4"
    },
    {
        "title": "CryptoLearn - Blockchain Education Game",
        "description": "An interactive game that teaches blockchain concepts through challenges and simulations. Players learn about consensus mechanisms, smart contracts, and DeFi by building their own virtual blockchain.",
        "theme": "Blockchain",
        "difficulty": "Intermediate",
        "tech_stack": ["Unity", "C#", "Solidity", "Web3.js", "Firebase"],
        "team_size": "3-4"
    },
    {
        "title": "AccessibleWeb - Automatic Accessibility Enhancer",
        "description": "A browser extension that automatically improves web accessibility. Adds alt text to images using AI, enhances color contrast, provides text-to-speech, and simplifies navigation for users with disabilities.",
        "theme": "Accessibility",
        "difficulty": "Intermediate",
        "tech_stack": ["JavaScript", "OpenAI API", "Chrome Extension API", "React"],
        "team_size": "2-3"
    }
]

def get_all_ideas():
    """Return all hackathon ideas from the knowledge base."""
    return HACKATHON_IDEAS

def get_ideas_by_theme(theme):
    """Filter ideas by theme."""
    return [idea for idea in HACKATHON_IDEAS if idea["theme"].lower() == theme.lower()]

def get_ideas_by_difficulty(difficulty):
    """Filter ideas by difficulty level."""
    return [idea for idea in HACKATHON_IDEAS if idea["difficulty"].lower() == difficulty.lower()]

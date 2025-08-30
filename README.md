# 🧠 Activation Function Visualizer with AI Explainer

A beautiful, interactive Flask web application for visualizing and understanding neural network activation functions. Now featuring an AI-powered assistant using Google's Gemini API for explaining and answering questions about activation functions. Built with a modern dark theme for an optimal learning experience.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)
![Gemini](https://img.shields.io/badge/Gemini-AI-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

### 🤖 AI-Powered Learning Assistant
- **Gemini AI Integration** - Ask questions about activation functions and get expert responses
- **Markdown Rendering** - AI responses are beautifully formatted with headers, lists, code blocks, and tables
- **Interactive Chat Interface** - Real-time question-and-answer system
- **Educational Context** - AI specifically trained to provide educational explanations about neural networks

### 📊 Interactive Visualization
- **Real-time plotting** of activation functions with matplotlib
- **Dark theme** with vibrant green accents for comfortable viewing
- **Responsive design** that works on desktop and mobile devices
- **Smooth animations** and transitions for better user experience

### 🔧 Supported Activation Functions
- **Sigmoid** - Classic S-shaped function, output range (0, 1)
- **Tanh** - Hyperbolic tangent, zero-centered output (-1, 1)
- **ReLU** - Rectified Linear Unit, most popular for hidden layers
- **Leaky ReLU** - Prevents dead neurons with small negative slope
- **Swish** - Self-gated function, often outperforms ReLU
- **GELU** - Gaussian Error Linear Unit, used in modern transformers
- **ELU** - Exponential Linear Unit, smooth everywhere

### 🎯 Educational Features
- **AI Question & Answer** - Ask anything about activation functions and get detailed explanations
- **Markdown-formatted responses** - Code examples, tables, and formatted text for better learning
- **Input/Output calculation** for any given value
- **Interactive point marking** on the function curve
- **Contextual AI responses** - Explanations tailored to neural network education

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- uv package manager
- Google Gemini API key

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-web-app
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   ```

3. **Set up environment variables**
   <br>Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   **Get your Gemini API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create a new API key
   - Copy the key to your `.env` file

4. **Run the application**
   ```bash
   uv run app.py
   ```

5. **Open your browser**
   <br>Navigate to `http://localhost:5000`

## 🖥️ Usage

### Basic Visualization
1. **Select an activation function** from the dropdown menu
2. **Enter an input value** to see the specific output
3. **Click "Visualize & Calculate"** to update the plot
4. **View the results** in the calculation panel below

### AI Assistant Features
1. **Ask questions** in the text area at the bottom of the page
2. **Get instant AI responses** about activation functions, powered by Gemini
3. **Example questions you can ask:**
- "What is ReLU?"
- "What is the difference between Sigmoid and Tanh?"
- "When should I use GELU?"
- "Explain the vanishing gradient problem."
- "How does Swish compare to other activation functions?"

### Advanced Features
- **Real-time updates**: The plot updates automatically as you change the input value
- **Keyboard shortcuts**: 
  - Press Enter in the input field to trigger visualization updates
  - Press Ctrl+Enter (or Cmd+Enter on Mac) in the question box to ask the AI
- **Mobile-friendly**: Responsive design works on all screen sizes
- **Markdown rendering**: AI responses include formatted code, tables, and structured content

## 📁 Project Structure

```
ai-web-app/
├── app.py                 # Flask application with activation functions and Gemini AI integration
├── templates/
│   └── index.html         # Main HTML template with styling and AI chat interface
├── test/
│   └── test_gemini.py     # Gemini API testing and examples
├── pyproject.toml         # Project configuration and dependencies
├── .env                   # Environment variables (create this file)
├── README.md              # This file
└── uv.lock               # Dependency lock file
```

## 🧮 Mathematical Background

### What are Activation Functions?
Activation functions are mathematical functions that determine the output of a neural network node. They introduce **non-linearity** into the network, which is crucial for learning complex patterns.

### Why Non-linearity Matters
Without activation functions, neural networks would be limited to learning only linear relationships. Non-linear activation functions enable networks to:
- Learn complex patterns and decision boundaries
- Approximate any continuous function (Universal Approximation Theorem)
- Solve real-world problems like image recognition and natural language processing

### Function Characteristics

| Function | Range | Advantages | Disadvantages |
|----------|-------|------------|---------------|
| Sigmoid | (0, 1) | Smooth, probabilistic output | Vanishing gradients |
| Tanh | (-1, 1) | Zero-centered, smooth | Vanishing gradients |
| ReLU | [0, ∞) | Simple, fast, avoids vanishing gradients | Dead neurons |
| Leaky ReLU | (-∞, ∞) | Prevents dead neurons | Requires tuning |
| Swish | (-∞, ∞) | Self-gated, smooth | More computationally expensive |
| GELU | (-∞, ∞) | Smooth, probabilistic | Complex computation |
| ELU | (-α, ∞) | Smooth, negative outputs | Exponential computation |

## 🎨 Design Features

### Dark Theme
- **Primary Background**: Deep dark blue (#0d1117)
- **Secondary Background**: Charcoal (#161b22)
- **Accent Color**: Bright green (#00ff88)
- **Text Colors**: Various shades of gray for optimal readability

### Responsive Layout
- **Grid-based design** that adapts to different screen sizes
- **Mobile-first approach** with touch-friendly controls
- **Accessible color schemes** with high contrast ratios

## 🔧 Technical Details

### Backend (Flask)
- **Route handling** for main page, plotting, calculations, and AI chat
- **Gemini AI integration** using Google's genai library
- **Matplotlib integration** with non-interactive backend
- **Error handling** for invalid inputs, API failures, and edge cases
- **JSON API** for seamless frontend communication
- **Environment variable management** for secure API key handling

### Frontend (HTML/CSS/JavaScript)
- **Vanilla JavaScript** for lightweight, fast interactions
- **Marked.js integration** for Markdown rendering
- **CSS Grid and Flexbox** for responsive layouts
- **Fetch API** for asynchronous server communication
- **Event handling** for real-time updates and AI interactions
- **Markdown styling** with syntax highlighting and proper formatting

### AI Features
- **Contextual responses** - AI understands it's helping with activation function education
- **Markdown output** - Responses include formatted code blocks, tables, and structured content
- **Error handling** - Graceful fallbacks when API is unavailable
- **Real-time interaction** - Instant responses with loading states

### Security Features
- **Input validation** to prevent injection attacks
- **Numpy clipping** to prevent overflow errors
- **Error boundaries** for graceful failure handling
- **Environment variable protection** for API keys
- **Sanitized Markdown rendering** with XSS protection

## 🤖 AI Assistant Details

### Gemini Integration
The application uses Google's Gemini 2.5 Flash model to provide intelligent responses about activation functions. The AI is specifically contextualized to act as an expert in neural networks and activation functions.

### Example Interactions
**Question**: "What's the difference between ReLU and Sigmoid?"

**AI Response**: The AI will provide a detailed comparison including:
- Mathematical definitions
- Output ranges
- Gradient behavior
- Use cases in different neural network architectures
- Advantages and disadvantages

### Supported Question Types
- **Conceptual explanations** - "How do activation functions work?"
- **Comparisons** - "ReLU vs Sigmoid vs Tanh"
- **Implementation details** - "When to use GELU in transformers?"
- **Problem-solving** - "How to fix vanishing gradients?"
- **Mathematical insights** - "Derivative of Swish function"

### API Requirements
- **Gemini API Key** - Free tier available from Google AI Studio
- **Internet connection** - Required for API calls
- **Rate limits** - Respects Google's API rate limiting

## 🎨 Design Features

### Dark Theme
- **Primary Background**: Deep dark blue (#0d1117)
- **Secondary Background**: Charcoal (#161b22)
- **Accent Color**: Bright green (#00ff88)
- **Text Colors**: Various shades of gray for optimal readability

### Responsive Layout
- **Grid-based design** that adapts to different screen sizes
- **Mobile-first approach** with touch-friendly controls
- **Accessible color schemes** with high contrast ratios
- **AI chat interface** optimized for both desktop and mobile

## 📦 Dependencies

### Python Packages (managed by uv)
- **Flask** - Web framework for the application
- **NumPy** - Numerical computations for activation functions
- **Matplotlib** - Plotting and visualization
- **python-dotenv** - Environment variable management
- **google-genai** - Google Gemini AI integration

### Frontend Libraries (CDN)
- **Marked.js** - Markdown parsing and rendering
- **Vanilla JavaScript** - No additional frameworks required

### Development Tools
- **uv** - Fast Python package manager
- **Git** - Version control
- **VS Code** - Recommended IDE with Python extensions

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Learning! 🎓**

*Explore the fascinating world of neural network activation functions and understand how they enable machines to learn complex patterns!*
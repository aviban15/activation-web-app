# 🧠 Activation Function Visualizer

A beautiful, interactive Flask web application for visualizing and understanding neural network activation functions. Built with a modern dark theme and green accents for an optimal learning experience.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Features

### 📊 Interactive Visualization
- **Real-time plotting** of activation functions with matplotlib
- **Dark theme** with vibrant green accents for comfortable viewing
- **Responsive design** that works on desktop and mobile devices
- **Smooth animations** and transitions for better user experience

### 🔧 Supported Activation Functions
- **Sigmoid** - Classic S-shaped function, output range (0, 1)
- **ReLU** - Rectified Linear Unit, most popular for hidden layers
- **Tanh** - Hyperbolic tangent, zero-centered output (-1, 1)
- **Leaky ReLU** - Prevents dead neurons with small negative slope
- **Swish** - Self-gated function, often outperforms ReLU
- **GELU** - Gaussian Error Linear Unit, used in modern transformers
- **ELU** - Exponential Linear Unit, smooth everywhere

### 🎯 Educational Features
- **Input/Output calculation** for any given value
- **Interactive point marking** on the function curve
- **Function descriptions** and use cases
- **Mathematical explanations** of non-linearity in neural networks

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- uv package manager

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

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🖥️ Usage

### Basic Usage
1. **Select an activation function** from the dropdown menu
2. **Enter an input value** to see the specific output
3. **Click "Visualize & Calculate"** to update the plot
4. **View the results** in the calculation panel below

### Advanced Features
- **Real-time updates**: The plot updates automatically as you change the input value
- **Keyboard shortcuts**: Press Enter in the input field to trigger updates
- **Mobile-friendly**: Responsive design works on all screen sizes

## 📁 Project Structure

```
ai-web-app/
├── main.py                 # Flask application and activation functions
├── templates/
│   └── index.html         # Main HTML template with styling
├── pyproject.toml         # Project configuration and dependencies
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
| ReLU | [0, ∞) | Simple, fast, avoids vanishing gradients | Dead neurons |
| Tanh | (-1, 1) | Zero-centered, smooth | Vanishing gradients |
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
- **Route handling** for main page, plotting, and calculations
- **Matplotlib integration** with non-interactive backend
- **Error handling** for invalid inputs and edge cases
- **JSON API** for seamless frontend communication

### Frontend (HTML/CSS/JavaScript)
- **Vanilla JavaScript** for lightweight, fast interactions
- **CSS Grid and Flexbox** for responsive layouts
- **Fetch API** for asynchronous server communication
- **Event handling** for real-time updates

### Security Features
- **Input validation** to prevent injection attacks
- **Numpy clipping** to prevent overflow errors
- **Error boundaries** for graceful failure handling

## 🧪 Development

### Running in Development Mode
```bash
# Enable debug mode
export FLASK_ENV=development
python main.py
```

### Code Quality
```bash
# Format code
black main.py

# Lint code
flake8 main.py

# Run tests (if available)
pytest
```

## 🚀 Deployment

### Local Deployment
The app runs on `0.0.0.0:5000` by default, making it accessible on your local network.

### Production Deployment
For production deployment, consider:
- Using a WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Configuring environment variables for security
- Using a process manager like systemd

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Learning! 🎓**

*Explore the fascinating world of neural network activation functions and understand how they enable machines to learn complex patterns!*
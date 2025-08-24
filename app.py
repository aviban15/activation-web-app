import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
import io
import base64
# import json

app = Flask(__name__)

# Activation functions
def sigmoid(x):
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip to prevent overflow

def tanh(x):
    """Tanh activation function"""
    return np.tanh(x)

def relu(x):
    """ReLU activation function"""
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.1):
    """Leaky ReLU activation function"""
    return np.where(x > 0, x, alpha * x)

def swish(x):
    """Swish activation function"""
    return x * sigmoid(x)

def gelu(x):
    """GELU activation function"""
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

def elu(x, alpha=1.0):
    """ELU activation function"""
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

# Dictionary of activation functions
ACTIVATION_FUNCTIONS = {
    'sigmoid': {'func': sigmoid, 'name': 'Sigmoid', 'range': (-10, 10)},
    'tanh': {'func': tanh, 'name': 'Tanh', 'range': (-5, 5)},
    'relu': {'func': relu, 'name': 'ReLU', 'range': (-5, 5)},
    'leaky_relu': {'func': leaky_relu, 'name': 'Leaky ReLU', 'range': (-5, 5)},
    'swish': {'func': swish, 'name': 'Swish', 'range': (-5, 5)},
    'gelu': {'func': gelu, 'name': 'GELU', 'range': (-3, 3)},
    'elu': {'func': elu, 'name': 'ELU', 'range': (-3, 5)}
}

def create_plot(func_name, input_value=None):
    """Create a plot of the activation function"""
    if func_name not in ACTIVATION_FUNCTIONS:
        return None
    
    func_info = ACTIVATION_FUNCTIONS[func_name]
    func = func_info['func']
    x_min, x_max = func_info['range']
    
    # Set dark theme for matplotlib
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    # Generate x values
    x = np.linspace(x_min, x_max, 1000)
    y = func(x)
    
    # Plot the function
    ax.plot(x, y, color='#00ff88', linewidth=2.5, label=func_info['name'])
    
    # Add input point if provided
    if input_value is not None:
        try:
            input_val = float(input_value)
            if x_min <= input_val <= x_max:
                output_val = func(np.array([input_val]))[0]
                ax.plot(input_val, output_val, 'o', color='#ff6b6b', markersize=10, 
                       label=f'Input: {input_val:.2f}, Output: {output_val:.4f}')
                
                # Add vertical and horizontal lines
                ax.axvline(x=input_val, color='#ff6b6b', linestyle='--', alpha=0.7)
                ax.axhline(y=output_val, color='#ff6b6b', linestyle='--', alpha=0.7)
        except ValueError:
            pass
    
    # Customize plot
    ax.grid(True, alpha=0.3, color='#404040')
    ax.set_xlabel('Input (x)', color='white', fontsize=12)
    ax.set_ylabel('Output f(x)', color='white', fontsize=12)
    ax.set_title(f'{func_info["name"]} Activation Function', color='white', fontsize=14, fontweight='bold')
    ax.legend(facecolor='#2a2a2a', edgecolor='#00ff88', framealpha=0.9)
    
    # Set tick colors
    ax.tick_params(colors='white')
    
    # Add zero lines
    ax.axhline(y=0, color='white', linewidth=0.8, alpha=0.5)
    ax.axvline(x=0, color='white', linewidth=0.8, alpha=0.5)
    
    plt.tight_layout()
    
    # Convert plot to base64 string
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', facecolor='#1a1a1a', edgecolor='none', dpi=100)
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.getvalue()).decode()
    plt.close()
    
    return img_data

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html', functions=ACTIVATION_FUNCTIONS)

@app.route('/plot')
def plot():
    """Generate plot for selected activation function"""
    func_name = request.args.get('function', 'sigmoid')
    input_value = request.args.get('input_value')
    
    img_data = create_plot(func_name, input_value)
    
    if img_data:
        return jsonify({
            'success': True,
            'image': img_data,
            'function_name': ACTIVATION_FUNCTIONS[func_name]['name']
        })
    else:
        return jsonify({'success': False, 'error': 'Invalid function'})

@app.route('/calculate')
def calculate():
    """Calculate output for given input"""
    func_name = request.args.get('function', 'sigmoid')
    input_value = request.args.get('input_value')
    
    if func_name not in ACTIVATION_FUNCTIONS:
        return jsonify({'success': False, 'error': 'Invalid function'})
    
    try:
        input_val = float(input_value)
        func = ACTIVATION_FUNCTIONS[func_name]['func']
        output_val = func(np.array([input_val]))[0]
        
        return jsonify({
            'success': True,
            'input': input_val,
            'output': float(output_val),
            'function_name': ACTIVATION_FUNCTIONS[func_name]['name']
        })
    except (ValueError, TypeError):
        return jsonify({'success': False, 'error': 'Invalid input value'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

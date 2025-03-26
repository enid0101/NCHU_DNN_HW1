import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get grid data from request
    data = request.json
    grid_size = data['gridSize']
    grid_data = data['gridData']
    
    # Parse grid data
    grid = np.zeros((grid_size, grid_size))
    start_pos = None
    end_pos = None
    
    for i in range(grid_size):
        for j in range(grid_size):
            cell_type = grid_data[i][j]
            if cell_type == 'start':
                start_pos = (i, j)
                grid[i][j] = 0
            elif cell_type == 'end':
                end_pos = (i, j)
                grid[i][j] = 20
            elif cell_type == 'obstacle':
                grid[i][j] = -5
            else:
                grid[i][j] = -0.1
    
    if start_pos is None or end_pos is None:
        return jsonify({'error': 'Start or end position not set'}), 400
    
    # Value Iteration
    v_map, policy = value_iteration(grid, grid_size, end_pos)
    
    # Find optimal path
    path = find_path(start_pos, end_pos, policy, grid_size)
    
    return jsonify({
        'valueMap': v_map.tolist(),
        'policyMap': policy,
        'path': path
    })

def value_iteration(grid, grid_size, end_pos):
    # Define actions: up, right, down, left
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    action_names = ['up', 'right', 'down', 'left']
    
    # Initialize value map
    v_map = np.zeros((grid_size, grid_size))
    
    # Initialize policy map (now will store lists of actions instead of single actions)
    policy = [[[] for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Value Iteration parameters
    gamma = 0.9  # discount factor
    theta = 0.001  # convergence threshold
    max_iterations = 1000
    
    # Value Iteration algorithm
    for _ in range(max_iterations):
        delta = 0
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == end_pos or grid[i][j] == -5:  # Skip terminal or obstacle states
                    continue
                
                v = v_map[i, j]
                
                # Try all possible actions
                action_values = []
                for idx, (di, dj) in enumerate(actions):
                    ni, nj = i + di, j + dj
                    
                    # Check if next position is valid
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        reward = grid[ni, nj]
                        action_values.append(reward + gamma * v_map[ni, nj])
                    else:
                        # Hitting the wall, stay in place
                        action_values.append(-0.1 + gamma * v_map[i, j])
                
                # Take the action with maximum value
                v_map[i, j] = max(action_values)
                
                # Update policy - now include all actions with max value
                max_value = max(action_values)
                best_actions = []
                for idx, val in enumerate(action_values):
                    # Include action if its value is close enough to the max value
                    if abs(val - max_value) < 1e-10:  # Use small epsilon for floating point comparison
                        best_actions.append(action_names[idx])
                policy[i][j] = best_actions
                
                delta = max(delta, abs(v - v_map[i, j]))
        
        if delta < theta:
            break
    
    return v_map, policy

def find_path(start_pos, end_pos, policy, grid_size):
    path = [start_pos]
    current = start_pos
    
    # Define actions
    action_deltas = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }
    
    # Maximum steps to prevent infinite loops
    max_steps = grid_size * grid_size
    steps = 0
    
    while current != end_pos and steps < max_steps:
        i, j = current
        actions = policy[i][j]
        
        if not actions:  # No valid action
            break
        
        # Just take the first action if there are multiple optimal actions
        action = actions[0]
        
        di, dj = action_deltas[action]
        ni, nj = i + di, j + dj
        
        # Check if next position is valid
        if 0 <= ni < grid_size and 0 <= nj < grid_size:
            current = (ni, nj)
            path.append(current)
        
        steps += 1
    
    return path

if __name__ == '__main__':
    app.run(debug=True)
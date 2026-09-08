# Question 17: Basic RNN for sequence prediction. Train on time series or text data.

import torch
import torch.nn as nn

# Create training sequences
# 1,2,3 -> 4
# 2,3,4 -> 5
# 3,4,5 -> 6
X = torch.tensor([[[1.0], [2.0], [3.0]],
                  [[2.0], [3.0], [4.0]],
                  [[3.0], [4.0], [5.0]]])

# Define target values
y = torch.tensor([[4.0],
                  [5.0],
                  [6.0]])

# Create an RNN layer
input_size = 1   # one value at each time step
hidden_size = 5  # five hidden neurons
rnn = nn.RNN(input_size=1, hidden_size=5, batch_first=True)

# Create an output layer
# Converts RNN output into the final prediction
fc = nn.Linear(5, 1)

# Define the loss function
# Measures the difference between predicted and actual values
criterion = nn.MSELoss()

# Create an Adam optimizer
# Updates the weights of both RNN and output layer
# lr specifies the learning rate
optimizer = torch.optim.Adam(list(rnn.parameters()) + list(fc.parameters()), lr=0.01)

# Train the model for 1000 epochs
for epoch in range(1000):
    # Pass input sequences through the RNN
    # RNN returns output and hidden state
    # Hidden state is not used, so it is ignored using _
    output, _ = rnn(X)
    
    # Use the last output of the sequence for prediction
    prediction = fc(output[:, -1, :])
    
    # Calculate prediction error
    loss = criterion(prediction, y)
    
    # Clear previously stored gradients
    optimizer.zero_grad()
    
    # Calculate gradients
    loss.backward()
    
    # Update weights using gradients
    optimizer.step()

# Create a new sequence for testing
# Expected next value is approximately 7
test = torch.tensor([[[4.0], [5.0], [6.0]]])

# Disable gradient calculation during testing
with torch.no_grad():
    # Pass test sequence through the RNN
    output, _ = rnn(test)
    # Predict the next value
    prediction = fc(output[:, -1, :])

# Display the predicted value
print("Predicted Value :", prediction.item())

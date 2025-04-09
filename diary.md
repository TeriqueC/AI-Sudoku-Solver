# Sudoku interface

## Importance of interface implementation
The main focus for the start of my project needs to be the interface for displaying the sudoku. this is a necessary starting point as in order to demonstrate Artificial Intelligence solving the sudoku, my product needs to be able to display both the unsolved and solved solution in a way that is easily digested by the target audience. the borders, regions, numbers and void values need to be distinct and observable to those trying to understand what the AI algorithms is trying to achieve, and if the algorithms are doing so correctly. that makes this element of the product integral to the development of my project.

## Implementation of sudoku interface
In order to implement this feature, i have decided to initially work on a console based interface. i felt this was necessary as my first iteration of the sudoku interface only needs to display an easily readable representation of the sudoku puzzle. this was achievable in the console as the borders can be represented through the '-' character for row division and '|' character for column division, the numbers as just numbers and the void values as an '*' character. this gave a simple and easy to read sudoku display on the console.

## Planned improvments to the interface
Once the other features of my project have become slightly more developed, I plan to return to improve the sudoku interface through various means, such as randomised sudoku generation of varying difficultly, as well as a better user interface to display the sudoku rather than primarily using the console, which works well and is readable, but is not the best means of displaying the puzzle in a visually appealing and user friendly fashion.

# Solving algorithm

## how a backtracking algorithm could solve a sudoku
A backtracking works similar to how a human would back track. The algorithms makes an attempt to solve a problem. so in the case of a sudoku it would attempt to fill in blank squares with a potential solution, and when a problem occurs in its solution, it goes back to the cause of the problem, which would be the invalid potential solution in that square or a previous one, and continues its attempt with a different solution for the sudoku, and this is done repeatedly till a viable solution is formed.​

## implementation of backtracking algorithm
When developing the solving algorithm, first came the crutial element of finding a blank square in the grid, this would be represented by a 0 in the sudoku grid array. the coordinates on the grid would be returned to the main algorithm when found, then using these, the main loop will attempt to fill the square with numbers ranging from 1 to the max value, which is also the length of the grid (usually 9), until a viable value for the square is found (a value that is not repeated in the row, column or sub-grid). if a viable value cannot be found, the algorithm clears the current square and backtracks to the previous square, and checks the next values for viability, if there are no viable values, the algorithm will clear the current square and backtrack once again to the square before and once again try different values until a different viable value is found and the algorithm searches for the next blank value and the algorithm repeats itself, until there is no more blank squares, or no more values to try on the grid that gives a solution to the problem.

## planned improvements for the backtracking algorithm
In order to improve the speeds of my backtracking algoritihm, I would need to look into my uses of exhaustive searches which is used alot in my algorithm for different functionalities such as, finding an empty square by looping through every value in the grid array, checking validity of a value by searching through every value in the row, column and sub-grid for a repeated value. this is very inefficient and I believe this can be rectified by maybe implementing faster search algorithms or making use of other methods and techniques to make the searches slightly quicker and efficient, which is necessary to prove AI's superior problem solving capabilities.

# improvement of the user interface

## creating a Graphical user interface
When creating my graphical user interface to display the sudoku and the solving algorithm, I decided to pygame as it provides an adaptable environment in which the sudoku grid can be drawn on the window and updated with little difficulty while still being able to display a way of visualising the backtracking algorithm. when creating the grid I decided to give it the length 340 which was big enough for the user to see the sudoku and the values in each square clearly. When dividing the grid into sub-grids I used the same divisor logic used in the console print function, however I divided the grid visually using thicker lines to create the division between the whole and sub grids. I then started adding values to square by placing a new square over the empty square with the intended value, this could be cleared through overwritting the square by filling the surface with a white square then updating the value to a new square to cover the cleared square. this function would be need to be called every time the value changed in the algorithm in order to give the visual backtracking effect.

## the benefits of having a GUI to display the problem solving algorithm
By introducing a GUI to display the solving algorithm, I am able to show the step by step solution being formed through mistake adaptation approach my backtracking algorithm takes as well as showing how quickly the computer can calculate this as the GUI updates the values very rapidly, demonstrating how much faster a computer is compared to a human, despite the GUI technically wasting computer processing speed, so it is faster to print the output directly then updating a GUI, but then the algorithm will not be demonstrated in an easily comprehensible manner.

## planned improvements to the GUI
In order to improve the Graphical User Interface I plan to make use of radio buttons or checkboxes to select which algorithm to use when solving the puzzle, I also feel a reset button to clear the grid and start button to start the algorithm would also be a nice touch, and will make the application experience more convienient. Additional text would also be needed, and useful for displaying the time it takes for solving the problem as well as potentially a mistakes counter for how efficiently/accurately it initially solves the problem.

# next solving algorithm

## how could a Neural Network solve a sudoku
My focus moving forwards will be on developing a Neural Network that will be trained on taking in sudoku solutions, this is so that it will learn what a solution to a sudoku should look like and it should recognise the patterns/rules of a sudoku so that when it is faced against a incomplete sudoku, it will be able to provide an accurate prediction of a solution, that will hopefully be the correct answer to the inputted problem.

# layers of the network

## Conv2D 
is used to extract features, makes use of filters called kernels to produce feature maps, which aids in pattern recognition in the network. the use of filters allows for parameter sharing which means less parameters are needed for the network to generalise better as filters cover multiple parts of the input. currently uses varied filter sizes and kernel sizes 3x3.

## BatchNormalisation 
aims to standardise the inputs so that the process of training becomes more stable and efficient. this allows for a higher rate of learning and quicker training processes, it also helps to prevent overfitting by adding on a bit on "noise" to the input of each layer. does this through working out the mean and variations of the inputs, then normalises based on the results.

## MaxPooling2D 
works by reducing spacial dimensions of the input data in order to reduce complexity and memory consumption in computations. it does this by keeping the maximum value from the pooling window, which helps to highlight prominent features, which improves generalisation and reduce overfitting.

## Dropout 
hopes to achieve a reduction in overfitting by randomly dropping out neurons (resetting to 0) so that the network is forced to learn redundant representations of the data, also allowing for better generalisation by preventing network from being too specialised to the training data. dropout can aid in reducting co-adaptation which is where neurons depend on other specific neurons, this means single neurons can learn more robust features independently. 

## Flatten layer
 converts the multidimestional data into a singular dimension which is what is needed as input for the dense layers of the CNN so that they can process and learn from the test data.

## Dense layers
 are fully connected layers as each neuron in this layer is connected to every neuron in the previous layer, so every input now has an impact of every output, which gives the model the ability to learn the patterns and complex relations of the training data.

# types of activations

## activation functions
this is the function in which the neurons in the network uses to learn and make decisions as it determines which neurons should activate and pass data to other layers to form the final prediction.

## ReLU
this is an activation function which works by taking in the input x and setting the output to x if positive (output is same as input) and if x is negative (x<=0) the output of the output is 0, this is a simplistic activation which is great for computational efficiency however, can lead to dying ReLU problem were neurons set to 0 are inactive consistently and therefore not learning.

## leaky ReLU
this is a variant of ReLU which attempts to address the dying ReLU problem by allowing for a very small non zero values which is calculated by multiplying the input with a very small constant (for example 0.01) if the input is x<=0 and just outputting x if the input is positive. this prevents neurons from being repeatedly deactivated in the network as they avoid the output being set to 0.

## ELU
this activation also aims to prevent the dying ReLU problem by using and exponential function on inputs <=0, this allows for the output to avoid being set to zero, as it is set closer to 0 but not actually 0, so the dying neuron problem is avoided. otherwise, for positive inputs, the output remains the same as the input.

## softmax
softmax is a final layer activation which this ensures that all output probability is normalised so that all probabilities add up to 1, so that it is perfect for classification as the probabilities is appropriately distributed over classes (perfect for sudokus as each cell has classes 1-9 as a potential solution).

# Model compilation

## network optimizer
a network optimizer is used to help adjust the weights of neurons and the biases in the neural network while in its training phase. it works to reduce the loss (errors) of the network while improving the accuracy of the predictions. it uses backpropagation to update network parameters based on gradient calculations, which in turn helps the neural network learn the dataset.

## learning rate
when using the Adam optimiser, the learning rate can effect the accuracy of the model during its learning phase, it is important as this dictates how much the models weights adapt when learning. the size in which this value is set can effect the speeds of convergence and as a result the training time, as well as how precise the updates in the weights which can improve the accuracy as well as keeping the rate of error (loss) to a minimum.

## loss function
this function is important for the training of the model, as this function is how the accuracy of the model prediction is calculated. this is needed to provide a measure on how well the model is performing on the training dataset. this function also works with the loss function to aid in the adjustment of weights and biases, to try and limit the loss which helps the model to learn more efficiently and predict more accurately. with classification models it is common to use a Cross-Entrophy loss function, as this helps with the models learning process.

# model training

## epochs
each time a model trains through an entire training set, this is called an epoch. the number of epochs refers to the number of times the model will cycle through the same entire training set. having multiple epochs are important as this allows for the model to better understand the data as one train through is not typically enough for the model to learn to effectively and accuratly predict. However, if there are too many epochs, there is a chance for the model to learn the specific training set and as a result will struggle to predict new examples which means it is overfitting.

## batch size
this is the amount of samples the network takes from the training set and trains with in one forward and backward pass. smaller batch sizes can lead to more frequent updates to the model which can help to make better predictions as well as consuming less computational resources, but larger batches despite the greater computational demand, can train the model much faster as well as having more stable updates which give smoother convergence.

## callbacks
callbacks can be helpful in the training phase of the model as it can provide a range of functionalities such as improving performance through early stoppage if validation loss stops decreasing (to avoid overfitting) and saving checkpoints for the model while training on the set so that at the end it can restore the point with the best learnt parameters.

# problems encountered

## severe underfitting
A serious issue that came with my first few drafts at developing my model is extreme underfitting. this is where the model was failing to properly learn from the training set, this was a serious issue as if it wasn't accurately learning and predicting with the training set, when I test it on new data, the prediction I get from the model is very much inaccurate and could not even pass as an almost solved sudoku. I believe the reasons for this the low numbers of conv2D layers, as well as very small filters and kernel sizes, in addition to extremely high batch sizes. these will need to be more finely adjusted to try and discover the appropriate model for solving a sudoku puzzle.

## extreme training durations
after adjusting the sizes of filters and conv2D layers, as well as the types of activation those layers required, I found when having too many layers, around 5 or more, and filters above 162 and greater, with kernels (5,5) and higher each and in combination gave extremely high training times per epoch, some parameters coming up to 5 hours on each epoch, which is very computationally exhaustive and in some cases not even beneficial as the models accuracy would be barely increasing in these hours, meaning the model is training past its peak which could be and indication of overfitting. 

## slight overfitting
with some of my larger model attempts, I would yeld better predictions to the sudokus I would pass in, however due to the long times spent training, the model would provide very high accuracy but slightly lower validation accuracy and when testing on new data would provide sudoku solutions with quite a few mistakes. I think moving forwards the model will need some parameters reduced and some of the data and layers more normalised or even dropped out in order to try and avoid neuron dependancy and overfitting in the model, which should smooth out and reduce mistakes made when solving the problem.

# potential solutions to the problems encountered

## number of Conv2D layers
increasing the number of convolutional layers can increase the models ability to learn by better extracting features from the training set being passed in so that it can use those features to classify and predict far more accurate predictions. however too many layers brings overfitting and can increase computational costs significantly.

## increased number of filters
by using more filters the convolutional layers are able to extract a deeper representation of the data, detecting patterns and features more precisely and as a result returning predictions with far less errors. although with greater increases in filters, the greater the demand on training durations, which may not give much in return.

## increased kernel sizes
larger kernels allows for the network to capture more extensive spatial features of the training data, this allows for smoother feature extractions as well as reduction the amount of layers the network would need to capture these features. similarly to the layers and filters, too many can still increase the computational costs in training the model and this could also lead to overfitting.

# final improvements to the User Interface

## improved layout
adjustments to the User Interface has been made to better center the sudoku on screen and also providing an instructions section to the application describing how the user can use the app, as well as providing a section in which the time the algorithm takes to provide the solution along with the number of mistakes it has made to come up with its final solution.

## use of additional inputs
allows user to use keys on the keyboard to navigate through different features of the app, such as number keys to switch between the sudoku problems, the enter key to solve with backtracking, the space key for the Neural Network solution and the backspace to clear the current solution leaving the user back with the unsolved sudoku puzzle.
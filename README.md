# challenge-chess-ai

Dataset: https://www.kaggle.com/datasets/datasnaek/chess
https://database.lichess.org/ May 2022

### Solo Project

<h2 align="center">Chess AI challenge</h2>
<p align="center"><a href="https://becode.org/">
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center"> Chess AI project at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
<h3 align="center"> Contributors: <a href="https://https://github.com/BertramDHooge"> Bertram</a></h3><br>

  
## The timeline of the project: 
**20/06/2022 - 30/06/2022*

## Project flow

This was the final project for a 6 month datascience course followed by me at BeCode. In this project the learners were given a few potential projects, but were also allowed to propose a more personal challenge which is how I ended up attempting to make a chess AI. The first challenge I came across was deciding what type of AI to use in the project. The current trend in Chess is to use neural networks and reinforcement learning to have an algoritm that improves continuously as more data and time is given, however, given the specs of my personal computer, this didn't seem to be the best way to tackle this project for me. So I defined 3 potential ways to feasibly build a chess AI within the restraints of both time and resources: 

1. Standard minimax using pointscores
2. Predicting the "best" move using a boardstate and moves from a better chess engine
3. Predicting the "human" move using moves played in a game

After some deliberation (and some lost days working on a function to transform a boardstate into a useable matrix state) I ended up working on trying to predict the "human" move using the moves played in a game.

To do this I split the games into sequences of 10 moves each, and split those into early game (the first 10 moves) and later game. Then I built a neural network that would see the game as a sentence of sorts and used NLP to predict the next move in the same way such an algoritm would predict words in a sentence.

## Next steps

At the current point (end of project) the algiritm is just able to give a list of potential moves with a confidence value for each one, but without taking into account leglity. Next would be to make a function that takes a game and a list of potential moves and is able to extract the legal moves and "play" a move, either by just picking the move with the highest confidence value or (more desirable) selecting one using a weighted random seletion using the confidence values a weights. 

Beyond this, I would also like to try my hand at building the other 2 potential algoritms I defined and eventually maybe even a reinforcement learning algoritm using all 3 of these algoritms. 

## Objectives of the project: 
* Building a basic chess AI

## Sources (both inspiration and code):
* Using NLP to predict "human" moves:
  * https://towardsdatascience.com/hacking-chess-with-decision-making-deep-reinforcement-learning-173ed32cf503
* NLP word prediction:
  * https://towardsdatascience.com/next-word-prediction-with-nlp-and-deep-learning-48b9fe0a17bf
  * https://medium.com/analytics-vidhya/nlp-word-prediction-by-using-bidirectional-lstm-9c01c24b2725
* General programming hints and issues:
  * [Stack Overflow](https://stackoverflow.com/) (obviously)
  * [HowToGeek](https://www.howtogeek.com/)

## Usage:
* The project can currently not be cleanly run as desired

## Project outline:

* [x] Extracting relevant data from [chessgame dataset](https://www.kaggle.com/datasets/datasnaek/chess) (about 20 000 games)
* [x] Splitting the games into sequences of 10 moves
* [x] Training a neural network to detect the 10th move in the sequence
* [ ] Selecting a legal move from the predicted results using weighted random selection

## Dataset details:
[Dataset](https://www.kaggle.com/datasets/datasnaek/chess) contains the following columns :

[x] relevant for this project
[ ] not relevant for this project

* [ ] Game ID; 
* [ ] Rated (T/F);
* [ ] Start Time;
* [ ] End Time;
* [ ] Number of Turns;
* [ ] Game Status;
* [x] Winner;
* [ ] Time Increment;
* [ ] White Player ID;
* [x] White Player Rating;
* [ ] Black Player ID;
* [x] Black Player Rating;
* [x] All Moves in Standard Chess Notation;
* [ ] Opening Eco (Standardised Code for any given opening, list here);
* [ ] Opening Name;
* [x] Opening Ply (Number of moves in the opening phase)

Not all relevant data is currently used, at the end of the project only the moves themselves were used, no additional data.

# Tic Tac Toe

This is my python implementation of Tic Tac Toe.

*From Wikipedia:*

Tic-tac-toe (American English) is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. 

## Current features

- An ASCII-based board.
- A "help" function for the player.
- A "surrender" function.
- Will correctly identify games that cannot be won by either player, and declares a draw

## Lessons learned

Overall a fun project to work with. It was tougher than expected and took a whole week to complete, but in the process I learned a ton about the git workflow and valuable lessons in humility.

Here are a few of my lessons learned.

### Checking diagonals
The biggest challenge was `LogicChecker._check_diagonals()`. I started off on the wrong foot by incorrectly assuming there could only be one diagonal (top left to bottom right) and this mistake rippled through my code. My tests failed to pick up on this for the simple reason that I couldn't test a problem I didn't know existed. Consequently, with green text from pytest giving me the thumbs up, I was lulled into a false sense of security. I confidently pushed https://github.com/Oyvind-Ege/TicTacToe/commit/39b861dad1cc6815d4f5aa79e11ef2f2a39190ee with the message "working victory conditions". Hurrah!

I discovered the logioc error when showing the game to a friend. Embarassed, I quickly hacked together what I thought was a solution, https://github.com/Oyvind-Ege/TicTacToe/commit/0a159786997f284f0331b6132b7ed04f7eff56a5, but this made things worse. It took a few more days of work before I finally rewrote the whole thing.

So what were the lessons learned?

1. **Understand the problem**. I didn't think enough about diagonals and made an egregious assumption. Going forward, I will consider the problem from multiple angles.
2. **Use TDD to truly consider edge cases. Don't cut corners**. TDD is a wonderful paradigm. It should force you to think through the problem and write appropriate tests. But writing a few tests and calling it a day is not TDD. Which leads to:
3. **Green tests are not guarantees**. Tests do not guarantee anything if they are premised on the same false assumptions as the code.


### Checking for draws
Another challenge was the draw checking logic. I spent quite a while on this, essentially from commit https://github.com/Oyvind-Ege/TicTacToe/commit/39b861dad1cc6815d4f5aa79e11ef2f2a39190ee to the latest version (one whole week).

The current code is a mess and the result of multiple iterations and hacks. 

I think the root of the problem is that I began to code too early. I once more did not consider the problem carefully and didn't have a clear mental model of what I was trying to do. I also didn't focus on one task at a time and making small "improvements" here and there as I spotted them ( https://github.com/Oyvind-Ege/TicTacToe/commit/219e352ab6a433dc56fb3dcdf844ea14ee3ce8d4 ). 

Lessons?

1. **Dont code too early**. Take your time to get a clear mental model.
2. **Focus on one task at a time**. Don't get scatterbrained and leave pawprints all over the code.

### Git
Working with git was completely new to me. In the beginning I really didn't know what I was doing. I pushed here and there, stashed this and that ( https://github.com/Oyvind-Ege/TicTacToe/commit/9a458fbd55092f8e1876d2f96a9155c672997d45 ), and wasn't sure how things worked.

I slowly got a hang of how to push and pull, but was still new to the workflow. For example, I made a lot of premature pushes to origin ( https://github.com/Oyvind-Ege/TicTacToe/commit/84ba91e3edc496f0badf5ae5e18b9f3119694397 ) only to discover that I had left out something, then pushed again ( https://github.com/Oyvind-Ege/TicTacToe/commit/f04b1e05b897bb3c42ee5e82d4b86ae4c5396402 ), and again( https://github.com/Oyvind-Ege/TicTacToe/commit/b4602416a1aa16fae2d9c477bd9fe824911ac83b ). This stuff is just ugly. But ,more worryingly, I sometimes pushed to origin without running my test suite ( https://github.com/Oyvind-Ege/TicTacToe/commit/e2fca26f6796729e16c033bb2a8bf1e83bc92a32 ).

I am not too hard on myself. It's just Tic Tac Toe. But still: it's crucial that I clean up my git commits and establish a good workflow. 

1. **Run tests before you push to origin**
2. **Establish a checklist, mental or otherwise, with everything that should be included in a push**.
3. **Consider origin pushes as milestones.**


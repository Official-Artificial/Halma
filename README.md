# Halma
CS470/570 Artificial Intelligence

Program #4: Life in the Game… (a.k.a., Implementing Adversarial Search)

Adapted from Dr. D’s Spring 2018 offering.
Overview:

It’s time to have some fun! And, of course, to get some more hands-on experience with applied AI techniques. As you’ve noticed from the past programming tasks, there’s a huge difference between talking about something theoretically in lecture and implementing a real piece of “smart” software based on the concept! And yet it’s creating a clever piece of software that AI is all about…

For our final project this year, we will divide the class up into teams that will each create an implementation of a simple board game called Halma. For the final project, each team will have to present their implementation as a programming deliverable, complete with write-up, just as usual. The fun twist will be that we’ll actually have a tournament at the end, where teams will run their Halma players head-to-head, with strict per-turn time limits, to see who has the smartest program. Of course, appropriate rewards will be given to the winner, as outlined below.

Let the games begin!
The Problem:

Because our main aim is to focus on the concepts of adversarial search and building some sort of smart game player, we want to choose a game that is relatively simple: simple board, simple rules, simple pieces, and simple piece movement. This will make encoding the basic foundations straightforward and will let teams focus on fine-tuning their gaming engines to make them as clever as possible. The simple board game Halma meets these criteria perfectly: the board is a simple square, there is only one kind of game piece, and movement rules are the same for all pieces. And yet it should be complex enough to create a reasonable-sized search space deep enough to reward finely-tuned implementations.

You can read all about Halma on the wikipedia page: https://en.wikipedia.org/wiki/Halma. It’s basically a game that was invented at by a surgeon at Harvard Medical School in the late 1800s, and has the distinction of being “the only truly American board game.” It is essentially a simplified version of Chinese Checkers, a better-known update developed later on.

The concept is very simple: you have a square board and play diagonally, from corner to corner. Each player starts with some pieces in their corner known as their camp (or also yard), and the goal is to get all of your pieces into the other person’s camp. The main points of the rules we’ll observe are:

    The game is turn-taking. We’ll flip a coin to see which player moves first, and there will be a time limit to make a move (e.g. 2 minutes).
    The “standard” Halma board is 16x16 in size, but 8x8 and 10x10 variations are common. Since this shouldn’t really affect any code (if we do this right), we will technically allow different board sizes; you pass in the board size as you start a game.
    Pieces can move in any direction that free space exists, and may also jump other pieces. See details of legal moves on the wiki page. There is no obligation to jump, and jumps may end before making all possible jumps in the chain.
    Once pieces have entered the goal camp, they can never leave it; once they have left their own home area, they can’t go back.
    There may be other rules or refinement tweaks that we add along the way, as needed based on evolving development and questions.

Although the Halma challenge is fairly simple as far as games go, it will still take some substantial time and effort to get all the little bits programmed and working right. Thus, we will divide up into teams for this challenge. To help people out a bit with their planning and division of labor, we’ll outline the programming task into distinct overall tasks, and we’ll have some “proof-of-progress” milestones along the way.
The Assignment:

Your task, as indicated above, is to work in self-selected teams of to create a correct and (hopefully!) skilled Halma playing agent. The agent will provide a graphical view of the game board, as well as a basic two-player turn-taking interface. Here is the basic use case:

    You open a terminal window on the gaming machine and invoke python on your game program, providing appropriate command-line parameters:
        bsize: Board size: 8, 10, or 16
        t-limit: Number of seconds allowed for each move. So that the algorithm can monitor its own time usage in order to present a move before the time limit runs out.
        h-player: Which player you (the human) are: Red or Green. Green always gets to move first.
        optional: you could allow passing in the filename of a “board file” containing a particular board. This can be useful during development. If nothing is passed in, it sets up a starting board.
    A window with the graphical representation of the board pops up, with sides marked as Human and Computer, depending on who’s playing what color. Like a chess board, the board is labeled with letters (‘a’ though ‘h’ ; or j or p, depending on board size) along the bottom (horizontal) edge, and numbers (1 through 8; or 10 or 16, depending on board size) along the vertical edge. This coordinate system is used to refer to board locations. The players’ camps are in the top-left and bottom-right corners and, for the sake of uniformity for everyone, let’s say that RED is always shown in the top-left, as on the graphic shown here.
    Status output: There is a “status bar” above the board; this is just a text area where you can display messages from your program to show what’s going on.
    Move input. Here you can choose what t�o provide. Basic: there is a “move entry” text area below the board. This appears/activates when it’s the human’s turn to enter a move. GUI I/O (extra points): You use clicking to move pieces, e.g., click the piece you want to move, then click the place to move it to.
    You start the game, and play proceeds by taking turns.
        If it is your (human) turn, you are asked to enter a move, e.g., text entry would be “a3->b4”. If you input an illegal move, it tells you and you get to try again. When you enter a legal move, the specified piece is graphically moved and (a) your most recently-moved piece is highlighted in some way, plus (b) the square you moved from is highlighted in some small way (slight background color change, tiny pebble marker, whatever). This makes it easy to see where each player moved to most recently. This highlighting stays until the next move is made, at which point it updates. There is no time limit on the human move.
        If it’s the computer’s turn, an “I’m thinking!” label appears in the status bar along with a timer counting down from the max. move limit time. When the computer stops thinking and makes a move, the same move highlighting techniques specified above are used for the computer’s move. Make the move highlighting different colors for computer and human to keep things clear.
    When a player wins, the game ends, which is clearly announced in a dialog that also shows (a) number of move-cycles made (b) the final score for each player. The score is the number of pieces in the goal camp, plus (1/d) for each piece outside the camp, where d is the SLD distance between that piece and being somewhere in the home camp. This helps give credit for close games and almost winning.

Timeline and organization:

To help teams organize and to make sure everyone contributes their share of effort, we will divide this task up into a couple of phases, each of which has a list of things to get done. The idea is that these smaller tasks will be assigned to individuals on the team, who are then responsible for getting them done. Of course, individual teams can choose to slice, redistribute, team up on, and otherwise organize tasks within their team as they see fit, but some clear accounting of who did what must be produced at the end. Here are the phases:
Basics Phase: Manual game playing framework, just to get the framework up and running.

This creates the basic game playing framework that allows two humans to play, but is missing an intelligent computer player. Has roughly these main pieces:

    Graphical board object: responsible for putting up board window, drawing board, and placing pieces on board. Methods might include init (passing in some board), and update, in which you pass it a next board. It then displays the next board, including the move highlighting to mark what piece got moved. Here are a couple of tech tips for doing simple graphics in Python.
    Win/loss detector. This is just a function (method of board object, most likely) that takes in a game board and reports whether somebody won. This is actually fairly easy: you just need to see if red/green has gotten all their pieces into the opposite camp.
    Move generator, v1: You’ll need a fast accurate move generator, so you’ll want to get that done right away. Ultimately, you’ll want to tune this module to the max, because it gets called **a lot** by your smart agent in the next phase. For now, just concentrate on getting a method that, given a board and whose turn it is to move (red/green), returns all possible legal moves that player could make. Don’t forget to have it look for jumps…that’s the tricky part!
    A “move” method. Takes in a current board and a move, and returns either a new board after making the move, or an error of some sort to indicate that the move is illegal. The computer player can, of course, avoid even generating illegal moves (in the move generator). But you also need to make sure the human player doesn’t enter illegal moves! This is easy: you just have your move generator (which only generates legal next moves) generate all possible next moves for the human. Then just check that the move that the human just entered is in that list!
    Main Game object: This is the main object that runs the game overall. It generates the starting board, calls the board object to set up the graphical display, handles turn-taking mechanics including user input (including detecting illegal moves (which is easy, just use your move generator!)), keeps the time, and prints out various status messages in the status bar. It also includes miscellaneous pieces like reporting a winner when that happens….including related stats (number of moves, jump moves made by each player, etc).

Milestone: when done with the basics stage, you should have a functioning game management system for two human players: It presents the game and then asks each player in turn for their move, moving pieces accordingly, reporting illegal moves, and reporting wins and scores.
Brains Phase: Creating your Halma agent

Now add a “computer player” by creating a smart Halma playing agent. Assuming that you have the basics in place, including a well-functioning moves generator, this part should be fairly straightforward. The main pieces are:

    You need to create your “player” object that gets created as the game starts, passing it the move time limit, which player (red or green) it is, and anything else you need to configure it.
    Minimax search. The main method you’ll want to create is “make-a-move”, which will just take in a game board (i.e. the current board that you’re supposed to move from), and will then search down the game tree using minimax search with alpha-beta pruning to return a next move. As you’ll recall (review Ch5!) this is essentially just a depth-limited DFS search, with MIN and MAX alternating at each level. It might be useful to return a move as an object: not just the move itself, but also some useful stats on how the search for it went: number of boards examined, depth of ply finished, value of starting board and board reached by move.
    Alpha-beta pruning. This is really an add-on to your Minimax search engine, as discussed in Ch5, allowing it to prune off whole sub-trees of the search space. Which has no effect on the ultimate outcome of the search, but will save tons of time…which will allow your program to search further ahead while staying in the time limit…which will help you WIN! If you return a move object (see last point), then you can easily add some alpha-beta stats to it to help visualize function, e.g., how many prunes and at what level/ply they occurred.
    Utility function. This is basically a more subtle version of the “win detector” from phase1. This function “scores” a board based on its “goodness”. What exactly it looks like to do this is part of the magic you’ll want to build into your solution! The most basic version might just add up the distance that each piece is from being in the “goal camp” (lower scores are best). More sophisticated versions will look at whether you are setting yourself or (your opponent!) up for fast-forward jumping moves.

Just getting your player up and playing legal Halma is only the first step, of course. If you want to WIN the tournament, you’ll want to leave plenty of time for refining and fine-tuning your player. Your basic goal here would be to streamline every aspect of the code related to exploring downward in the game tree so that you can fully search as many plies as possible within the time limit. This might mean streamlining often-called functions like the move generator and utility function, but perhaps also exploring other more efficient/compact board representations.

Ultimately, you need to stay within the time limit, so you’ll want to test enough to know how long it takes your program, maximally, to search one ply, two plies, three plies, etc etc. That way, when the game starts and the time limit is given, you can tell your program to search to some ply that you know is well within that limit, and return a move…then use any remaining time to have it try to tackle the next ply. If time runs out, you can return the move you have; if you can finish another ply, you have an even better move to return!
The Tournament. Finding out who has the most artificial intelligence chops…

This project is the Final Project for the course, and thus is due at the designated time for the final exam. During this time, we will hold a tournament. We can negotiate some details as the time approaches, but the basic plan is to meet in the classroom, establish a playoff bracket, and have a series of head-to-head matches to determine who is the Halma champion. It will go like this:

    The tournament will be played using an 8x8 board, 10 pieces each, with starting position as shown here.
    Each team must bring at least one laptop that has functioning versions of Python2 and Python3 installed.
    Two teams that are playing each other will choose a laptop to play on; both programs get loaded onto that laptop so that there are no hardware advantages. (If the teams agree that both of their team laptops are of comparable performance, they could play on two laptops). The two Halma players are started on the laptop, one with a red human player, one with a green human player.
    The green player goes first: that player’s Halma agent thinks and then generates a move. That move is entered manually by the observing humans into the other running program as “the human’s move”; that agent then generates a responding move; which is then entered back into the other program. And so on.
    All Halma agents must be quiescent after generating a move. That is, they must generate a move, then prompt for the human player’s next move…and then block, waiting for that move to be entered. Specifically: no multi-threading and burning resources in the background!
    If an erroneous move is detected, or some other error/crash happens, then the program that has crashed/errored forfeits the match. If the error was a fluke and time is still left in the round, the match should be restarted if possible, to allow the losing team a chance to prove that their player mostly works.

Dr. D will act as referree, and will be circulating around, scoring the different programs as play progresses. The final round will be played on the class video screens, and bets will be taken!

There are always small details and questions that will arise that are not addressed here, but we can resolve these quickly as we go along. Here are rules for a few detailed situations that have come up in the past:

    No “input area” is required if you provide an elegant and effective direct-manipulation (e.g. clicking on board) way to enter moves. Still must highlight most recent move as spec’d above.
    No null moves: Handles the perverse situation of whether you can do a jump…and on the second hop, jump back to where you started. The answer is “no”. In other words: legal moves will always land you somewhere other than at your starting point.
    Wins by time-out: It is possible that (for whatever reason) a game will not complete within a set amount of time. If a game is terminated prematurely, the winner is the player who, at that moment, has the best score, as calculated by the metric suggested under “utility function”, i.e., sum of shortest straight-line distances of all piece to the goal area. Uses Pythagorean in simplest way: SQRT(SQR(row-diff) + SQR(col-diff)) where your target is the nearest square inside the goal area. You should print this score in your display area as a running total, re-calc’d after every move you make.
    Move times. We are sticking with what was originally specified: allowed time/move will be decided in each round, and entered as a param when launching the players. The move time may be different for each round/game, so your players should adapt smoothly to different limits, i.e., always return a move in the limit, but utilize all time available. We might minor “overage” on move time once or two, but you’ll forfeit if you go over limit frequently.
    Blocking: Blocking is when a player leaves pieces in their home area late into the game, which of course could prevent (“block”) the opponent from getting their pieces into the opposing home area to win. We decided to handle this in a simple fashion, no complex programming required: At the end of the game, if there are pieces in the home area blocking an otherwise possible win, we will simply declare a win. So: if you could win if it were not for the blocking, then you win.

Scoring for this project

Scoring for this project will be similar to that for previous project (effort invested, performance on tests/tournament, quality of code), but adapted for teams and the tournament at end. There are three basic deliverables for this project:

    Your report for Phase 1, including write-ups and demos.
    Your report for Phase 2, including write-ups and demos.
    The tournament, which evaluates the final functional value of your effort.

The hardcopy deliverables will describe the nature and extent of your implementation, including exactly who worked on what parts of the product on each team. The tournament provides the proof of what you state in your write-ups; it’s where the rubber hits the road.

The detailed scoring will, of course, be left up to your professor, but the basic outline goes like this:

    0-60% – Team has a fully-functional manual version of a Halma playing program.
    60-90% – Team has a fully-functional Halma agent, i.e., program with smart computer player. Detailed points depend on level of smartness, as described in write-up and demonstrated in tournament.
    90-100% – The last 10% of the points will be doled out as premiums in the tournament: winner gets 10%, second gets 7.5%, third gets 5%

Project Deadlines and Deliverables:

As outlined above, the project is divided into two phases to help make sure that teams are moving along, and stay on track to produce a good product on time at the final. Each deliverable is a PDF uploaded to bblearn; the details and deadlines are as follows:
Phase 0 Deliverable

Single nicely-formatted page with: Team name, team logo (optional), Team members (max 4 students per team), course, assignment title, date.

This establishes the team and is essentially the cover sheet that you’ll use for the remaining deliverables.
Phase 1 Deliverable

Phase 1 Deliverable consists of the following, presented exactly in the order shown below:

    Cover sheet: Team name, team logo, Team members, course, assignment title, date
    Overview. A brief description of how you chose to architect your project: overview of the key objects/classes and their key methods.
    Effort description. This documents in a fairly precise fashion, which teammate worked on what parts of the project and how that person performed. Start with an overall statement of how you split up the work in the phase, e.g., “We discussed our skills/interests and this is what came out <discuss>. Given this, we generally decided that Joe would lead on X, Suzy would lead on Y, and Pat would lead on Z”. The heart is then a detailed table that shows the major tasks involved in that stage. You could use my bullets above as a starting point, but ultimately its up to each team to decide how to split up the work. The table has four columns: Task description, Assigned to, Percentage of effort, completion notes. How to fill this out:
        Task description obviously outlines what the task is, with focus on functionalities expected in the outcome product.
        Percentage of effort is the percentage of effort that this task took out of the total effort invested for this project phase. Obviously the sum of %effort across all tasks in the phase by all team members (i.e., the effort column as a whole) should total up to 100%. By totalling the effort for tasks done by any one person, one would get the percentage of effort invested by that person in this particular project phase; in an ideal team, that number would be 1/N percent, where N is the number on the team.
        Tasks are assigned to ONE person on the team; it is that person’s sole responsibility to see that the task gets done.
        Completion notes document what actually happened. In the best case, it just says “completed and satisfactory”. If the team member was not able to complete the task and another team member had to jump in, this is documented here. Describe what happened, and state what percentage of the task (task owner versus rescuer) performed.
    Functionality checklist. This documents precisely the functionality that you completed for this phase. Hopefully, this is just a series of “100% working” checkmarks. Make this a table as well, with three columns: Functionality, %complete, notes. Here are the items in the “Functionality” column:
        Graphical board display: Generates nicely-formatted GUI for your system, including the board, plus status and move entry areas
        Board updating: GUI can receive updates to the board, display them smoothly, and includes move highlighting to chose from/to places of last-moved piece.
        Move generator: Given a board and which player to move, it produces a correct and complete list of possible next moves, including jumps.
        Win detector: Given a board and a player, correctly returns whether it is a winning (or losing!) board for that player.
        A “move” method. Takes in a board and a move and returns either a new board (after making move), or an error report detailing a bad move.
        Fully functional play mode: A Game object that plays a fully functional manual game, taking in moves from two human players in alternating sequence, showing the boards, reporting bad moves, and reporting win/loss.
        Any extra/additional functionality that you innovated and think is worth highlighting.
    Demos: Clearly labeled and annotated screenshots that very clearly demonstrated each of the above. In the best case, this is just a sequence of screenshots (labeled and annotated) of two humans playing your game, showing the board, some both good and erroneous moves, and ultimately a win by someone. Obviously, if your product is not able to play a coherent game, then you’ll need to at least demo each of the pieces that you did get working. Let’s hope it doesn’t come to that…

Phase 2 Deliverable

    Cover sheet: Team name, team logo, Team members, course, assignment title, date
    Overview: Similar to phase 1, but now extended to focus on the creation of your intelligent Halma agent. Condense your description of the basics from Phase1 (labeling them as “Phase1” pieces), but leave them in so as to give a complete picture. Then add in (labeling as Phase 2) what objects/classes you added to upgrade your program into an intelligent system for playing Halma. Be sure to discuss the design of your utility function, i.e., what metrics it uses to determine the “goodness” of a board.
    Effort Description. Exactly as for Phase 1, but now centered around your Phase2 tasks, as assigned to team members.
    Functionality Checklist. Just as for Phase 1, but now has the following items for the Functionality column:
        Utility function. Have a fully-functional utility function that, given a board, return some non-trivial (i.e. actually useful) measure of how strong that board is.
        Minimax search. Is able to take a board, which player is moving, and some indication of how much to search (either #plies directly, or the time it has to move), and will return a move. At very least, it returns a legal move to make each and every time. At best, it returns a really good move to make!
        Alpha-beta. Can be turned on or off (for testing purposes) in your call to minimax search. Implements the alpha-beta algorithm correctly. Has some way of reporting the pruning events, so that you can effectively debug/demo its efficacy.
        Any extra/additional functionality that you think is worth highlighting.
    Demos: Same thing as before, but focus it on your “intelligent” pieces. Some specifics to show would be:
        Your unit testing for minimax: show some board, then start minimax on that board with some time limit, then show the resulting move plus all the stats: how many plies you went down, how many boards where generated/examined, and time taken.
        Your alpha-beta being awesome. Using the same board as above, now show your minimax running with alpha-beta turned ON. One would hope to see the stats improve (more boards within same time…or less time for same number of boards), plus some indication of how many pruning events happened and on what ply/level.

# codespaces_python_chess
python chess game built using codespaces but it is chess with an advanced variant

__Gametypes__
#Computer
  with Varying Difficulty (Easy, Hard, AI, Bad AI)

#2 Player
  switches turns each round:

#Multiplayer
  (local host) create lobby (creates a server with a code to join) , join lobby (joins a server using a code)
  (rest framework) online - join server, post get methods ...



__Gamemodes__

#Classic Chess:


        a b c d e f g h
      +-----------------+
    8 | r n b q k b n r | 8
    7 | p p p p p p p p | 7
    6 | - - - - - - - - | 6
    5 | - - - - - - - - | 5
    4 | - - - - - - - - | 4
    3 | - - - - - - - - | 3
    2 | P P P P P P P P | 2
    1 | R N B Q K B N R | 1
      +-----------------+
        a b c d e f g h


#Chess 2 - Full Court Chess
(Variation : https://imgur.com/a/VrSwn40 )

    
        a b c d e f g h i j
      +---------------------+
    8 | r n b e q k C b n r | 8
    7 | l p p p p p p p p l | 7
    6 | - - - - - - - - - - | 6
    5 | - - - - - - - - - - | 5
    4 | - - - - - - - - - - | 4
    3 | - - - - - - - - - - | 3
    2 | l P P P P P P P P l | 2
    1 | R N B e Q K C B N R | 1
      +---------------------+
        a b c d e f g h i j



#MOBA Chess - two types:


#AutoChess Chess:


    Your board:
        a b c d e f g h
      +-----------------+
    8 | - # - # - # - # | 8
    7 | # - # - # - # - | 7
    6 | - # - # - # - # | 6
    5 | # - # - # - # - | 5
    4 | - - - - P - - - | 4
    3 | - - - - - - - - | 3
    2 | - - - - P - - - | 2
    1 | - - - - K - - - | 1
      +-----------------+
        a b c d e f g h
        
    1. Open Shop | 2. View Enemy Board | 3. Manage Board | 4. End turn | 5. Game Options

    Enemy board:
        h g f e d c b a
      +-----------------+
    8 | - - - K - - - - | 8
    7 | - - - P - - - - | 7
    6 | - - - - - - - - | 6
    5 | - - - P - - - - | 5
    4 | - - - P P - - - | 4
    3 | - - - K - - - - | 3
    2 | - - - - - - - - | 2
    1 | - - - - - - - - | 1
      +-----------------+
        h g f e d c b a

    1. Close Board | 2. Change Enemy Board | 3. Show your view | 4. Manage your board | 5. Exit | 6. Game Options

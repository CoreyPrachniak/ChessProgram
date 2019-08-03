# Chess-Program

Welcome to Corey’s chess program! Please enter a string of legal moves in Algebraic Chess notation,
and the program will output the resulting position. For additional instructions, see below:

- This program can handle all chess moves that could be legal for some existing chess position.
- Enter moves <chess location> to see the legal movements of the piece on <chess location>.
- Moves may be entered omitting the numbers that represent move number.
- You may go back to a previous positions by repeatedly entering Undo.
- To cycle between appearances of the chess board, press enter.
- The program stops running at checkmate or stalemate.

## Test Games
Here are some test games that you may use as inputs:


```
1. e4 e6 2. d4 d5 3. e5 c5 4. c3 cxd4 5. cxd4 Bb4+ 6. Nc3 Nc6 7. Nf3 Nge7 8. Bd3 O-O 9. Bxh7+ Kxh7 10. Ng5+ Kg6 11. h4 Nxd4 12. Qg4 f5 13. h5+ Kh6 14. Nxe6+ g5 15. hxg6e.p.#
```

```
1. e4 e5 2. Nf3 d6 3. d4 Bg4 4. dxe5 Bxf3 5. Qxf3 dxe5 6. Bc4 Nf6 7. Qb3 Qe7 8. Nc3 c6 9. Bg5 b5 10. Nxb5 cxb5 11. Bxb5+ Nb8d7 12. 0-0-0 Rd8 13. Rxd7 Rxd7 14. Rd1 Qe6 15. Bxd7+ Nxd7 16. Qb8+ Nxb8 17. Rd8#
```

```
1. e4 d6 2. Bc4 Be6 3. Bb3 Nc6 4. d4 Nf6 5. Bg5 h6 6. Bxf6 exf6 7. d5 Bd7 8. dxc6 Bxc6 9. Nc3 d5 10. Nxd5 g5 11. Qh5 Bxd5 12. Bxd5 Bb4+ 13. c3 Bc5 14. Qxf7#
```

The game below was played by two grandmasters recently. It ended in a resignation, therefore this program will not terminate here.

```
1. d4 Nf6 2. c4 g6 3. Nc3 d5 4. Nf3 Bg7 5. h3 O-O 6. Bg5 Ne4 7. Nxe4 dxe4 8. Ne5 f6 9. Qb3 fxe5 10. O-O-O exd4 11. e3 Nc6 12. c5+ Kh8 13. exd4 Nxd4 14. Qe3 Qd5 15. Bxe7 Re8 16. Bg5 Qxc5+ 17. Kb1 Qc2+ 18. Ka1 Qxd1+ 19. Qc1 Qxc1+ 20. Bxc1 e3 21. fxe3 Nc2+ 22. Kb1 Bf5 23. g4 Be4 24. Bb5 Na3+ 25. Ka1 Bxh1 26. Bxe8 Rxe8 27. h4 Rd8 28. g5 Rd1
```

## Stalemate Games

The games below end in stalemate. 

```
1. c4 h5 2. h4 a5 3. Qa4 Ra6 4. Qxa5 Rah6 5. Qxc7 f6 6. Qxd7 Kf7 7. Qxb7 Qd3 8. Qxb8 Qh7 9. Qc8 Kg6 10. Qe6
```

```
1. c4 h5 2. h4 a5 3. Qa4 Ra6 4. Qxa5 Rah6 5. Qxc7 f6 6. Qxd7 Kf7 7. Qxb7 Qd3 8. Qxb8 Qh7 9. Qc8 Kg6 10. a4 Kf7 11. a5 Kg6 12. a6 Kf7 13. Ra5 Kg6 14. Qe6
```
Here is a setup for testing the legality of castling. Notice that the white king has moved previously (so white castling will not be allowed).

```
1. e4 e5 2. d4 d5 3. Ke2 Qd7 4. g3 g6 5. Bg2 Bg7 6. Nf3 Nf6 7. Ke1 a6
```

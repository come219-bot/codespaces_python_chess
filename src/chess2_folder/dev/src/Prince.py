from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

from src.Coordinate import Coordinate as C
from src.Move import Move
from src.Piece import Piece

if TYPE_CHECKING:
    from src.Board import Board

WHITE = True
BLACK = False

# if the prince is promoted, it acts as another king.
PROMOTED = False


class Prince(Piece):
    stringRep = 'E'
    value = 3

    def __init__(
            self, board: Board, side: bool, position: C, movesMade: int = 0
    ) -> None:
        super(Prince, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self) -> Iterator[Move]:

	if PROMOTED == False:
		currentPos = self.position
        movements = [
            C(0, 1),
            C(0, -1),
            C(1, 0),
            C(-1, 0),
            C(1, 1),
            C(1, -1),
            C(-1, 1),
            C(-1, -1),
        ]
        for movement in movements:
            newPos = currentPos + movement
            if self.board.isValidPos(newPos):
                pieceAtNewPos = self.board.pieceAtPosition(newPos)
                if self.board.pieceAtPosition(newPos) is None:
                    yield Move(self, newPos)
                elif pieceAtNewPos.side != self.side:
                    yield Move(self, newPos, pieceToCapture=pieceAtNewPos)

# Castling
        if self.movesMade == 0:
            inCheck = False
            kingsideCastleBlocked = False
            queensideCastleBlocked = False
            kingsideCastleCheck = False
            queensideCastleCheck = False
            kingsideRookMoved = True
            queensideRookMoved = True

            kingsideCastlePositions = [
                self.position + C(1, 0),
                self.position + C(2, 0),
            ]
            for pos in kingsideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    kingsideCastleBlocked = True
                    break

            queensideCastlePositions = [
                self.position - C(1, 0),
                self.position - C(2, 0),
                self.position - C(3, 0),
            ]
            for pos in queensideCastlePositions:
                if self.board.pieceAtPosition(pos):
                    queensideCastleBlocked = True
                    break

            if kingsideCastleBlocked and queensideCastleBlocked:
                return

            otherSideMoves = self.board.getAllMovesUnfiltered(
                not self.side, includeKing=False
            )
            for move in otherSideMoves:
                if move.newPos == self.position:
                    inCheck = True
                    break
                if (
                        move.newPos == self.position + C(1, 0)
                        or move.newPos == self.position + C(2, 0)
                ):
                    kingsideCastleCheck = True
                if (
                        move.newPos == self.position - C(1, 0)
                        or move.newPos == self.position - C(2, 0)
                ):
                    queensideCastleCheck = True

            kingsideRookPos = self.position + C(3, 0)
            kingsideRook = (
                self.board.pieceAtPosition(kingsideRookPos)
                if self.board.isValidPos(kingsideRookPos)
                else None
            )  # TODO kingsideRook shouldn't be None to match Move class
            if (
                    kingsideRook and kingsideRook.stringRep == 'R'
                    and kingsideRook.movesMade == 0
            ):
                kingsideRookMoved = False

            queensideRookPos = self.position - C(4, 0)
            queensideRook = (
                self.board.pieceAtPosition(queensideRookPos)
                if self.board.isValidPos(queensideRookPos)
                else None
            )  # TODO queensideRook shouldn't be None to match Move class
            if (
                    queensideRook and queensideRook.stringRep == 'R'
                    and queensideRook.movesMade == 0
            ):
                queensideRookMoved = False

            if not inCheck:
                if (
                        not kingsideCastleBlocked and not kingsideCastleCheck
                        and not kingsideRookMoved
                ):
                    move = Move(self, self.position + C(2, 0))
                    rookMove = Move(kingsideRook, self.position + C(1, 0))  # type: ignore[arg-type]  # noqa: E501
                    move.specialMovePiece = self.board.pieceAtPosition(kingsideRookPos)  # type: ignore[assignment]  # noqa: E501
                    move.kingsideCastle = True
                    move.rookMove = rookMove  # type: ignore[assignment]
                    yield move
                if (
                        not queensideCastleBlocked and not queensideCastleCheck
                        and not queensideRookMoved
                ):
                    move = Move(self, self.position - C(2, 0))
                    rookMove = Move(queensideRook, self.position - C(1, 0))  # type: ignore[arg-type]  # noqa: E501
                    move.specialMovePiece = self.board.pieceAtPosition(queensideRookPos)  # type: ignore[assignment]  # noqa: E501
                    move.queensideCastle = True
                    move.rookMove = rookMove  # type: ignore[assignment]
                    yield move



# ELSE	elif:

        board = self.board
        currentPos = self.position
        movements = [
            C(2, 1),
            C(2, -1),
            C(-2, 1),
            C(-2, -1),
            C(1, 2),
            C(1, -2),
            C(-1, -2),
            C(-1, 2),
        ]
        for movement in movements:
            newPos = currentPos + movement
            if board.isValidPos(newPos):
                pieceAtNewPos = board.pieceAtPosition(newPos)
                if pieceAtNewPos is None:
                    yield Move(self, newPos)
                elif pieceAtNewPos.side != self.side:
                     yield Move(self, newPos, pieceToCapture=pieceAtNewPos)




### or use pawn promotion code to promote when king is in check ?? requires king data

insert into board(Location) select Location from revertBoard;

insert into board(Piece) select Piece from revertBoard;

insert into board(Colour) select Colour from revertBoard;

insert into board(Which) select Which from revertBoard;


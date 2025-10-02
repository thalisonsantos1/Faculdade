INSERT INTO tbl_Livro
(NomeLivro, ISBN, DataPub, PrecoLivro, NumPaginas, Edicao, IdAssunto, IdEditora)
VALUES
('SSH, the Secure Shell','9780596008956', '2005-05-17', 58.30, 435, 1, 1, 2),
('Using Samba','9780596002565', '2003-12-21', 61.45, 385, 1, 1, 2),
('Fedora and Red Hat Linux', '9780133477436', '2014-01-10', 62.24, 780, 1, 1, 4),
('Windows Server 2012 Inside Out','9780735666313', '2013-01-25', 66.80, 1236, 2, 1, 3),
('Microsoft Exchange Server 2010','9780735640610', '2010-12-01', 45.30, 950, 3, 1, 3),
('Practical Electronics for Inventors', '9781259587542', '2016-03-24', 67.80, 963, 4, 1, 5);


INSERT INTO tbl_autor_livro (IdAutor, IdLivro)
VALUES
(1, 1), -- Gerald Carter, SSH
(2, 2), -- Mark Sobell, Using Samba
(3, 3), -- William Stanek, Fedora and Red Hat Linux
(4, 4), -- Richard Blum, Windows Server 2012 Inside Out
(4, 5), -- Richard Blum, Microsoft Exchange Server 2010
(12, 6), -- Simon Monk, Practical Electronics
(13, 6); -- Paul Scherz, Practical Electronics
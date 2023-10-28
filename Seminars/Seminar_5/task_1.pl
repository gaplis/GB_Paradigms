% Задание 1:
%
% Контекст:
% Продолжаем исследовать генеалогию с помощью
% логического программирования. Подобный пример мы уже
% разбирали на лекции. На этот раз ваша задача реализовать
% генеалогическое древо на языке Prolog самостоятельно.
%
% Ваша задача:
% Реализовать изображённое генеалогическое древо на языке
% Prolog таким образом, чтобы про Алексея и Анастасию можно
% было узнать кто их: мать, отец, дедушки, бабушки, дети.

female(lubov).
female(galina).
female(anastasiya).
female(vera).
female(olga).

male(alexsey).
male(alexander).
male(serafim).
male(vladimir).
male(sergey).

parent(vera, lubov).
parent(vera, sergey).
parent(alexsey, galina).
parent(alexsey, vladimir).
parent(anastasiya, vera).
parent(anastasiya, alexsey).
parent(olga, vera).
parent(olga, alexsey).
parent(serafim, anastasiya).
parent(serafim, alexander).

father(X, Y):- parent(X, Y), male(Y).
mother(X, Y):- parent(X, Y), female(Y).

grandpa(X, Z):- parent(X, Y), father(Y, Z).
grandma(X, Z):- parent(X, Y), mother(Y, Z).

child(X, Y):- parent(Y, X).

% father(X, vera), write(X), write('\n').
% grandpa(X, serafim), write(X), write('\n').
% mother(X, vera), write(X), write('\n').
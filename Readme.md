1.Utilisation du polymorphisme 
Nous avons une classe de base [WorkOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5) avec une méthode [printMessage()](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L67C9-L67C21) qui est définie. Ensuite, nous avons une classe dérivée [WorkOnDates](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L67C9-L67C21) qui hérite de la classe [WorkOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5) et redéfinisse la méthode  [printMessage()](https://github.com/troliti420/OOP/blob/main/workOnDates.py#L55) pour rendre un message différent.

Le polymorphisme se produit lorsque la méthode [printMessage()](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L67C9-L67C21) est appelée pour differents classes, et le comportement est differents.

2.Utilisation de l'encapsulation 
La classe [Checker](https://github.com/troliti420/OOP/blob/main/checker.py#L12) a les attributs [_personalInfo](https://github.com/troliti420/OOP/blob/main/checker.py#L15), [_optionWord](https://github.com/troliti420/OOP/blob/main/checker.py#L16) et [_optionDate ](https://github.com/troliti420/OOP/blob/main/checker.py#L17) qui sont des variables d'instance protégées.

L'encapsulation est utilisée ici pour restreindre l'accès direct aux attributs [_personalInfo](https://github.com/troliti420/OOP/blob/main/checker.py#L15), [_optionWord](https://github.com/troliti420/OOP/blob/main/checker.py#L16) et [_optionDate ](https://github.com/troliti420/OOP/blob/main/checker.py#L17) depuis l'extérieur de la classe.

3.Utilisation de composition 
Dans l'init de la classe  [checker](https://github.com/troliti420/OOP/blob/main/checker.py#L12) on déclare [workOnStrings](https://github.com/troliti420/OOP/blob/main/checker.py#L19)
La composition permet à la classe [checker](https://github.com/troliti420/OOP/blob/main/checker.py#L12) d'utiliser et d'accéder aux fonctionnalités de la classe [WorkOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5), tout en maintenant une séparation claire entre les deux classes. Cela offre une plus grande flexibilité et facilite la gestion des dépendances entre les différentes parties d'un système.

4.Utilisation de l'héritage 
Nous avons une classe de base [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5).

Nous avons une classe dérivé [workOnDates](https://github.com/troliti420/OOP/blob/main/workOnDates.py#L5)  qui hérite de la classe [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5). Cette classe étends la classe de base [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5).

5.Utilisation d'interface 
En Python, il n'y a pas de concept d'interface formel. Donc on utilise des classes abstraites et des méthodes abstraites pour simuler une interface.

On a une classe abstraite [printMessageInterface](https://github.com/troliti420/OOP/blob/main/printMessageInterface.py#L4) qui définit la méthode abstraite [printMessage](https://github.com/troliti420/OOP/blob/main/printMessageInterface.py#L6). Ces méthodes sont des "contrats" que toutes les classes dérivées de [printMessageInterface](https://github.com/troliti420/OOP/blob/main/printMessageInterface.py#L4) doivent implémenter.

Ensuite, nous définissonsla classe [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5) qui hérite de la classe [printMessageInterface](https://github.com/troliti420/OOP/blob/main/printMessageInterface.py#L4) et implémente la méthode  [printMessage](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L67).

6.Utilisation de méthodes et attributs d'objets
Nous avons une classe [PasswordGenerator](https://github.com/troliti420/OOP/blob/main/passwordGenerator.py#L4). Elle possède plusieurs attributs. Les méthodes de la cette classe sont définies pour interagir avec les objets de la classe.

7.Utilisation de méthodes et attributs statiques 
Nous avons la classe [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5) qui contient un attribut statique.
[Message](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L6) est un attributs statiques utilsé [ici](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L68)

8.Utilisation de méthodes et attributs de classe 
Nous avons la classe [workOnStrings](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L5) qui contient une méthode de calsse.
[stringOptions](https://github.com/troliti420/OOP/blob/main/workOnStrings.py#L63C9-L63C22) est une méthode de classe statiques utilsé [ici](https://github.com/troliti420/OOP/blob/main/workOnDates.py#L52)


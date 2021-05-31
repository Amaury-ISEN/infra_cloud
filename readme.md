**Une infra dans le cloud**
**Auteurs** : Ronan et Amaury

**Résumé du projet** :
Une API est installée dans le cloud amazon sur une instance elasticbeanstalk de manière conteneurisée à l'aide de Docker. L'API est bâtie via docker-compose.

L'API a un script principal main.py et un script secondaire data.py qui contient la partie BDD (connexion et requêtes).

L'API discute avec une base de donnée hébergée sur une instance Amazon RDS Postgre et effectue possiblement deux requêtes simples.

L'API fonctionnait en local mais nous avons eu des difficutés lors du déploiement. Pour faire fonctionner l'API dockerisée en conditions réelles sur notre instance sans que le endpoint ne buggue, il a fallu installer via SSH un serveur nginx sur le linux de notre instance elasticbeanstalk.
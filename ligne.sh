#!/bin/bash

# on définit les variables pour les commandes à exécuter 
command1="ls -l"
command2="df -h"

# on crée le fichier de sortie 
output="command_output.txt"

# on exécute les deux commandes et on stocke le résultat dans le fichier de sortie
$command1 >> $output
$command2 >> $output

# on affiche un message de confirmation 
echo "Les commandes ont été exécutées et le résultat a été stocké dans $output"
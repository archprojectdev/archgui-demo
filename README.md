
# <p align="center">Archgui</p>
  
Archgui est un module basé sur `FreeSimpleGUI`. 
Il permet la création de modèle de fenêtre à partir d’un fichier `.json` et d’un fichier `.py` pour les events
correspondant à ce modèle. Le but de ce module est de simplifier la création d’application nécessitant
la gestion de plusieurs fenêtres.

À terme une `GUI` basé sur ce module sera disponible pour la création des fenêtres. 
Il ne sera plus nécessaire d’éditer à la main les fichiers `.json` qui est la partie la plus chronophage,
le gain de temps devrait etre significatif entre une application développée depuis `FreeSimpleGUI` et 
une développée avec la surcouche `Archgui`.


⚠️ Le development de ce module est en cours. 
Ce n’est pour le moment qu’une demonstration incomplète. 
Si vous souhaitez tester ce module, il est préférable de le faire dans un environnement dédié. 


## 😊 Fonctionnalités principales :
- Dimensionnement et positionnement simplifié des fenêtres.
- Dimensionnement et positionnement des fenêtres relatif à une autre fenêtre ou à la résolution du moniteur.
- Création de fenêtre sur la base d’un fichier `.json`.
- Les fenêtres sont gérées comme modèle et peuvent être dupliqué et affiché à volonté.
- Création et affichage de graphique via `MatPlotLib` simplifié.
- Update simple des éléments d’une fenêtre.
- Supporte le multithreading.


## 💻 Fonctionne sous les OS :
- Ubuntu 24.04 
- Windows 11 (en cours de test)


## 🛠️ Nécessite :
- Anaconda
- Python >= 3.10


## 🛠️ Installation :

#### Création de l'environnement via Conda :
```bash
conda create -n archgui_demo python=3.10 anaconda
```

#### Utilisation de l'environnement :
```bash
conda activate archgui_demo
```

#### Ubuntu 24.04 :
```bash
conda install libpython-static nomkl numpy scipy scikit-learn numexpr
conda remove mkl mkl-service

conda install -c conda-forge tk=*=xft_*
conda install -c conda-forge nuitka pynput screeninfo

pip install freesimplegui
```
#### Windows 11 :
```bash
conda install libpython-static nomkl numpy scipy scikit-learn numexpr
conda remove mkl mkl-service

conda install -c conda-forge tk=*=xft_*
conda install -c conda-forge nuitka pynput pywin32

pip install freesimplegui
```
La différence d’installation se fait entre le module `screeninfo` pour Ubuntu et `pywin32` pour Windows.



## 🛠️ Utilisation :

Lorsque les Windows ou Events sont modifiés, 
le module doit être lancé avant le script principal pour la copie et la modification de `Loader.py`. 
Cette partie est nécessaire pour la prise en compte des modifications. 
Cela permet de facilité la compilation sous Nuitka.

```bash
python -m archgui windows=ag_windows events=ag_events config=ag_config.json
python monscript.py
```
Il est nécessaire définir un dossier hors du module pour les Windows et Events ainsi 
que le fichier de configuration par défaut. 


- Les fichiers Events manquant seront générés dans le dossier défini par `events=`.
- Le fichier de configuration par défaut défini par `config=` sera généré s’il n’existe pas.


## 🛠️ Nuitka :
Compilation en onefile sous Nuitka fonctionnelle.
Cela nécessitera l'installation de Nuika par Conda pour avoir la bonne version de `gcc`.

#### Installation :
```bash
conda install -c conda-forge nuitka
```

#### Compilation :
```bash
python -m nuitka --onefile --enable-plugin=tk-inter demo.py
```

## 🧐 Démonstration :
#### Demo A (demo_a.py):
<a href="demo_img/demo_1.png"><img src="demo_img/demo_1.png" align="left" height="100" width="100" ></a>

#### Demo B (demo_b.py):
#### Demo C (demo_c.py):
#### Demo D (demo_d.py):
#### Demo E (demo_e.py):

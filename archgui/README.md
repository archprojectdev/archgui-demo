
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

<br/>

## 😊 Fonctionnalités principales :
- Dimensionnement et positionnement simplifié des fenêtres.
- Dimensionnement et positionnement des fenêtres relatif à une autre fenêtre ou à la résolution du moniteur.
- Création de fenêtre sur la base d’un fichier `.json`.
- Les fenêtres sont gérées comme modèle et peuvent être dupliqué et affiché à volonté.
- Création et affichage de graphique via `MatPlotLib` simplifié.
- Update simple des éléments d’une fenêtre.
- Supporte le multithreading.

<br/>

## 💻 Fonctionne sous les OS :
- Ubuntu 24.04 
- Windows 11 (en cours de test)

<br/>

## 🛠️ Nécessite :
- Anaconda
- Python >= 3.10

<br/>

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


<br/>

## 🛠️ Utilisation :

Après la création de nouvelles fenêtre, il est nécessaire de relancer le module par la commande ci-dessous. Cela est nécessaire pour l'intégration des fenêtres au fichier de lancement `ag_loader.py`.

```bash
python -m archgui windows=ag_windows events=ag_events config=ag_config.json
python test.py
```
Il est nécessaire définir un dossier respectif pour les Windows et Events.
- Les fichiers du dossier `windows=` seront intégré dans le fichier `ag_loader.py`.
- Les fichiers Events manquant seront générés dans le dossier défini par `events=`.
- Le fichier de configuration défini par `config=` sera créé à la racine de l'application s’il n’existe pas.
- Le fichier de lancement du module `ag_loader.py` sera créé à la racine de l'application s’il n’existe pas.

<br/>

## 🛠️ Premier lancement de test :

#### Dossier initial:
```
.
├── archgui
├── ag_events
├── ag_windows
│   └── test.json
└── test.py
```

#### Fichier: ag_windows/test.json :
```json
{
    "parameters": {
        "location_x": "50%",
        "location_y": "50%",
        "width": 516,
        "height": 133
    },
    "items": [[
        [{"t": "column", "k": "column_1", "p": [[0, 0], [0, 5]], "sc": false, "scvo": false}, [
            [
                [{"t": "frame", "k": "frame_1", "v": " Frame 1 "}, [
                    [
                        [{"t": "column", "k": "column_11", "p": [[5, 5], [0, 10]] }, [
                            [
                                [{"t": "label", "k": "label_1", "v": "label_1", "s": [14, 1]}],
                                [{"t": "in_line", "k": "in_line_1", "v": "in_line_1", "s": [20, 1]}],
                                [{"t": "button", "k": "button_1", "v": "button_1", "s": [16, 1]}]
                            ],
                            [
                                [{"t": "in_line", "k": "in_line_2", "v": "in_line_2", "s": [50, 1]}]
                            ]
                        ]]
                    ]
                ]]
            ]
        ]]
    ]]
}
```

#### Fichier: test.py :
```python
from ag_loader import archgui


ag = archgui()

modules = {"archgui": ag}
ag.define_modules(modules)

test_uniqid = ag.open(
    model="test",
    wid="0",
    title="Archgui - Test")

ag.define_main(test_uniqid)

ag.run()
```

#### Lancement du module :
```bash
python -m archgui windows=ag_windows events=ag_events config=ag_config.json
```
#### Dossier avec les fichiers créés :
```
.
├── archgui
├── ag_events
│   └── test.py
├── ag_windows
│   └── test.json
├── ag_loader.py
└── test.py
```

#### Lancement du test :
```bash
python test.py
```

#### Fenêtre obtenue :

![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/test.png?raw=true)


---

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

<br/>
<br/>

---

#### Pour accéder à la partie suivante vous devez vous rendre au depot : [archgui-demo](https://github.com/Seblefdev/archgui-demo)

---
<br/>

### 👉 Demo A :
#### Manipulation des inputs inline text et button.

| Script          | Model                     | Events                 |
|-----------------|---------------------------|------------------------|
| [`demo_a.py`](https://github.com/Seblefdev/archgui-demo/blob/main/demo_a.py) | [`ag_windows/demo_a.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_a.json)  | [`ag_events/demo_a.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_a.py)  |

![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_a.png?raw=true)



<br/>

---
### 👉 Demo B :
#### Création et manipulation d’un graphique via `MatPlotLib`.

| Script          | Model                     | Events                 |
|-----------------|---------------------------|------------------------|
| [`demo_b.py`](https://github.com/Seblefdev/archgui-demo/blob/main/demo_b.py) | [`ag_windows/demo_b.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_b.json)  | [`ag_events/demo_b.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_b.py)  |

![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_b.png?raw=true)



<br/>

---
### 👉 Demo C :
#### Manipulation d’une barre de progression.

| Script          | Model                     | Events                 |
|-----------------|---------------------------|------------------------|
| [`demo_c.py`](https://github.com/Seblefdev/archgui-demo/blob/main/demo_c.py) | [`ag_windows/demo_c.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_c.json)  | [`ag_events/demo_c.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_c.py)  |

![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_c.png?raw=true)



<br/>

---
### 👉 Demo D :
#### Manipulation d'onglet.

| Script          | Model                     | Events                 |
|-----------------|---------------------------|------------------------|
| [`demo_d.py`](https://github.com/Seblefdev/archgui-demo/blob/main/demo_d.py) | [`ag_windows/demo_d.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_d.json)  | [`ag_events/demo_d.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_d.py)  |

![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_d.png?raw=true)



<br/>

---
### 👉 Demo E :
#### Manipulation de plusieurs fenêtres positionnement et dimensionnement relatif.

| Script                                                                       | Model                                                                                                      | Events                                                                                               |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [`demo_e.py`](https://github.com/Seblefdev/archgui-demo/blob/main/demo_e.py) | [`ag_windows/demo_e.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e.json)     | [`ag_events/demo_e.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e.py)     |
| `onclick: button_1`                                                          | [`ag_windows/demo_e_1.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_1.json) | [`ag_events/demo_e_1.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_1.py) |
| `onclick: button_2`                                                                   | [`ag_windows/demo_e_2.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_2.json) | [`ag_events/demo_e_2.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_2.py) |
| `onclick: button_3`                                                                   | [`ag_windows/demo_e_3.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_3.json) | [`ag_events/demo_e_3.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_3.py) |
| `onclick: button_4`                                                                   | [`ag_windows/demo_e_4.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_4.json) | [`ag_events/demo_e_4.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_4.py) |
| `onclick: button_5`                                                                   | [`ag_windows/demo_e_5.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_5.json) | [`ag_events/demo_e_5.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_5.py) |
| `onclick: button_6`                                                                   | [`ag_windows/demo_e_6.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_6.json) | [`ag_events/demo_e_6.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_6.py) |
| `onclick: button_7`                                                                   | [`ag_windows/demo_e_7.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_7.json) | [`ag_events/demo_e_7.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_7.py) |
| `onclick: button_8`                                                                   | [`ag_windows/demo_e_8.json`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_windows/demo_e_8.json) | [`ag_events/demo_e_8.py`](https://github.com/Seblefdev/archgui-demo/blob/main/ag_events/demo_e_8.py) |

[![Image](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_e_0.png?raw=true)](https://github.com/Seblefdev/archgui-demo/blob/main/demo_img/demo_e_1.png?raw=true)

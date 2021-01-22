from sklearn.model_selection import train_test_split
import source.datasets_management as dm
import source.classifiers as clfs
import source.output_management as om


# Leggo, elimino gli esempi cattivi di troppo e divido in train set e test set il dataset Australian

australian_data, australian_target = dm.readAustralian()

australian_data, australian_target = dm.resizeDataset(australian_data, australian_target, 0.7)

australian_data_train, australian_data_test, australian_target_train, australian_target_test = train_test_split(
    australian_data, australian_target, test_size=0.33, random_state=0, shuffle=False)

# Leggo e divido in train set e test set il dataset German
german_data, german_target = dm.readGerman()

german_data_train, german_data_test, german_target_train, german_target_test = train_test_split(
    german_data, german_target, test_size=0.33, random_state=0, shuffle=False)

# proportions indica le varie proporzioni tra i buoni e cattivi esempi sui quali andranno provati gli algoritmi
proportions = [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.975, 0.99]

# Scores conterrà i punteggi ottenuti dagli algoritmi lungo i vari esperimenti
scores = [[[0 for k in range(3)] for j in range(2)] for i in range(len(proportions))]

# Per ogni proporzione, aumento lo sbilanciamento e metto alla prova i classificatori
for i in range(len(proportions)):
    if i != 0:
        australian_data_train, australian_target_train = dm.resizeDataset(australian_data_train, australian_target_train, proportions[i])
        german_data_train, german_target_train = dm.resizeDataset(german_data_train, german_target_train, proportions[i])

    scores[i][0] = clfs.getScores(australian_data_train, australian_target_train, australian_data_test, australian_target_test, proportions[i], 0)
    scores[i][1] = clfs.getScores(german_data_train, german_target_train, german_data_test, german_target_test, proportions[i], 1)

# Stampo le due tabelle
om.plotScoresTable(scores, 'Australian')
om.plotScoresTable(scores, 'German')

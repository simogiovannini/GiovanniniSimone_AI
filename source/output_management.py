import matplotlib.pyplot as plt


# Credits to: https://machinelearningmastery.com/k-fold-cross-validation/
def plotScoresTable(scores, datasetName):
    plt.close()
    var = 0
    if datasetName == 'German':
        var = 1

    data = [[0 for x in range(8)] for y in range(3)]

    for i in range(3):
        ind = 0
        for j in range(8):
            data[i][ind] = scores[j][var][i]
            ind = ind + 1

    column_headers = ('Aus 70/30', 'Aus 75/25', 'Aus 80/20',
                      'Aus 85/15', 'Aus 90/10', 'Aus 95/5',
                      'Aus 97.5/2.5', 'Aus 99/1')

    if datasetName == 'German':
        column_headers = ('Ger 70/30', 'Ger 75/25', 'Ger 80/20',
                          'Ger 85/15', 'Ger 90/10', 'Ger 95/5',
                          'Ger 97.5/2.5', 'Ger 99/1')

    row_headers = ['Perceptron', 'C4.5', 'Random Forest']

    fig_background_color = 'skyblue'
    fig_border = 'steelblue'

    cell_text = []
    for row in data:
        cell_text.append([f'{str(x)}' for x in row])

    plt.figure(linewidth=2,
               edgecolor=fig_border,
               facecolor=fig_background_color,
               tight_layout={'pad': 1},
               )

    the_table = plt.table(cellText=cell_text,
                          rowLabels=row_headers,
                          rowLoc='right',
                          colLabels=column_headers,
                          loc='center')

    the_table.scale(1, 1.5)

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.box(on=None)

    plt.figtext(0.95, 0.05, '', horizontalalignment='right', size=6, weight='light')

    plt.draw()

    fig = plt.gcf()
    fileName = datasetName + '_table.png'
    plt.savefig(fileName,
                edgecolor=fig.get_edgecolor(),
                facecolor=fig.get_facecolor(),
                dpi=150
                )
    pass
